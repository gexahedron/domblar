from sc3.all import *
import random


@synthdef
def bplay(out = 0, buf = 0, rate = 1, amp = 0.5, pan = 0, pos = 0, rel=15):
    sig = PlayBuf.ar(2, buf, BufRateScale.ir(buf) * rate,
                            1, BufDur.kr(buf) * pos * 48000,
                            done_action=2)
    env = EnvGen.ar(Env.linen(0.0, rel, 0), done_action=2)
    sig = sig * env
    sig = sig * amp
    sig = Pan2.ar(sig, pan)
    sig = Mix.ar(sig)
    Out.ar(out, sig)

@synthdef
def chiptune_varsaw(out=0, freq=440, amp=0.5, dur=1, env_nom=0, decay=0.1, pan=0, gate=1, hpf=100, lpf=10000):
    length = dur * 1.5
    env_mult = 0.6
    env = env_nom * EnvGen(Env([0.01, 0.5, 0.01],
                               [0.2 * env_mult, length * env_mult]), done_action=2) +\
          (1 - env_nom) * EnvGen(Env([0.001, 1, decay, 0.001],
                                     [0.02 * env_mult, (length + 0.2 - 0.04) * env_mult, 0.02 * env_mult],
                                     'exponential'), done_action=2)
    lag = 0.05
    sig = Lag.kr(freq, lag)
    sig = [VarSaw.ar(sig * num, random.random()) / (num ** 3) for num in range(1, 4)]
    sig = sig * amp
    sig = HPF.ar(sig, hpf)
    sig = LPF.ar(sig, lpf)
    sig = Pan2.ar(sig, pan, 1) * env
    sig = Mix(sig)
    Out.ar(out, sig)

@synthdef
def chiptune_triangle(out=0, freq=440, amp=0.5, dur=1, decay=0.1, pan=0, gate=1, hpf=100, lpf=10000,
                      atk = 0.01, dec = 0.075, sus = 1, rel = 1, hold = 0.5):
    fenv = freq
    sig = (LFTri.ar(fenv, random.random()) * 0.5 + 1)#.round(1 / 15)
    env = EnvGen.kr(Env([0, 1, 1, 0], [atk, dec, hold, rel]), done_action=2)
    sig = Pan2.ar(sig, pan, 1)
    sig = sig * amp * env
    Out.ar(0, sig)

@synthdef
def fm_2op_sinfb(out=0, freq=440,
                 m_ratio=1, c_ratio=1,
                 index=0, i_scale=1, c_atk=4, c_rel=-4,
                 amp=0.2, atk=0.01, rel=1, pan=0,
                 fx=0, fxsend=-25,
                 dur=1, decay=0.1, gate=1, hpf=100, lpf=10000):
    i_env = EnvGen.kr(Env([index, index * i_scale, index], [atk, rel], [c_atk, c_rel]), done_action=2)
    env = EnvGen.kr(Env.perc(atk, rel, curve=[c_atk, c_rel]), done_action=2)
    mod = SinOsc.ar(freq * m_ratio) * (freq * m_ratio * i_env)
    car = SinOscFB.ar(freq * c_ratio + mod) * env * amp
    car = Pan2.ar(car, pan)
    Out.ar(out, car)

@synthdef
def fm_2op_saw(out=0, freq=440,
               m_ratio=1, c_ratio=1,
               index=0, i_scale=1, c_atk=4, c_rel=-4,
               amp=0.2, atk=0.01, rel=1, pan=0,
               fx=0, fxsend=-25,
               dur=1, decay=0.1, gate=1, hpf=100, lpf=10000):
    i_env = EnvGen.kr(Env([index, index * i_scale, index], [atk, rel], [c_atk, c_rel]), done_action=2)
    env = EnvGen.kr(Env.perc(atk, rel, curve=[c_atk, c_rel]), done_action=2)
    mod = SinOsc.ar(freq * m_ratio) * (freq * m_ratio * i_env)
    car = LFSaw.ar(freq * c_ratio + mod) * env * amp
    car = Pan2.ar(car, pan)
    Out.ar(out, car)

@synthdef
def fm_2op_pulse(out=0, freq=440,
                 m_ratio=1, c_ratio=1,
                 index=1, i_scale=5, c_atk=4, c_rel=-4,
                 amp=0.2, atk=0.01, rel=1, pan=0,
                 fx=0, fxsend=-25,
                 dur=1, decay=0.1, gate=1, hpf=100, lpf=10000):
    i_env = EnvGen.kr(Env([index, index * i_scale, index], [atk, rel], [c_atk, c_rel]), done_action=2)
    env = EnvGen.kr(Env.perc(atk, rel, curve=[c_atk, c_rel]), done_action=2)
    mod = SinOsc.ar(freq * m_ratio) * (freq * m_ratio * i_env)
    car = LFPulse.ar(freq * c_ratio + mod) * env * amp
    car = Pan2.ar(car, pan)
    Out.ar(out, car)

# @synthdef
# def bell(out=0, freq=440, pan=0,
#          t60=1, pitchy=1, amp=0.25, gate=1):
#     exciter = WhiteNoise.ar() * EnvGen.ar(Env.perc(0.001, 0.05), gate) * 0.25
#     sig = Klank.ar(
#         (
#             [1, 2, 2.803, 3.871, 5.074, 7.81, 10.948, 14.421],   # freqs
#             [1, 0.044, 0.891, 0.0891, 0.794, 0.1, 0.281, 0.079], # amplitudes
#             [1, 0.205, 1, 0.196, 0.339, 0.047, 0.058, 0.047] * t60 # ring times
#         ),
#         exciter,
#         freq_scale=freq * pitchy)
#     sig = FreeVerb.ar(sig) * amp
# #     DetectSilence.ar(sig, 0.001, 0.5, done_action=2)
#     sig = Pan2.ar(sig, pan)
#     Out.ar(out, sig)

# @synthdef
# def pluck(out=0, freq = 440, amp = 0.5, decay = 5, coef = 0.1, pan=0):
#     env = EnvGen.kr(Env.linen(0, decay, 0), done_action=2)
#     sig = Pluck.ar(
#         input=WhiteNoise.ar() * amp,
#         trig=Impulse.kr(0),
#         maxdelaytime=0.1,
#         delaytime=1.0 / freq,
#         decaytime=decay,
#         coef=coef)
#     sig = Pan2.ar(sig, pan)
#     Out.ar(out, sig)
    
@synthdef
def hihat(out = 0, amp = 0.5, att = 0.01, rel = 0.2, ffreq = 6000, pan = 0):
    env = EnvGen.kr(Env.perc(att, rel, amp), done_action=2)
    snd = WhiteNoise.ar()
    snd = HPF.ar(input=snd, freq=ffreq) * env
    Out.ar(out, Pan2.ar(snd, pan))

@synthdef
def snare(out = 0, amp = 0.1, sinfreq = 180, att = 0.01, rel = 0.2, ffreq = 2000, pan = 0):
    env = EnvGen.kr(Env.perc(att, rel, amp), done_action=2)
    snd1 = HPF.ar(
        input=WhiteNoise.ar(),
        freq=ffreq) * env
    snd2 = SinOsc.ar(freq=sinfreq) * env
    sum = snd1 + snd2
    Out.ar(out, Pan2.ar(sum, pan))

@synthdef
def kick(out = 0, amp = 0.3, sinfreq = 60, glissf = 0.9, att = 0.01, rel = 0.45, pan = 0):
    env = EnvGen.kr(Env.perc(att, rel, amp), done_action=2)
    ramp = XLine.kr(
        start=sinfreq,
        end=sinfreq * glissf,
        dur=rel)
    snd = SinOsc.ar(freq=ramp) * env
    snd = Pan2.ar(snd, pan)
    Out.ar(out, snd)

@synthdef
def kalimba(out = 0, freq = 440, amp = 0.1, mix = 0.1, pan=0):
    snd = SinOsc.ar(freq) * EnvGen.ar(Env.perc(0.03, Rand(3.0, 4.0), 1, -7), done_action=2)
    snd = HPF.ar(LPF.ar(snd, 380), 120)
    click = DynKlank.ar(
        (
            [240 * ExpRand(0.97, 1.02), 2020 * ExpRand(0.97, 1.02), 3151 * ExpRand(0.97, 1.02)],
            [0.354, 1, 0.562],
            [0.8, 0.07, 0.08],
        ), BPF.ar(PinkNoise.ar(), 6500, 0.1) * EnvGen.ar(Env.perc(0.001, 0.01))) * 0.1
    snd = (snd * mix) + (click * (1 - mix))
    snd = Pan2.ar(snd, pan, 1) * amp
    Out.ar(out, snd)
