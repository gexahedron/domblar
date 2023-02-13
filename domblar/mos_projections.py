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


has_keyboard = False

def note_remap(n):
    n = n - 1
    column = n // 7
    row = n % 7
    return column * 7 + 7 - row


client = pyOSC3.OSCClient()
client.connect(('127.0.0.1', 57120))

def send_msg(note, out_bus_idx, cur_timbre):
    try:
        msg = pyOSC3.OSCMessage()
        msg.setAddress("/tonnetz")

        msg.append([note, out_bus_idx, cur_timbre])
        # print('sent', note,'to', out_bus_idx)
        client.send(msg)
        time.sleep(0.002)
    except Exception as e:
        pass


def parse(scale):
    ratios = scale.split(', ')
    ratios = [r.split('/') for r in ratios]
    ratios = [(int(r[0]), int(r[1])) for r in ratios]
    return ratios

# Caleb Morgan's 13-limit superparticular tuning
scale = '1/1, 49/48, 36/35, 21/20, 16/15, 13/12, 11/10, 10/9, 9/8, 8/7, '\
'7/6, 13/11, 6/5, 11/9, 16/13, 5/4, 14/11, 9/7, 21/16, 4/3, '\
'27/20, 11/8, 7/5, 45/32, 10/7, 16/11, 40/27, 3/2, 32/21, 14/9, '\
'11/7, 8/5, 13/8, 18/11, 5/3, 22/13, 12/7, 7/4, 16/9, 9/5, '\
'11/6, 13/7, 15/8, 21/11, 35/18, 55/28'

ratios = parse(scale)
ratios.sort(key=lambda r: util.ratio_to_cents(r[0], r[1]))
# print(len(ratios), ratios)

up_rep_notes = [7, 21, 35, 56, 70, 84]
down_rep_notes = [8, 22, 36, 57, 71, 85]
initial_note_ratios = [None]
cur_ratio_idx = 0
for i in range(1, 98 + 1):
    cur_octave = cur_ratio_idx // len(ratios)
    initial_note_ratios.append((ratios[cur_ratio_idx % len(ratios)], cur_octave))
    if i not in up_rep_notes:
        cur_ratio_idx += 1
print('initial_note_ratios:', initial_note_ratios)
cur_note_ratios = deepcopy(initial_note_ratios)
for i in up_rep_notes:
    assert(cur_note_ratios[i] == cur_note_ratios[i + 1])


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
    # print(r, spectrum)
# print(spectrums)

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


porcupine15 = MOS('porcupine[15]', 1200, 162.708, 15)
qcomma_meantone19 = MOS('1/4-comma-meantone[19]', 1200, 696.578, 19)
miracle21 = MOS('miracle[21]', 1200, 116.715, 21)
mavila16 = MOS('mavila[16]', 1200, 679.806, 16)
htt29 = MOS('secor-htt[29]', 1200, 703.5787, 29)
dicot11 = MOS('dicot[11]', 1200, 338.846, 11)
orwell9 = MOS('orwell[9]', 1200, 271.546, 9)
negri10 = MOS('negri[10]', 1200, 126.431, 10)
tetracot7 = MOS('tetracot[7]', 1200, 175.622, 7)
magic13 = MOS('magic[13]', 1200, 380.427, 13)
maqamic17 = MOS('maqamic[17]', 1200, 350.816, 17)
hanson15 = MOS('hanson[15]', 1200, 316.611, 15)
sensi11 = MOS('sensi[11]', 1200, 443.321, 11)
# fixme:
# blackwood10 = MOS('blackwood[10]', 240, 399, 10, [5, 8, 0, 14, 29, 7], [0, 0, 7, 0, -7, 7])
# wrong notes

moses = [
    tetracot7,
    hanson15,
    porcupine15,
    qcomma_meantone19,
    miracle21,
    mavila16,
    htt29,
    dicot11,
    orwell9,
    negri10,
    tetracot7,
    magic13,
]
# maqamic17,
# sensi11

melodies_file = 'melodies.txt'
melodies = []
with open(melodies_file, 'r') as f:
    ls = f.readlines()
    for l in ls:
        if 'test' in l.split(' ')[0]:
            continue
        base_hz = float(l.split(' ')[1])
        melody = ' '.join(l.split(' ')[2:])
        melody = ast.literal_eval(melody)
        melodies.append((melody, base_hz, l.split(' ')[0].split(':')[1]))


if has_keyboard:
    import mido
    instruments = mido.get_input_names()
    print(instruments)
    inport = mido.open_input(instruments[0])

state = 'stopped'
vernisage_melody = []

cur_melody_idx = 0
cur_note_idx = 0
cur_tonic_in_ji_shift = np.array([0, 0, 0, 0, 0, 0])
cur_note_ratios = deepcopy(initial_note_ratios)

bck_melody = None
bck_melody_idx = None
bck_note_idx = None
bck_initial_tonic_in_hz = None
bck_tonic_in_ji_shift = None
bck_note_ratios = None

# pump_wait_threshold = 0.1

prev_poll_time = None

def play_note(note_info, is_vernisage,
        cur_note_idx, cur_tonic_in_ji_shift, cur_note_ratios, initial_tonic_in_hz,
        cur_timbre):
    hex_note = note_info[0]
    init_ratio, init_octave = cur_note_ratios[hex_note]

    if note_info[1] < timbre_change_wait_threshold:
        cur_timbre += 1

    # do pump
    cur_note_ratios = [None] * len(cur_note_ratios)
    cur_ratio_idx = 0
    for i in range(hex_note, 98 + 1):
        cur_octave = cur_ratio_idx // len(ratios)
        cur_note_ratios[i] = (ratios[cur_ratio_idx % len(ratios)], cur_octave)
        if i not in up_rep_notes:
            cur_ratio_idx += 1
    cur_ratio_idx = 0
    for i in range(hex_note - 1, 0, -1):
        if i not in up_rep_notes:
            cur_ratio_idx -= 1
        cur_octave = cur_ratio_idx // len(ratios)
        cur_note_ratios[i] = (ratios[cur_ratio_idx % len(ratios)], cur_octave)

    for i in up_rep_notes:
        assert (cur_note_ratios[i] == cur_note_ratios[i + 1])

    cur_tonic_in_ji_shift += spectrums[init_ratio]
    cur_tonic_in_ji_shift[0] += init_octave


    ratio, octave = cur_note_ratios[hex_note]

    cur_note_in_ji_shift = cur_tonic_in_ji_shift + spectrums[ratio]
    cur_note_in_ji_shift[0] += octave
    ji_hz = calc_hz(cur_note_in_ji_shift, initial_tonic_in_hz)
    # send_msg(ji_hz, 0, 0)
    # send_msg(ji_hz, 1, 0)
    # prev_note_in_ji_shift = cur_note_in_ji_shift

    # print(idx, 'ratio', ratio, octave)
    # print(idx, 'cur_note_in_ji_shift', cur_note_in_ji_shift)
    # print(idx, 'cur_tonic_in_ji_shift', cur_tonic_in_ji_shift)

    for mos_idx, mos in enumerate(moses):
        tempered_note_in_cents = mos.calc_note_in_cents(cur_note_in_ji_shift)
        if tempered_note_in_cents > 1200 * 5:
            tempered_note_in_cents %= 1200
        if tempered_note_in_cents < -1200 * 2:
            tempered_note_in_cents %= 1200
        mos_hz = calc_hz_from_cents(tempered_note_in_cents, initial_tonic_in_hz)
        if state == 'vernisage':
            mos_hz = ji_hz
        send_msg(mos_hz, mos_idx, cur_timbre)
        #print(mos.name, 'cents:', tempered_note_in_cents, 'hz:', mos_hz, 'vs', ji_hz)

    return cur_tonic_in_ji_shift, cur_note_ratios, cur_timbre


cur_timbre = 0
timbre_change_wait_threshold = 0.1

while True:
    cur_poll_time = datetime.datetime.now()
    if prev_poll_time is None or (cur_poll_time - prev_poll_time).total_seconds() > 1:
        msg = None
        if has_keyboard:
            msg = inport.poll()
        if msg is not None and msg.type == 'note_on':
            velocity = msg.velocity
            cur_note = note_remap(msg.note)
            if cur_note == 85:
                if vernisage_melody:
                    cur_melody = deepcopy(bck_melody)
                    cur_melody_idx = bck_melody_idx
                    cur_note_idx = bck_note_idx
                    cur_tonic_in_ji_shift = deepcopy(bck_tonic_in_ji_shift)
                    cur_note_ratios = deepcopy(bck_note_ratios)
                    initial_tonic_in_hz = bck_initial_tonic_in_hz
                vernisage_melody = []
                print('continue playing melody', melodies[cur_melody_idx][2])
                state = 'stopped'
                continue

            if cur_note == 98:
                state = 'recording'
                if not vernisage_melody:
                    bck_melody = deepcopy(cur_melody)
                    bck_melody_idx = cur_melody_idx
                    bck_note_idx = cur_note_idx
                    bck_tonic_in_ji_shift = deepcopy(cur_tonic_in_ji_shift)
                    bck_note_ratios = deepcopy(cur_note_ratios)
                    bck_initial_tonic_in_hz = initial_tonic_in_hz

                vernisage_melody = []
                initial_tonic_in_hz = 220
                cur_tonic_in_ji_shift = np.array([0, 0, 0, 0, 0, 0])
                cur_note_ratios = deepcopy(initial_note_ratios)
                last_time = datetime.datetime.now()
                while state == 'recording':
                    msg = inport.receive()
                    if msg.type != 'note_on':
                        continue
                    print('msg', msg)
                    velocity = msg.velocity
                    cur_note = note_remap(msg.note)

                    if cur_note == 98:
                        state = 'vernisage'
                        cur_note_idx = 0
                        cur_melody = vernisage_melody
                    else:
                        # todo
                        cur_time = datetime.datetime.now()
                        cur_note_info = (
                            cur_note,
                            (cur_time - last_time).total_seconds(),
                            velocity,
                            cur_note_ratios[cur_note])
                        vernisage_melody.append(cur_note_info)
                        _, _, cur_timbre = play_note(cur_note_info, True,
                                cur_note_idx, cur_tonic_in_ji_shift, cur_note_ratios,
                                initial_tonic_in_hz,
                                cur_timbre)
                        last_time = cur_time

    if state != 'vernisage':
        if cur_note_idx == 0:
            print('starting playing melody', melodies[cur_melody_idx][2])
            cur_melody = melodies[cur_melody_idx][0]
            initial_tonic_in_hz = melodies[cur_melody_idx][1]
            cur_tonic_in_ji_shift = np.array([0, 0, 0, 0, 0, 0])
            cur_note_ratios = deepcopy(initial_note_ratios)

    else:
        if cur_note_idx == 0:
            print('starting playing vernisage melody')

    if cur_note_idx == 0:
        cur_timbre += 1
        prime_pumps = [1] * len(primes)
        for i in range(len(prime_pumps)):
            if random.random() > 0.7:
                prime_pumps[i] *= -1

    # fixme!
    if cur_note_idx >= len(cur_melody):
        cur_melody_idx = 0
        cur_note_idx = 0
        cur_tonic_in_ji_shift = np.array([0, 0, 0, 0, 0, 0])
        cur_note_ratios = deepcopy(initial_note_ratios)

        bck_melody = None
        bck_melody_idx = None
        bck_note_idx = None
        bck_initial_tonic_in_hz = None
        bck_tonic_in_ji_shift = None
        bck_note_ratios = None

        # pump_wait_threshold = 0.1
        state = 'stopped'
        continue

    note_info = cur_melody[cur_note_idx]

    if cur_note_idx == 0:
        time.sleep(0.1)
    else:
        time.sleep(min(note_info[1], 1.5))

    cur_tonic_in_ji_shift, cur_note_ratios, cur_timbre = play_note(note_info, False,
            cur_note_idx, cur_tonic_in_ji_shift, cur_note_ratios,
            initial_tonic_in_hz,
            cur_timbre)

    if state != 'vernisage':
        cur_note_idx += 1
        if cur_note_idx == len(cur_melody):
            print('finished playing melody', melodies[cur_melody_idx][2])
            cur_note_idx = 0
            cur_melody_idx += 1
            if cur_melody_idx == len(melodies):
                cur_melody_idx = 0
            time.sleep(2)
    else:
        cur_note_idx += 1
        if cur_note_idx == len(cur_melody):
            print('finished playing vernisage melody')
            cur_note_idx = 0
            time.sleep(2)
