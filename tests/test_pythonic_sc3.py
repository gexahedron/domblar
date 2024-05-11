from setup import D
from domblar.edo import mos


def test_pythonic_sc3():
    d = D(context='python-sc3')
    d.set_synth(0, 'chiptune_varsaw')
    edo = 22
    scale = list(range(edo))
    cur_scale = mos(9, gen=5, edo=edo, down=0, shift=0) + [edo]
    d.play(cur_scale, scale, edo, synth_idx=[0], dur=0.3)
