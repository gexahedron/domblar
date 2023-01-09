def get_grouped_rhythm(groups):
    res = []
    for group in groups:
        res += ['x'] * group + ['.']
    return res

def rhythm_to_notes(voice, note):
    res = []
    for r in voice:
        if r != '.':
            res.append(note)
        else:
            res.append('.')
    return res
