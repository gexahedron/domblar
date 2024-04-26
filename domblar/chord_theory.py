from copy import copy, deepcopy
import random

from domblar.edo import note_in_scale
from domblar.tonal_theory import sequence, build_tonic_steps
from domblar.gestures import parse_gesture


# FIXME: move this somewhere else?
# FIXME: what is the purpose of this class? it shouldn't be just a dump
class Config():
    def __init__(self):
        self.synths = None
        self.dur = None
        self.sus = None
        self.voicing = None
        self.quality = None  # FIXME: should be more flexible, less global
        self.gestures = None  # FIXME: should be more flexible, less global
        self.edo = None  # FIXME: remove
        self.once = False  # FIXME: default value should be None


class Configurable():
    def __init__(self):
        self.config = Config()

    def synths(self, synth_list):
        self.config.synths = synth_list
        return self

    def dur(self, dur_val):
        self.config.dur = dur_val
        return self

    def sus(self, sus_val):
        self.config.sus = sus_val
        return self

    def voicing(self, voicing_list):
        self.config.voicing = voicing_list
        return self

    def q(self, quality_str):
        self.config.quality = quality_str
        return self

    def g(self, gestures_list):
        self.config.gestures = gestures_list
        return self

    def once(self, once_bool=True):
        self.config.once = once_bool
        return self

    def set_config(self, config):
        self.config = config
        return self

# FIXME:
class Chord():
    def __init__(self):
        pass


class Chords(Configurable):
    def __init__(self):  # TODO? add context
        super().__init__()
        self.progression = None
        self.chords = []

    def from_chords(self, chords):
        self.chords = chords
        return self

    def seq(self, start, ops, **kwargs):
        # FIXME: adhoc
        # TODO: add support for mods
        self.config.edo = kwargs['edo']
        self.progression = sequence(start, ops, **kwargs)
        return self

    def evaluate(self):
        assert self.progression is not None
        self.chords = progress(self.progression,
             voices_default=len(self.config.synths),  # FIXME: ugly
             voicing=self.config.voicing,
             # FIXME: start_from parameter is in conflict with voicing
             # FIXME: it is used right now exclusively to start from last_chord
             # start_from=None,
             quality=self.config.quality,
             # FIXME: used in 3rd part
             #  always_jump_on=[],
             )
        return self

    def __str__(self):
        self.evaluate()
        return str(self.chords)

    def __repr__(self):
        self.evaluate()
        return self.chords.__repr__()


class Voices(Configurable):
    def __init__(self):
        super().__init__()
        self.events = []

    def from_list(self, voices):
        self.events = voices
        return self


def chords_to_voices(chords, gestures=None, edo=None, durs=None):
    if type(chords) is list:
        chords = Chords().from_chords(chords)
    if gestures is None and chords.config.gestures is not None:  # FIXME: what if we have both?
        gestures = chords.config.gestures
        edo = chords.config.edo

    if gestures is not None:
        assert edo is not None
        gestures = [parse_gesture(gesture) for gesture in gestures]
        result = [[] for _ in range(len(gestures))]
    else:
        result = [[] for _ in range(len(chords.chords[0]))]

    if durs is not None:
        assert len(durs) == len(chords.chords)
    else:
        durs = [1] * len(chords.chords)

    for chord_idx, chord in enumerate(chords.chords):
        if gestures is not None:
            for voice_idx, gesture in enumerate(gestures):
                motif = []
                for note_idx, octave, dur in gesture:
                    if type(note_idx) is int:
                        note = chord[note_idx] + octave * edo
                    else:
                        note = note_idx
                    motif.append((note, dur * durs[chord_idx]))
                result[voice_idx].extend(motif)
        else:
            for voice_idx in range(len(chord)):
                result[voice_idx].append((chord[voice_idx], durs[chord_idx]))
    # FIXME:
    # return result
    return Voices().from_list(result).set_config(chords.config)


def parse_voicing(voicing):
    # TODO/FIXME: create nice syntax for voicings
    ops = dict()
    # FIXME: find a better name
    chunks = voicing.strip().split(' ')
    for chunk in chunks:
        octave = 0
        octave -= chunk.count('_')
        chunk = chunk.replace('_', '')
        octave += chunk.count('^')
        chunk = chunk.replace('^', '')
        ops[int(chunk)] = octave
    return ops


def apply_voicing(chord, voicing, octave):
    if voicing is None:
        return chord
    voicing_ops = parse_voicing(voicing)
    # FIXME: copy chord
    for voice_idx in voicing_ops:
        chord[voice_idx] += octave * voicing_ops[voice_idx]
    return chord


# FIXME: rename voices to voices_count
# FIXME: hide defaults for quality and voices
def chord_in_scale(scale, degree, voices=3, quality='tertian'):
    # FIXME: this approach won't work in non-fifth based edos
    # and scales with length not equal to 7 or 10
    steps = build_tonic_steps(scale, voices, quality)

    assert 0 < degree <= len(scale)
    root = degree - 1

    chord = []
    sum_step = 0
    for i in range(voices):
        chord.append(root + sum_step)
        if i < voices - 1:
            sum_step += steps[i]
    return chord


def chord_in_edo(scale, edo, degree, voices=3, quality='tertian', voicing=None):
    chord = chord_in_scale(scale, degree=degree, voices=voices, quality=quality)
    if voices == 3:
        chord.append(chord[0] + len(scale))
    # FIXME: hacky default voicing, remove it
    if voicing is None:
        voicing = '0_'
    chord = apply_voicing(chord, voicing, octave=len(scale))
    # TODO: add option to sort notes, so that bass is note 0
    # NOTE/maybe FIXME: we switch here from scale to full edo, maybe there's a better approach
    return [note_in_scale(scale, n, edo) for n in chord]


# FIXME: inconsistent naming
# "in_edo" in "chord_in_edo" means something different
# than "in_edo" in "cadence_in_edo"
def cadence_in_edo(chord, new_chord_shape, edo, new_root=None, jump=False):
    # FIXME: should be a function/Chord() method
    new_pc_set = set()
    new_pc_set = frozenset([n % edo for n in new_chord_shape])
    if new_root is None:
        new_root = new_chord_shape[0] % edo

    # FIXME: right now we keep only 1 candidate for each possible pc set
    # but in the future we should keep a bit more promising candidates
    possible_new_sub_chords = dict()

    # FIXME: quartal chords don't have roots
    # TODO: for each voice we should respect voice range restrictions

    # FIXME: we also implicitly assume here that bass in voice 0
    # FIXME: maybe move this variable to optional parameters
    base_is_root = jump
    first_non_jump_note = 0
    # NOTE: this tolerance is in edo steps, not in scale steps
    # smooth_leading_tolerance_in_steps = round(edo / 3)  # FIXME: heuristic
    smooth_leading_tolerance_in_steps = round(edo * 5 / 12)  # other probable heuristic
    if base_is_root:
        first_non_jump_note = 1
        # TODO: inefficient
        for diff in range(smooth_leading_tolerance_in_steps + 1):
            # FIXME: we implicitly assume here that
            # we can have only 1 candidate within the tolerance
            # although with tolerance < edo/2 this should be always true
            signs = [-1, 1]
            if diff == 0:
                signs = [-1]
            for sign in signs:
                note = chord[0] + diff * sign
                pc = note % edo
                if pc == new_root:
                    assert (not possible_new_sub_chords)
                    # FIXME: ad hoc data structure
                    # tuple (chord, edo-step penalty)
                    possible_new_sub_chords[frozenset([pc])] = ([note], 0)
            if possible_new_sub_chords:
                break
        if not possible_new_sub_chords:
            candidates = []
            for sign in [-1, 1]:  # in current implementation the order here doesn't matter
                # TODO: inefficient, should be O(1)
                for diff in range(smooth_leading_tolerance_in_steps + 1, edo):
                    note = chord[0] + diff * sign
                    pc = note % edo
                    if pc == new_root:
                        candidates.append((note, pc))
                        break
            assert len(candidates) == 2
            note, pc = random.choice(candidates)
            possible_new_sub_chords[frozenset([pc])] = ([note], 0)
    else:
        possible_new_sub_chords[frozenset()] = ([], 0)

    # now find some voice-leading for "non-bass" notes
    for i in range(first_non_jump_note, len(chord)):
        possible_new_bigger_sub_chords = dict()
        found = False  # NOTE: actually it's not needed, we will always find something
        # but i will keep it for now because the code is complicated
        for diff in range(smooth_leading_tolerance_in_steps + 1):  # FIXME: probably inefficient for large edos
            signs = random.choice([[-1, 1], [1, -1]])  # FIXME: hack, to alleviate the problem with equal penalty
            if diff == 0:
                signs = [1]
            for sign in signs:
                note = chord[i] + diff * sign
                # FIXME: should be a function/Chord() method
                pc = note % edo
                if pc in new_pc_set:
                    found = True
                    penalty = diff
                    # FIXME: confusing naming
                    for prev_pc_set in possible_new_sub_chords:
                        prev_chord, prev_penalty = possible_new_sub_chords[prev_pc_set]
                        bigger_pc_set = frozenset(list(prev_pc_set) + [pc])
                        bigger_chord = copy(prev_chord) + [note]
                        bigger_penalty = penalty + prev_penalty
                        prev_bigger_penalty = None
                        if bigger_pc_set in possible_new_bigger_sub_chords:
                            prev_bigger_penalty = possible_new_bigger_sub_chords[bigger_pc_set][1]
                        if (prev_bigger_penalty is None) or (prev_bigger_penalty > bigger_penalty):
                            possible_new_bigger_sub_chords[bigger_pc_set] = (bigger_chord, bigger_penalty)
                        # FIXME: we could have an ambiguity here,
                        # if penalties are the same
        assert found
        possible_new_sub_chords = deepcopy(possible_new_bigger_sub_chords)

    # TODO: choose best chord
    if new_pc_set in possible_new_sub_chords:
        return possible_new_sub_chords[new_pc_set][0]
    new_chord = None
    best_pc_set_size = 0
    best_penalty = None
    for pc_set in possible_new_sub_chords:
        if len(pc_set) >= best_pc_set_size:
            candidate_chord, candidate_penalty = possible_new_sub_chords[pc_set]
            if (len(pc_set) > best_pc_set_size) or candidate_penalty >= best_penalty:
                # FIXME: we could have an ambiguity here,
                # if penalties are the same
                new_chord = candidate_chord
                best_penalty = candidate_penalty
                best_pc_set_size = len(pc_set)
    assert new_chord is not None

    # FIXME: with the current approach we can have some "problems",
    # e. g.:
    # - merging of 2 voices into the same note (should be easy to fix)
    # - voice crossings (should be easy to fix)
    # - not getting the full chord quality/modality (to fix this we would need to split notes)
    # although sometimes this is actually a desired behavior
    return new_chord


def cadence(chord, scale, edo, degree,
            voices=3, quality='tertian', jump=False):
    new_chord_shape = chord_in_scale(scale, degree=degree, voices=voices, quality=quality)
    # TODO: we switch here from scale to full edo, maybe there's a better approach
    new_chord_shape = [note_in_scale(scale, n, edo) for n in new_chord_shape]
    new_root = note_in_scale(scale, degree - 1, edo) % edo
    return cadence_in_edo(chord, new_chord_shape, edo, new_root=new_root, jump=jump)


# FIXME: hide default value for voices_default
# FIXME: code duplicate
def progress(degrees, voices_default=3,
             voicing=None, start_from=None,  # FIXME: these 2 parameters are conflicting
             quality=None,
             always_jump_on=[],
):
    default_quality = quality
    chords = []
    for info, cur_scale, edo in degrees:
        # FIXME: this is ugly, need a parser
        if type(info) is tuple:
            degree, voices = info
        else:
            degree = info
            voices = voices_default

        jump = False
        quality = default_quality
        if quality is None:
            quality = 'tertian'

        # parse degree and other properties
        if type(degree) is str:
            # FIXME: this is ugly, need a parser
            if 'q' in degree:
                quality = 'quartal'
                degree = degree.replace('q', '')
            elif 'add6' in degree:
                quality = 'add6'
                degree = degree.replace('add6', '')
            elif 'add2' in degree:
                quality = 'add2'
                degree = degree.replace('add2', '')
            if 'j' in degree:
                jump = True
                degree = degree.replace('j', '')
            if 'v4' in degree:
                voices = 4
                degree = degree.replace('v4', '')
            if 'v3' in degree:
                voices = 3
                degree = degree.replace('v3', '')
            degree = int(degree)

        if degree in always_jump_on:
            jump = True

        if not chords:
            if start_from is None:
                chords.append(chord_in_edo(scale=cur_scale, edo=edo,
                                           degree=degree, voices=voices,
                                           quality=quality, voicing=voicing))
            else:
                chords.append(cadence(start_from, scale=cur_scale, edo=edo,
                                      degree=degree, voices=voices,
                                      jump=jump, quality=quality))
        else:
            chords.append(cadence(chords[-1], scale=cur_scale, edo=edo,
                                  degree=degree, voices=voices,
                                  jump=jump, quality=quality))
    return chords


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
            pc1 = note % self.edo  # FIXME: should be a function/Chord() method
            for idx, interval in enumerate(self.intervals):
                pc2 = (root + interval) % self.edo  # FIXME: should be a function/Chord() method
                if pc1 == pc2:
                    positions.append(self.annotations[idx])
        return positions


# build once
# FIXME: better precalculate this and store this as a DB or binary file
# TODO: use sqlite
ALL_CHORDS = []
ALL_CHORDS.append(ChordKB('maj', edo=12, intervals=[0, 4, 7]))
ALL_CHORDS.append(ChordKB('min', edo=12, intervals=[0, 3, 7]))
ALL_CHORDS.append(ChordKB('dim', edo=12, intervals=[0, 3, 6]))
ALL_CHORDS.append(ChordKB('dom7no5', edo=12, intervals=[0, 4, 10],
                          annotations=['root', '3rd', '7th']))


def annotate_chord(chord, edo):
    assert edo == 12

    # FIXME: should be a function/Chord() method
    pc_set = set()
    for note in chord:
        pc_set.add(note % edo)

    for chord_type in ALL_CHORDS:
        if pc_set in chord_type:
            positions = chord_type.annotate_chord(chord, pc_set)
            return chord_type.modality, positions
    assert False
