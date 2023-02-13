import time

from domblar.edo import triad, get_freq
from domblar.sc3.client import SC3Client


def play(chords, scale, edo, client: SC3Client,
         dur=0.25, sus=None, delay=None, synth_idx=[0], rep=1,
         muls=[], amps=[], voice_amps=[]):
    if chords and muls:
        assert len(chords) == len(muls)
    if chords and amps:
        assert len(chords) == len(amps)
    if type(rep) is list:
        assert len(synth_idx) == len(rep)
    else:
        rep = [rep] * len(synth_idx)
    last_reps = [0] * len(synth_idx)
    for chord_idx, chord in enumerate(chords):
        if type(chord) is tuple:
            chord = list(chord)
        elif type(chord) is not list:
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
                timetag=timetag, channel=0) # TODO: for MPE with channels use channel=note_idx
            last_reps[note_idx] = (last_reps[note_idx] + 1) % rep[note_idx]
            if delay:
                time.sleep(delay)
        sleep_dur = dur
        if muls:
            sleep_dur *= muls[chord_idx]
        time.sleep(sleep_dur)


# TODO: currently unused
def play_voice(notes, timbre, scale, edo, client, dur=0.25, sus=None, delay=None):
    if type(notes) is not list:
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
        chords.append(triad(sub_scale, deg))
    play(chords, scale, edo, client, dur=dur)
