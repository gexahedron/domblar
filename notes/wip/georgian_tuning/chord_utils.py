import math
from collections import namedtuple


OCTAVE_IN_CENTS = 1200

def calc_hz(pitch, ref_hz):
    if pitch is None:
        return None
    return ref_hz * (2 ** (pitch / OCTAVE_IN_CENTS))

def cents_from_hz(hz, ref_hz):
    return math.log(hz / ref_hz) / math.log(2) * OCTAVE_IN_CENTS

def ratio_to_cents(m, n):
    return OCTAVE_IN_CENTS * math.log2(float(m) / n)

def ch(interval_chord):
    pitches = []
    ref = None
    for cents in interval_chord:
        if cents is None:
            pitches.append(None)
            continue
        if ref is None:
            ref = cents
            pitch = ref
        else:
            pitch = ref + cents
        pitches.append(pitch)
    return pitches

def hz2c(chord_in_hz, ref_hz=55):
    chord_in_cents = []
    for hz in chord_in_hz:
        if hz is None:
            chord_in_cents.append(None)
        else:
            chord_in_cents.append(round(cents_from_hz(hz, ref_hz)))
    return chord_in_cents

def check_chords(chords, redux_cents):
    for chord in chords:
        assert(len(chord.gvm) == len(chord.tony))
        assert(len(chord.gvm) == len(chord.redux))
        for i in range(len(chord.gvm)):
            if chord.gvm[i] is None:
                assert(chord.tony[i] is None)
                assert(chord.redux[i] is None)
            elif chord.redux[i] is not None:
                if chord.redux[i] not in redux_cents:
                    print(chord.redux[i], chord)
                assert(chord.redux[i] in redux_cents)
    return True

Chord = namedtuple('Chord', ['timestamp', 'gvm', 'tony', 'redux', 'syllable'])
