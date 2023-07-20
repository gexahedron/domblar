class Synths:
    synths = {}

class Synth:
    def __init__(self, synth_idx, pitch_bend_sensitivity):
        self.pitch_bend_sensitivity = pitch_bend_sensitivity
        Synths.synths[synth_idx] = self
