import math


def freq2midi(freq):
    # this value works both for Dexed in non-MPE mode,
    # and for Plogue chipsynths in MPE mode
    pitch_bend_sensitivity = 48

    # 440 = A4_FREQ, 69 = A4_MIDI, 12 = 12edo
    bended_note = 69 + 12 * math.log(freq / 440, 2)

    # MIDI pitch bend range: [0, 16384)
    # default is 8192, corresponds to absence of bend
    # here we assume that pitch bend should be in 8192+[0..8192)/pitch_bend_sensitivity range
    note = math.floor(bended_note)
    bend = int(8192 * ((bended_note - note) / pitch_bend_sensitivity + 1))
    return note, bend
