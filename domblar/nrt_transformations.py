from domblar.chord_theory import annotate_chord


# code for Neo-Riemannian theory transformations / voice-leadings
# at the moment it only works for 12edo

# TODO: would be nice to organize this code better,
# too many functions with non-obvious names

def generic_chord_transform(chord, edo, shifts):
    assert edo == 12
    modality, annotated_chord = annotate_chord(chord, edo)
    assert modality in shifts
    new_chord = []
    for idx, note in enumerate(chord):
        shift = 0
        if annotated_chord[idx] in shifts[modality]:
            shift = shifts[modality][annotated_chord[idx]]
        new_chord.append(note + shift)
    if 'expect' in shifts[modality]:
        new_modality, _ = annotate_chord(new_chord, edo)
        assert new_modality == shifts[modality]['expect']
    return new_chord


# FIXME: calculating all these shifts is fragile, error-prone
# we need to find a better way to code them
# maybe through some kind of discovery process
# and while building knowledge base
# although we also need to attach names to this operations
def p(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'maj': {'3rd': -1, 'expect': 'min'},
        'min': {'3rd': 1, 'expect': 'maj'}
    })

def l(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'maj': {'root': -1, 'expect': 'min'},
        'min': {'5th': 1, 'expect': 'maj'}
    })

def r(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'maj': {'5th': 2, 'expect': 'min'},
        'min': {'root': -2, 'expect': 'maj'}
    })

# this name is from David Kopp's classification
def m(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'maj': {'3rd': -1, '5th': 1, 'expect': 'maj'},
        'min': {'root': -1, '5th': 1, 'expect': 'min'},
    })

def slide(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'maj': {'root': 1, '5th': 1, 'expect': 'min'},
        'min': {'root': -1, '5th': -1, 'expect': 'maj'},
    })

# TODO: what is this transformation? too much movement
def maj_to_dim_wat(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'maj': {'3rd': 2, '5th': 2, 'expect': 'dim'},
    })

# unused, but it's the obvious one
def min_to_dim1(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'min': {'5th': -1, 'expect': 'dim'}
    })

def min_to_dim2(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'min': {'root': -2, '3rd': 1, 'expect': 'dim'}
    })

def min_to_dim3(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'min': {'5th': 2, 'expect': 'dim'}
    })

def dim_to_dom7no5(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'dim': {'root': 1, '5th': 1, 'expect': 'dom7no5'}  # actually, SLIDE for maj is same movement
    })

def min_to_dom7no5(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'min': {'3rd': -1, '5th': -1, 'expect': 'dom7no5'}
    })

def dom7no5_to_dim(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'dom7no5': {'3rd': -1, '7th': -1, 'expect': 'dim'}  # same as min_to_dom7no5
    })

def f(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'maj': {'3rd': 1, '5th': 1, 'expect': 'min'},
        'min': {'3rd': 2, '5th': 2, 'expect': 'maj'}
    })

def dim_to_maj(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'dim': {'root': -2, '5th': 1, 'expect': 'maj'}
    })

# TODO: what is this transformation? too much movement
def dim_to_min_wat(chord, edo):
    assert edo == 12
    return generic_chord_transform(chord, edo, {
        'dim': {'root': 1, '3rd': 1, '5th': 2, 'expect': 'min'}
    })
