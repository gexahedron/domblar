from copy import copy

from domblar.edo import note_in_scale
from domblar.music_math import OCTAVE_IN_CENTS, ratio_to_cents
from domblar.transformations import transpose


def build_scale_from_steps(steps, edo=None, start=0):
    if type(steps) is str:
        steps = [int(x) for x in steps]
    assert type(steps) is list
    scale = [start]
    for step in steps[:-1]:
        scale.append(scale[-1] + step)
    if edo is not None:
        assert scale[-1] + steps[-1] == scale[0] + edo
    return scale


def cents_to_steps(cents, edo, use_round=True):
    float_steps = cents / OCTAVE_IN_CENTS * edo
    if use_round:
        return round(float_steps)
    return int(float_steps)


def ratio_to_steps(m, n, edo, use_round=True):
    return cents_to_steps(ratio_to_cents(m, n), edo, use_round=use_round)


def acoustic_scale(edo, use_round=True):
    # 7 note scale, kind-of approximating harmonics 7:8:9:10:11:12:13
    # NOTE/maybe FIXME: for 12edo the usual acoustic scale uses int instead of round
    # and there are actually some reasons for this,
    # explained in papers by Dmitri Tymoczko or Marek Žabka
    # but if we use round - we still get acoustic scale in 12edo,
    # just with a different "root"
    # for other edo scales this is not true
    scale = []
    for i in range(7, 14):
        scale.append(ratio_to_steps(i, 7, edo, use_round=use_round))
    return scale


def build_tonic_steps(scale, voices_count, quality):
    # TODO: add support for octatonic scales
    # FIXME: in reality there should be some analysis of the scale
    # that corresponds to the quality
    # say, that we understand, that 2 steps really produce tertian quality
    # TODO: add support for higher limits (7-, 11-, 13-)
    # TODO: add support polytonality
    assert voices_count in [3, 4]
    steps = None
    if len(scale) == 7:
        if quality == 'tertian':
            steps = [2] * (voices_count - 1)
        elif quality == 'quartal':
            steps = [3] * (voices_count - 1)
        elif quality == 'add6':
            # FIXME: this is a bit ugly
            assert voices_count == 4
            steps = [2, 2, 1]
        else:
            assert quality == 'add2'
            assert voices_count == 4
            # FIXME: it's add9, really
            # also known as mu chord
            steps = [2, 2, 4]
    else:
        assert len(scale) == 10
        # TODO: add more support for decatonic scales
        # for 7-limit tetrads, the decatonic pattern is
        # X _ _ X _ _ X _ X _ X
        quality == 'tertian'
        steps = [3, 3, 2]
        steps = steps[:voices_count]
    return steps


# NOTE/FIXME: start is 1-indexed, which is incosistent with previous code
def sequence(start, ops,
             length=None, final_deg=None,  # TODO/FIXME: replace with fn to check the goal conditions
             scale=None, edo=None,
             rewrite=dict(),  # FIXME: this thing needs notation
             modulate_to=dict(),  # FIXME: this thing needs same notation
             modulate_from=dict(),  # FIXME: this thing needs same (?) notation
             cutoff=1000,  # FIXME: arbitrary number; # FIXME: bad naming?
):
    # FIXME: maybe not needed assertions
    assert scale is not None
    assert edo is not None

    # assertions
    if (rewrite is not None) or (modulate_to is not None):
        assert (scale is not None) and (edo is not None)
    # assert that exactly one of these is not None
    assert (length is not None) != (final_deg is not None)

    cur_scale = copy(scale)
    cur_deg = start
    result = []
    idx = 0
    while True:
        # check that we have achieved the goal
        if length is not None and len(result) >= length:
            break
        elif final_deg is not None and result[-1][0] == final_deg:
            break

        # FIXME: in theory we may never achieve the goal
        # so we need some emergency stop
        # what is the best strategy here?
        assert len(result) < cutoff

        # FIXME/TODO: what if we have same cur_deg
        # both in rewrite and in modulate_to or
        # both in rewrite and in modulate_from?

        # analyze cur_deg and cur_scale
        if (cur_deg in rewrite) or (cur_deg in modulate_to) or (cur_deg in modulate_from):
            # rewrite[degree] = (a, b)
            # where b is degree of cur_scale, and it becomes a root of next_scale
            # a is degree of next_scale
            # e. g., in heptatonic (7-note) scale
            # a/b ~= .../IV, if we treat cur_scale as V of next_scale
            if (cur_deg in modulate_from):
                assert cur_deg not in rewrite
                new_pair = modulate_from[cur_deg]
                new_root = note_in_scale(cur_scale, new_pair[1] - 1, edo) % edo
                new_scale = transpose(cur_scale, new_root - cur_scale[0])
                result.append((new_pair[0], new_scale, edo))
            if (cur_deg in rewrite) or (cur_deg in modulate_to):
                if cur_deg in modulate_to:
                    assert cur_deg not in rewrite
                    result.append((cur_deg, cur_scale, edo))
                    to_pair = modulate_to[cur_deg]
                else:
                    assert cur_deg not in modulate_to
                    to_pair = rewrite[cur_deg]
                new_root = note_in_scale(cur_scale, to_pair[1] - 1, edo) % edo
                cur_scale = transpose(cur_scale, new_root - cur_scale[0])
                cur_deg = to_pair[0]

        result.append((cur_deg, cur_scale, edo))

        # recalc cur_deg, and idx for next ops
        cur_deg = cur_deg + ops[idx]
        while cur_deg <= 0:
            cur_deg += len(scale)
        while cur_deg > len(scale):
            cur_deg -= len(scale)
        # FIXME: it's better to convert ops to a lazy infinite stream
        idx = (idx + 1) % len(ops)
    if length is not None:
        result = result[:length]

    return result
