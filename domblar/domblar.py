from domblar.sc3.client import SC3Client
from domblar.sc3.instruments import setup_instruments, assign_instrument
from domblar.players import play


class Domblar:
    def __init__(self, synth_count, vst_name, preset_name):
        self.client = SC3Client()
        self.synths = setup_instruments(self.client,
                synth_count, vst_name, preset_name)

    def set_synth(self, synth_idx, synth_name):
        assign_instrument(synth_idx, synth_name, self.synths, self.client)

    def play(self, chords, scale, edo, dur=0.25, sus=None, delay=None, synth_idx=0):
        play(chords, scale, edo, self.client,
             dur=dur, sus=sus, delay=delay, synth_idx=synth_idx)

    def stop_server(self):
        self.client.stop_server()
