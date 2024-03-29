import numbers


def map_note(indices, note):
    if isinstance(note, int):
        return indices[note]
    return note


def transpose(n, m):
    if isinstance(n, numbers.Number):
        return n + m
    if isinstance(n, list):
        return [transpose(note, m) for note in n]
    return n


# FIXME: what to do with defaults here? should i remove them?
def cycle(a, dup_start=False, dup_end=False):
    end = -2
    if dup_end:
        end = -2
    if dup_start:
        return a + a[end::-1]
    else:
        return a + a[end:0:-1]


# FIXME: rename to shift_left
# FIXME: rename voice
def shift(voice, s):
    return voice[s:] + voice[:s]


# FIXME: rename voice
# FIXME: what to do with defaults?
# TODO: add parameter for number of voices; right now it's only 2
def split(voice, zipped=False):
    voice1 = []
    voice2 = []
    for i, n in enumerate(voice):
        n1 = n
        n2 = '.'  # FIXME: use enum
        if i % 2:
            n1, n2 = n2, n1
        voice1.append(n1)
        voice2.append(n2)
    if zipped:
        return list(zip(voice1, voice2))
    return [voice1, voice2]


def iterate_voice_leadings(chord, transformations, permutation, sequential_units):
    # Dmitri Tymoczko iterable voice-leading, repetitions
    # https://youtu.be/n0V6FI2eB68?t=3397

    # example from Dmitri:
    # chord = "(c4 r) (d4 e4) (g4 g#4) (b4 r)"
    # transformations = "*-2, 3, 2, 1"  # TODO: why these numbers?
    # permutation = "?0, 3, 1, 2"  # TODO: why question mark, and why this permutation?
    # scale = 12  # TODO: is it used, actually?

    # at the moment we use a different convention:
    # chord: [0, 2, 7, 11]
    # transformations: [-2, 10, -2, -2]
    # permutation: [0, 2, 3, 1]

    # TODO, maybe:
    # chord = chord_str.split(' ')
    # transformations = transformations_str.split(' ')
    # transformations = [int(x) for x in transformations]
    # permutation = permutation_str.split(' ')
    # permutation = [int(x) for x in permutation]

    assert(len(chord) == len(transformations))
    assert(len(chord) == len(permutation))
    res = [chord]
    for idx in range(sequential_units - 1):
        chord = res[-1]
        # TODO: reuse transpose() here
        new_chord = tuple(chord[i] + transformations[i] for i in range(len(chord)))
        new_chord = tuple(new_chord[i] for i in permutation)
        res.append(new_chord)
    return res
