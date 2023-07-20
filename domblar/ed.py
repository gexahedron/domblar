import numbers

from domblar.music_math import C4_FREQ


class ED:
    def __init__(self, steps, octave=2):
        self.steps = steps
        self.octave = octave

    def get_freq(self, note):
        freq = None
        if isinstance(note, numbers.Number):
            in_oct = note % self.steps
            in_oct = in_oct / self.steps
            oct_idx = note // self.steps
            note_in_linear = in_oct + oct_idx
            freq = C4_FREQ * (self.octave ** note_in_linear)
        return freq


class Scale():
    def __init__(self, notes, ed: ED) -> None:
        self.notes = notes
        self.ed = ed

    def __getitem__(self, note_idx):
        if not isinstance(note_idx, numbers.Number):
            return note_idx
        in_oct = self.notes[note_idx % len(self.notes)]
        oct_idx = note_idx // len(self.notes)
        return in_oct + oct_idx * self.ed.steps

    def get_freq(self, note):
        return self.ed.get_freq(self[note])

    def __add__(self, shift):
        return Scale([n + shift for n in self.notes], self.ed)

    def __iadd__(self, shift):
        self.notes = [n + shift for n in self.notes]
        return self

    def __repr__(self):
        return f'Scale({self.ed.steps}ed{self.ed.octave}, {self.notes})'

    def __len__(self):
        return len(self.notes)


def mos(steps, gen, ed: ED):
    chroma = ed.steps
    notes = [0]  # FIXME: move to parameters as root
    cur = 0
    for _ in range(steps - 1):
        cur = (cur + gen) % chroma
        notes.append(cur)
    notes.sort()
    # FIXME: add check that we have only 2 step sizes
    return Scale(notes, ed)
