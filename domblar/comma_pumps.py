#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyOSC3
import time
import numpy as np
import util
import random
import math
from copy import deepcopy
import ast

import datetime
from collections import defaultdict


client = pyOSC3.OSCClient()
client.connect(('127.0.0.1', 57120))

def send_msg(note, out_bus_idx, cur_timbre):
    try:
        msg = pyOSC3.OSCMessage()
        msg.setAddress("/tonnetz")

        msg.append([note, out_bus_idx, cur_timbre])
        # print('sent', note,'to', out_bus_idx)
        client.send(msg)
        time.sleep(0.001)
    except Exception as e:
        pass


def parse_note(note):
    if note == '-':
        return None
    note_num = 0
    note_names = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
    note_idx = [0, 2, 4, 5, 7, 9, 11]
    note_num = note_idx[note_names.index(note[0])]
    if len(note) == 1:
        return note_num
    if note[1] == 'b':
        note_num -= 1
    elif note[1] == 'd':
        note_num += 1
    if note[-1] not in ['b', 'd']:
        oct_num = int(note[-1])
        note_num += 12 * (oct_num - 1)
    return note_num

def tet_to_hz(note, base_hz):
    return base_hz * (2 ** (note / 12))



def parse(scale):
    ratios = scale.split(', ')
    ratios = [r.split('/') for r in ratios]
    ratios = [(int(r[0]), int(r[1])) for r in ratios]
    return ratios

scale = '1/1, 6/5, 3/2, 5/4, 2/3, 3/4, 3/5, 7/8, 7/4, 5/8, 8/7, 8/5, 4/3'
ratios = parse(scale)
ratios.sort(key=lambda r: util.ratio_to_cents(r[0], r[1]))


primes = [2, 3, 5, 7, 11, 13]
spectrums = dict()
for r in ratios:
    spectrum = [0] * (len(primes))
    nr = [r[0], r[1]]
    for i, p in enumerate(primes):
        while nr[0] % p == 0:
            spectrum[i] += 1
            nr[0] //= p
        while nr[1] % p == 0:
            spectrum[i] -= 1
            nr[1] //= p
    spectrums[r] = np.array(spectrum)


def calc_hz(ji_shift_orig, base_hz):
    ji_shift = deepcopy(ji_shift_orig)
    cur_hz = base_hz
    low_hz = 20
    high_hz = 10000
    while any(ji_shift):
        changed = False
        for i, p in enumerate(primes):
            if ji_shift[i] != 0:
                if cur_hz < low_hz and ji_shift[i] < 0:
                    continue
                if cur_hz > high_hz and ji_shift[i] > 0:
                    continue
                if ji_shift[i] > 0:
                    cur_hz *= float(p)
                    ji_shift[i] -= 1
                else:
                    cur_hz /= float(p)
                    ji_shift[i] += 1
                changed = True
        if not changed:
            print('not changed!', cur_hz, ji_shift)
        assert(changed)
    return cur_hz

def calc_hz_from_cents(cents, base_hz):
    return base_hz * util.cents_to_ratio(cents)


# MOSes:
# (octave, generator, gen_count); both in cents
# (oct_map, gen_map)
class MOS:
    def __init__(self, name, octave, generator, gen_count,
                 oct_map=None, gen_map=None):
        self.name = name
        self.oct = octave
        self.gen = generator
        self.gen_count = gen_count
        self.oct_map = np.array(oct_map)
        self.gen_map = np.array(gen_map)
        ji = [1200.0, 1901.9550008653873, 2786.3137138648344,
              3368.825906469125, 4151.317942364757, 4440.527661769311]
        ji_octave = [1, 1, 2, 2, 3, 3]
        if oct_map is None or gen_map is None:
            assert(util.same(1200, octave))
            assert(generator < octave)
            self.oct_map = np.array([1, 0, 0, 0, 0, 0])
            self.gen_map = np.array([0, 0, 0, 0, 0, 0])
            notes = []
            pitch = 0
            oct_count = 0
            for i in range(gen_count):
                notes.append((pitch, i, oct_count))
                pitch += generator
                if pitch >= octave:
                    pitch -= octave
                    oct_count += 1
            notes.sort()
            for i in range(1, len(ji)):
                nearest_note = None
                nearest_oct = None
                nearest_dist = None
                for oct in range(ji_octave[i] - 1, ji_octave[i] + 2):
                    for n in notes:
                        cur_cents = n[0] + oct * self.oct
                        if nearest_note is None or nearest_dist > abs(ji[i] - cur_cents):
                            nearest_note = n
                            nearest_dist = abs(ji[i] - cur_cents)
                            nearest_oct = oct
                # print('nearest', nearest_note, nearest_oct, nearest_dist, ji[i])
                self.oct_map[i] = nearest_oct - nearest_note[2]
                self.gen_map[i] = nearest_note[1]
            # print('maps:', self.oct_map, self.gen_map)
        self.oct_corr = (self.gen * self.gen_count) // self.oct
        # print('oct correction for', self.name, 'is', self.oct_corr)
        # print('adjusted:', abs(self.calc_adjusted_harmonics() - ji))
        # print('naive:', abs(self.calc_naive_harmonics() - ji))
    def calc_naive_harmonics(self):
        oct_steps = self.oct_map
        gen_steps = self.gen_map
        return self.oct * oct_steps + self.gen * gen_steps
        # return self.oct * (oct_steps + (gen_steps // self.gen_count) * self.oct_corr) +\
            # self.gen * (gen_steps % self.gen_count)
    def calc_adjusted_harmonics(self):
        oct_steps = self.oct_map
        gen_steps = self.gen_map
        return self.oct * (oct_steps + (gen_steps // self.gen_count) * self.oct_corr) +\
            self.gen * (gen_steps % self.gen_count)
    def calc_note_in_steps(self, oct_steps, gen_steps):
        # correct them for finitudeness of MOS
        return self.oct * (oct_steps + (gen_steps // self.gen_count) * self.oct_corr) +\
            self.gen * (gen_steps % self.gen_count)
    def calc_note_in_cents(self, note_in_ji_shift):
        # calc oct_steps and gen_steps:
        oct_steps = sum(self.oct_map * note_in_ji_shift)
        gen_steps = sum(self.gen_map * note_in_ji_shift)
        # correct them for finitudeness of MOS
        return self.oct * (oct_steps + (gen_steps // self.gen_count) * self.oct_corr) +\
            self.gen * (gen_steps % self.gen_count)



# porcupine15 = MOS('porcupine[15]', 1200, 162.708, 15)
tet12 = MOS('tet[12]', 1200, 700, 12)
ji = [1200.0, 1901.9550008653873, 2786.3137138648344,
      3368.825906469125, 4151.317942364757, 4440.527661769311]
# print('7:4', tet12.calc_note_in_cents([-2, 0, 0, 1, 0, 0]))

# miracle21 = MOS('miracle[21]', 1200, 116.63, 21)
miracle21 = MOS('miracle[21]', 1200, 116.63, 21, [1, 1, 3, 3, 2, 4], [0, 6, -7, -2, 15, -3])
# # print(ji[2], 'vs', miracle21.calc_note_in_steps(2, 3))
# # print(ji[2], 'vs', miracle21_wiki.calc_note_in_steps(3, -7))
# print('7:4', miracle21.calc_note_in_cents([-2, 0, 0, 1, 0, 0]))
# print('15:14', miracle21.calc_note_in_cents([-1, 1, 1, -1, 0, 0]))
# print('16:15', miracle21.calc_note_in_cents([4, -1, -1, 0, 0, 0]))
# print('7:4', miracle21_wiki.calc_note_in_cents([-2, 0, 0, 1, 0, 0]))
# print('15:14', miracle21_wiki.calc_note_in_cents([-1, 1, 1, -1, 0, 0]))
# print('16:15', miracle21_wiki.calc_note_in_cents([4, -1, -1, 0, 0, 0]))

# ksajdfk

# xen.wiki: [1, 1, 3, 3, 5, 4], [0, 6, -7, -2, -16, -3])
# mine: [1 1 2 2 2 3] [ 0  6  3  8 15  7] - this one gives a comma pump

# fixme: why my maps are wrong?
# qcomma_meantone19 = MOS('1/4-comma-meantone[19]', 1200, 696.578, 19)
# mavila16 = MOS('mavila[16]', 1200, 679.806, 16)
# htt29 = MOS('secor-htt[29]', 1200, 703.5787, 29)
# dicot11 = MOS('dicot[11]', 1200, 338.846, 11)
# orwell9 = MOS('orwell[9]', 1200, 271.546, 9)
# negri10 = MOS('negri[10]', 1200, 126.431, 10)
# tetracot7 = MOS('tetracot[7]', 1200, 175.622, 7)
# magic13 = MOS('magic[13]', 1200, 380.427, 13)
# maqamic17 = MOS('maqamic[17]', 1200, 350.816, 17)
# hanson15 = MOS('hanson[15]', 1200, 316.611, 15)
# sensi11 = MOS('sensi[11]', 1200, 443.321, 11)



# (a, b)
# a - lists any note which goes further and where it goes
# b - chord, which always includes fraction 1/1
# chords = [
#     ([1, 0], [(1, 1), (6, 5), (3, 2)]),
#     ([0, 0], [(1, 1), (5, 4), (3, 2)]), # пояснение ко второй ноте 5/4: 3/2 = 5/4 * 6/5
#     ([1, 1], [(2, 3), (3, 4), (1, 1)]),
#     ([0, 0], [(3, 5), (3, 4), (1, 1)]),
#     ([0, 0], [(1, 1), (5, 4), (3, 2)]),
#     ([1, 1], [(2, 3), (3, 4), (1, 1)]),
#     ([0, 0], [(3, 5), (3, 4), (1, 1)]),
#     ([0, 0], [(1, 1), (5, 4), (3, 2)]),
# ]

# (1, 1), (5, 4), (3, 2), (7, 4)
chords = [
    ([0, 0], [(7, 8), (1, 1), (5, 4), (3, 2)]),
    ([3, 3], [(1, 1), (5, 4), (3, 2), (7, 4)]),
    ([2, 3], [(5, 8), (3, 4), (7, 8), (1, 1)]),
    ([1, 1], [(5, 8), (3, 4), (7, 8), (1, 1)]),
    ([2, 2], [(1, 1), (8, 7), (4, 3), (8, 5)]),
    ([1, 0], [(7, 8), (1, 1), (5, 4), (3, 2)]),
    ([2, 2], [(1, 1), (8, 7), (4, 3), (8, 5)]),
]

cur_chord = [None] * len(chords[0][1])
prev_chord = deepcopy(cur_chord)

cur_timbre = 0
sleep_time = 0.7
initial_tonic_in_hz = 440
cur_tonic_in_ji_shift = np.array([0, 0, 0, 0, 0, 0])
mos = miracle21

first = True
while True:
    for i, chord_info in enumerate(chords):
        note_map, chord = chord_info
        if not first:
            i1 = 0
            for j, n in enumerate(cur_chord):
                if n is not None:
                    i1 = j
                    break
            cur_tonic_in_ji_shift = cur_chord[i1] - spectrums[chord[i1]]
        first = False

        cur_chord = np.array([cur_tonic_in_ji_shift] * len(cur_chord))
        for j in range(len(chord)):
            cur_chord[j] += spectrums[chord[j]]

        ji_hzs = []
        mos_hzs = []
        for n in cur_chord:
            ji_hz = calc_hz(n, initial_tonic_in_hz)
            ji_hzs.append(ji_hz)
            tempered_note_in_cents = mos.calc_note_in_cents(n)
            mos_hz = calc_hz_from_cents(tempered_note_in_cents, initial_tonic_in_hz)
            mos_hzs.append(mos_hz)
            # if i == 0:
                # send_msg(ji_hz, 0, cur_timbre)
            send_msg(mos_hz, 0, cur_timbre)
        # if i == 0:
            # print('ji hz', ji_hzs[0])
            # print('mos hz', mos_hzs[0])
            # print()
        print(i, 'mos hz', mos_hzs)

        # print('hzs', base_hz, 'vs', cur_hz)
        time.sleep(sleep_time)
        prev_chord = deepcopy(cur_chord)
        cur_chord = [None] * len(cur_chord)
        cur_chord[note_map[1]] = prev_chord[note_map[0]]


# melody = [
#     ['-', '-', '-', 'c'],
#     ['a', 'a', 'g', 'a'],
#     ['f', 'c', 'c', 'c'],
#     ['a', 'a', 'bb', 'g'],
#     ['c2', '-', '-', 'c2'],
#     ['d', 'd', 'bb', 'bb'],
#     ['a', 'g', 'f', 'f'],
#     ['a', 'a', 'g', 'a'],
#     ['f', '-', '-']
# ]
#
# harmonics = [3,5,7,11]
#
# for cycle in melody:
#     for i, note in enumerate(cycle):
#         time.sleep(sleep_time)
#         tet_note = parse_note(note)
#         if tet_note is None:
#             continue
#         note_in_hz = tet_to_hz(tet_note, base_hz)
#         note_in_hz *= harmonics[i]
#         send_msg(note_in_hz, 0, 3)
