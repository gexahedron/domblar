import time

from domblar.sc3.client import SC3Client
from domblar.sc3.instruments import setup_instruments, assign_instrument
from domblar.players import play


class Domblar:
    def __init__(self, synth_count, context, analysis_mode=False):
        self.client = SC3Client()

        assert context == 'dexed'
        self.vst_name = 'Dexed.vst3'
        self.init_preset_name = 'dexed_preset'
        self.tmp_preset_name = 'dexed_instrument'
        self.analysis_mode = analysis_mode

        if not self.analysis_mode:
            self.synths = setup_instruments(
                self.client,
                synth_count, self.vst_name, self.init_preset_name)

    def set_synth(self, synth_idx, synth_name):
        if not self.analysis_mode:
            assign_instrument(synth_idx, synth_name, self.synths, self.client)

    def set_param(self, synth_idx, param, val):
        # assuming that val is float and in [0..1] range
        self.client.set_param(synth_idx, param, int(val * 127))

    def play(self, chords, scale, edo,
             dur=0.25, sus=None, delay=None, synth_idx=[0], rep=1,
             muls=[], amps=[], voice_amps=[]):
        if not self.analysis_mode:
            play(chords, scale, edo, self.client,
                dur=dur, sus=sus, delay=delay, synth_idx=synth_idx, muls=muls, rep=rep,
                amps=amps, voice_amps=voice_amps)

    def stop_server(self):
        self.client.stop_server()

    def open_editor(self, synth_idx):
        self.client.open_editor(synth_idx)

    def save_preset(self, synth_idx):
        self.client.save_preset(synth_idx, self.tmp_preset_name)

    def load_preset(self, synth_idx):
        self.client.load_preset(synth_idx, self.tmp_preset_name)

    def print_params(self, synth_idx):
        self.save_preset(synth_idx)
        time.sleep(0.5)
        self.load_preset(synth_idx)
        time.sleep(0.5)
        self.client.print_params(synth_idx)
