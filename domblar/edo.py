from copy import copy
import numbers

from domblar.music_math import C4_FREQ


class Scale():
    def __init__(self, notes, edo) -> None:
        self.notes = notes
        self.edo = edo

    def __getitem__(self, note_idx):
        in_oct = self.notes[note_idx % len(self.notes)]
        oct_idx = note_idx // len(self.notes)
        return in_oct + oct_idx * self.edo


def get_freq(note, scale, edo):
    freq = None
    if isinstance(note, numbers.Number):
        in_oct = note % len(scale)
        in_oct = scale[in_oct] / edo
        oct_idx = note // len(scale)
        note_in_linear = in_oct + oct_idx
        freq = C4_FREQ * (2 ** note_in_linear)
    return freq


def build_mos_from_edo(n, gen, edo, down=0, shift=0):
    notes = [0]
    cur = 0
    for _ in range(n - down - 1):
        cur = (cur + gen) % edo
        notes.append(cur)
    cur = 0
    for _ in range(down):
        cur = (cur - gen) % edo
        notes.append(cur)

    notes.sort()

    center = shift % len(notes)
    notes1 = [x - notes[center] for x in notes[center:]]
    notes2 = [x + edo - notes[center] for x in notes[:center]]
    return notes1 + notes2


def intervals_in_edo(sub_scale, edo, scale=None):
    if scale is None:
        scale = list(range(edo))
    sub_scale_in_linear = []
    for note in sub_scale:
        in_oct = scale[note % len(scale)]
        oct_idx = note // len(scale)
        note_in_linear = in_oct + oct_idx * edo
        sub_scale_in_linear.append(note_in_linear)
    if (sub_scale_in_linear[0] + edo) not in sub_scale_in_linear:
        sub_scale_in_linear.append(sub_scale_in_linear[0] + edo)
    res = []
    for idx in range(len(sub_scale_in_linear) - 1):
        res.append(sub_scale_in_linear[idx + 1] - sub_scale_in_linear[idx])
    return res


# NOTE: note is 0-indexed
def note_in_scale(sub_scale_orig, note, edo):
    sub_scale = copy(sub_scale_orig)
    # FIXME: refactor so that we don't need this if
    if sub_scale[-1] == sub_scale[0] + edo:
        sub_scale = sub_scale[:-1]
    in_oct = sub_scale[note % len(sub_scale)]
    oct_idx = note // len(sub_scale)
    return (in_oct + oct_idx * edo)


def triad(sub_scale_orig, degree, edo, quality='tertiary'):
    sub_scale = copy(sub_scale_orig)
    if edo in sub_scale:
        sub_scale = sub_scale[:-1]
    assert (len(sub_scale) == 7)
    if quality == 'tertiary':
        notes = [degree, degree + 2, degree + 4]
    elif quality == 'quartal':
        notes = [degree, degree + 3, degree + 6]
    chord = []
    for note in notes:
        in_oct = sub_scale[note % len(sub_scale)]
        oct_idx = note // len(sub_scale)
        chord.append(in_oct + oct_idx * edo)
    return chord
