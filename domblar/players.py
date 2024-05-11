import time

from domblar.edo import triad, get_freq
from domblar.sc3.osc3vst.client import SC3Client


def play_non_edo(chords, client: SC3Client,
         dur=0.25, sus=None, delay=None, synth_idx=[0], rep=1,
         muls=[], amps=[], voice_amps=[]):
    if chords and muls:
        assert len(chords) == len(muls)
    if chords and amps:
        assert len(chords) == len(amps)
    if isinstance(rep, list):
        assert len(synth_idx) == len(rep)
    else:
        rep = [rep] * len(synth_idx)
    last_reps = [0] * len(synth_idx)
    for chord_idx, chord in enumerate(chords):
        if isinstance(chord, tuple):
            chord = list(chord)
        elif not isinstance(chord, list):
            chord = [chord]
        for note_idx, freq in enumerate(chord):
            send_note_dur = dur
            if sus:
                send_note_dur = sus
            if muls:
                send_note_dur *= muls[chord_idx]
            amp = 1.0
            if amps:
                amp = amps[chord_idx]
            if voice_amps:
                amp *= voice_amps[note_idx]
            timetag = time.time()
            client.send_note(
                synth_idx[note_idx] + last_reps[note_idx],
                freq=freq, dur=send_note_dur, amp=amp,
                timetag=timetag, channel=0)  # TODO: for MPE with channels use channel=note_idx
            last_reps[note_idx] = (last_reps[note_idx] + 1) % rep[note_idx]
            if delay:
                time.sleep(delay)
        sleep_dur = dur
        if muls:
            sleep_dur *= muls[chord_idx]
        time.sleep(sleep_dur)


# FIXME: remove this function; duplicates play_non_edo
def vst_play(chords, scale, edo, client: SC3Client,
             dur=0.25, sus=None, delay=None, synth_idx=[0], rep=1,
             muls=[], amps=[], voice_amps=[]):
    if chords and muls:
        assert len(chords) == len(muls)
    if chords and amps:
        assert len(chords) == len(amps)
    if isinstance(rep, list):
        assert len(synth_idx) == len(rep)
    else:
        rep = [rep] * len(synth_idx)
    last_reps = [0] * len(synth_idx)
    for chord_idx, chord in enumerate(chords):
        if isinstance(chord, tuple):
            chord = list(chord)
        elif not isinstance(chord, list):
            chord = [chord]
        for note_idx, note in enumerate(chord):
            freq = get_freq(note, scale, edo)
            send_note_dur = dur
            if sus:
                send_note_dur = sus
            if muls:
                send_note_dur *= muls[chord_idx]
            amp = 1.0
            if amps:
                amp = amps[chord_idx]
            if voice_amps:
                amp *= voice_amps[note_idx]
            timetag = time.time()
            client.send_note(
                synth_idx[note_idx] + last_reps[note_idx],
                freq=freq, dur=send_note_dur, amp=amp,
                timetag=timetag, channel=0)  # TODO: for MPE with channels use channel=note_idx
            last_reps[note_idx] = (last_reps[note_idx] + 1) % rep[note_idx]
            if delay:
                time.sleep(delay)
        sleep_dur = dur
        if muls:
            sleep_dur *= muls[chord_idx]
        time.sleep(sleep_dur)


def sc3_play(chords, scale, edo, synths,
             dur=0.25, sus=None, delay=None, synth_idx=[0], rep=1,
             muls=[], amps=[], voice_amps=[]):
    # FIXME: mostly duplicates vst_play
    if chords and muls:
        assert len(chords) == len(muls)
    if chords and amps:
        assert len(chords) == len(amps)
    if isinstance(rep, list):
        assert len(synth_idx) == len(rep)
    else:
        rep = [rep] * len(synth_idx)
    last_reps = [0] * len(synth_idx)
    for chord_idx, chord in enumerate(chords):
        if isinstance(chord, tuple):
            chord = list(chord)
        elif not isinstance(chord, list):
            chord = [chord]
        for note_idx, note in enumerate(chord):
            freq = get_freq(note, scale, edo)
            send_note_dur = dur
            if sus:
                send_note_dur = sus
            if muls:
                send_note_dur *= muls[chord_idx]
            amp = 1.0
            if amps:
                amp = amps[chord_idx]
            if voice_amps:
                amp *= voice_amps[note_idx]
            synths[note_idx](0, freq,
                  dur=send_note_dur,
                  pan=0,
                #   pan=pan,  # FIXME
                  add_action='head',
                  amp=amp)
            last_reps[note_idx] = (last_reps[note_idx] + 1) % rep[note_idx]
            if delay:
                time.sleep(delay)
        sleep_dur = dur
        if muls:
            sleep_dur *= muls[chord_idx]
        time.sleep(sleep_dur)


# def sc3_play(notes,
#          scale,
#          edo=12,  # FIXME
#          synth=chiptune_varsaw,
#          amp=1,
#          pan=0.0,
#          dur=1.0,  # FIXME: doesn't work in most synths
#          base_freq=261.6255653006,
#          debug=False):
#     debug_output = []
#     for i, n_tuple in enumerate(notes):
#         # FIXME: ugly
#         if n_tuple == '.':
#             continue
#         if isinstance(n_tuple, int):
#             n_tuple = (n_tuple,)
#         for n in n_tuple:
#             # TODO: use function
#             edo_n = scale[n % len(scale)] + edo * (n // len(scale))
#             debug_output.append(edo_n)
#             freq = base_freq * (2 ** (edo_n / edo))
#             synth(0, freq,
#                   dur=dur*1.1,  # FIXME
#                   pan=pan,
#                   add_action='head',
#                   amp=max(0.1, 0.4 - freq / 440 / 4) * amp)  # FIXME
#         time.sleep(dur)
#     if debug:
#         print('notes:', debug_output)


# TODO: currently unused
def play_voice(notes, timbre, scale, edo, client, dur=0.25, sus=None):
    if not isinstance(notes, list):
        notes = [notes]
    for note in notes:
        freq = get_freq(note, scale, edo)
        send_note_dur = dur
        if sus:
            send_note_dur = sus
        timetag = time.time()
        client.send_note(timbre, freq=freq, dur=send_note_dur, timetag=timetag)
        time.sleep(dur)


# TODO: currently unused
def play_voices(voices, timbres, scale, edo, client, dur=0.25, sus=None):
    # check preconditions
    for v in voices:
        assert (len(v) == len(voices[0]))
    assert (len(voices) == len(timbres))

    for note_idx in range(len(voices[0])):
        for v_idx, v in enumerate(voices):
            notes = v[note_idx]
            if not isinstance(notes, list):
                notes = [notes]
            for chord_note_idx, note in enumerate(notes):
                freq = get_freq(note, scale, edo)
                send_note_dur = dur
                if sus:
                    send_note_dur = sus
                timetag = time.time()
                client.send_note(
                    timbres[v_idx],
                    freq=freq, dur=send_note_dur * 2, timetag=timetag, channel=chord_note_idx)
        time.sleep(dur)


# TODO: currently unused
def play_triads(sub_scale, degrees, dur, scale, edo, client):
    chords = []
    for deg in degrees:
        chords.append(triad(sub_scale, deg, edo))
    play(chords, scale, edo, client, dur=dur)
