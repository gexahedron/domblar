from typing import Tuple

import math
import numbers


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


def ratio_to_cents(m, n):
    return OCTAVE_IN_CENTS * math.log2(float(m) / n)


# TODO: move to edo_math?
def get_freq(note, scale, edo):
    freq = None
    if isinstance(note, numbers.Number):
        in_oct = note % len(scale)
        in_oct = scale[in_oct] / edo
        oct_idx = note // len(scale)
        note_in_linear = in_oct + oct_idx
        freq = C4_FREQ * (2 ** note_in_linear)
    return freq


def freq_to_midi(freq: float) -> Tuple[int, int]:
    """TODO:_summary_

    Args:
        freq (float): _description_

    Returns:
        Tuple[int, int]: _description_
    """
    # this value works both for Dexed in non-MPE mode,
    # and for Plogue chipsynths in MPE mode
    pitch_bend_sensitivity = 48

    bended_note = A4_MIDI + WESTERN_EDO * math.log2(freq / A4_FREQ)

    # MIDI pitch bend range: [0, 16384)
    # default is 8192, corresponds to absence of bend
    # here we assume that pitch bend should be in 8192+[0..8192)/pitch_bend_sensitivity range
    note = math.floor(bended_note)
    bend = int(8192 * ((bended_note - note) / pitch_bend_sensitivity + 1))
    return note, bend
