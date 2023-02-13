def apply_gestures(chords, gestures, edo):
    result = []
    for idx, chord in enumerate(chords):
        motif = []
        for pos in gestures[idx]:
            # FIXME: i assume here that gesture output is melody
            # but it could also be chords
            if type(pos) is int:
                note_idx = pos
                octave = 0
            else:
                note_idx, octave = pos
            note = chord[note_idx] + octave * edo
            motif.append(note)
        result.extend(motif)
    return result
