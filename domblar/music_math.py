import math
from typing import Tuple

from domblar.synths import Synths


WESTERN_EDO = 12
OCTAVE_IN_CENTS = WESTERN_EDO * 100
A4_MIDI = 69
A4_FREQ = 440.0
C4_FREQ = A4_FREQ * (2 ** (-9 / WESTERN_EDO))


def calc_hz(pitch, ref_hz):
    if pitch is None:
        return None
    return ref_hz * (2 ** (pitch / OCTAVE_IN_CENTS))


def cents_from_hz(hz, ref_hz):
    return math.log2(hz / ref_hz) * OCTAVE_IN_CENTS


# FIXME: rename
def ratio_to_floats(m, n):
    return math.log2(float(m) / n)


def ratio_to_cents(m, n):
    return OCTAVE_IN_CENTS * ratio_to_floats(m, n)


def cents_to_ratio(cents):
    return 2 ** (cents / OCTAVE_IN_CENTS)


def freq_to_midi(freq: float, synth_idx: int) -> Tuple[int, int]:
    pitch_bend_sensitivity = Synths.synths[synth_idx].pitch_bend_sensitivity

    bended_note = A4_MIDI + WESTERN_EDO * math.log2(freq / A4_FREQ)

    # MIDI pitch bend range: [0, 16384)
    # default is 8192, corresponds to absence of bend
    # here we assume that pitch bend should be in 8192+[0..8192)/pitch_bend_sensitivity range
    note = math.floor(bended_note)
    bend = int(8192 * ((bended_note - note) / pitch_bend_sensitivity + 1))
    return note, bend
