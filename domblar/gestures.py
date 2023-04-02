# FIXME: it's very similar to parse_voicing
# ideally i think it should be a single function for both
def parse_gesture(gesture):
    # NOTE: i assume here that gesture output is melody
    # TODO: add support for chords (won't work for Dexed; but for other MPE synths it's good)
    result = []
    if type(gesture) is str:
        gesture = gesture.strip().split(' ')

    assert type(gesture) is list

    for note_info in gesture:
        rep = 1
        if type(note_info) is str:
            if '*' in note_info:
                note_info = note_info.split('*')
                assert len(note_info) == 2
                rep = int(note_info[-1])
                note_info = note_info[0]
            dur = 1
            if ':' in note_info:
                note_info = note_info.split(':')
                assert len(note_info) == 2
                dur = int(note_info[-1])
                note_info = note_info[0]
            # FIXME: code duplication
            octave = 0
            octave -= note_info.count('_')
            note_info = note_info.replace('_', '')
            octave += note_info.count('^')
            note_info = note_info.replace('^', '')
            note_idx = note_info
            # FIXME: explicit dot
            if note_idx != '.':
                note_idx = int(note_idx)
        # FIXME: code here should be mostly deprecated
        elif type(note_info) is dict:
            pitch_info = list(note_info.keys())[0]
            dur = list(note_info.values())[0]
            if type(pitch_info) is tuple:
                note_idx, octave = pitch_info
            else:
                note_idx = pitch_info
                octave = 0
        else:
            pitch_info = note_info
            dur = 1
            # FIXME: code duplication
            if type(pitch_info) is tuple:
                note_idx, octave = pitch_info
            else:
                note_idx = pitch_info
                octave = 0

        result.extend([(note_idx, octave, dur)] * rep)

    return result


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
