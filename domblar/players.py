import time

from domblar.edo import triad, get_freq


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


def play(chords, scale, edo, client, dur=0.25, sus=None, delay=None, synth_idx=0):
    for chord_idx, chord in enumerate(chords):
        if type(chord) is not list:
            chord = [chord]
        for note_idx, note in enumerate(chord):
            freq = get_freq(note, scale, edo)
            send_note_dur = dur
            if sus:
                send_note_dur = sus
            timetag = time.time()
            client.send_note(
                synth_idx,
                freq=freq, dur=send_note_dur, timetag=timetag, channel=note_idx)
            if delay:
                time.sleep(delay)
        time.sleep(dur)


def play_triads(sub_scale, degrees, dur, scale, edo, client):
    chords = []
    for deg in degrees:
        chords.append(triad(sub_scale, deg))
    play(chords, scale, edo, client, dur=dur)
