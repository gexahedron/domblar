class ChordKB():
    def __init__(self, modality, edo, intervals, annotations=['root', '3rd', '5th']):
        assert len(intervals) == len(annotations)
        self.modality = modality
        self.edo = edo
        self.intervals = intervals
        # FIXME: there's python builtin __annotations__
        # which will be confusing in the future
        self.annotations = annotations
        self.build_chords()

    def build_chords(self):
        self.chords = dict()
        for note in range(self.edo):
            self.chords[note] = frozenset(
                [(note + interval) % self.edo for interval in self.intervals])
        self.chords_set = set(self.chords.values())

    def __contains__(self, pc_set):
        return pc_set in self.chords_set

    def annotate_chord(self, chord, pc_set):
        # TODO: chord and pc_set are interrelated and shouldn't be independent variables here
        assert pc_set in self
        root = None
        # TODO: optimize this search
        for note in range(self.edo):
            if self.chords[note] == pc_set:
                root = note
                break
        assert root is not None

        positions = []
        for note in chord:
            pc1 = note % self.edo  # TODO: should be a function
            for idx, interval in enumerate(self.intervals):
                pc2 = (root + interval) % self.edo  # TODO: should be a function
                if pc1 == pc2:
                    positions.append(self.annotations[idx])
        return positions


# build once
# FIXME: better precalculate this and store this as a DB or binary file
ALL_CHORDS = []
ALL_CHORDS.append(ChordKB('maj', edo=12, intervals=[0, 4, 7]))
ALL_CHORDS.append(ChordKB('min', edo=12, intervals=[0, 3, 7]))
ALL_CHORDS.append(ChordKB('dim', edo=12, intervals=[0, 3, 6]))
ALL_CHORDS.append(ChordKB('dom7no5', edo=12, intervals=[0, 4, 10],
                          annotations=['root', '3rd', '7th']))


def annotate_chord(chord, edo):
    assert edo == 12

    # TODO: this should be a separate function
    pc_set = set()
    for note in chord:
        pc_set.add(note % edo)

    for chord_type in ALL_CHORDS:
        if pc_set in chord_type:
            positions = chord_type.annotate_chord(chord, pc_set)
            return chord_type.modality, positions
    assert False
