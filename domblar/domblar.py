import time

from domblar.chord_theory import chords_to_voices
from domblar.players import play
from domblar.sc3.client import SC3Client
from domblar.sc3.instruments import setup_instruments, assign_instrument
from domblar.tracker import Tracker


class Domblar:
    def __init__(self, synth_count, context, mode='once'):
        self.client = SC3Client()

        assert context == 'dexed'
        self.vst_name = 'Dexed.vst3'
        self.init_preset_name = 'dexed_preset'
        self.tmp_preset_name = 'dexed_instrument'
        self.mode = mode  # could be 'once', 'tracker', 'analysis'
        self.analysis_mode = (self.mode == 'analysis')

        if not self.analysis_mode:
            self.synths = setup_instruments(
                self.client,
                synth_count, self.vst_name, self.init_preset_name)
            self.tracker = Tracker(client=self.client, synth_count=synth_count)

    def set_synth(self, synth_idx, synth_name, synth_name2=None, proportion=None,
                  shift=0, param_count=None):
        if not self.analysis_mode:
            import sys, importlib
            importlib.reload(sys.modules['domblar.sc3.instruments'])
            from domblar.sc3.instruments import update_instruments
            self.synths = update_instruments()
            assign_instrument(synth_idx, synth_name, self.synths, self.client,
                              synth_name2=synth_name2, proportion=proportion,
                              shift=shift, param_count=param_count)

    def set_param(self, synth_idx, param, val):
        # assuming that val is float and in [0..1] range
        self.client.set_param(synth_idx, param, int(val * 127))

    # FIXME: default values
    # FIXME: parameters are copied from inner methods
    def play(self, chords_or_voices, scale, edo,
             dur=0.25, sus=None, delay=None, synth_idx=[0], rep=1,
             muls=[], amps=[], voice_amps=[],
             once=False, loop_from=0):
        if not self.analysis_mode:
            if self.mode == 'once':
                # FIXME: remove this, by reusing tracker
                play(chords_or_voices, scale, edo, self.client,
                    dur=dur, sus=sus, delay=delay, synth_idx=synth_idx, muls=muls, rep=rep,
                    amps=amps, voice_amps=voice_amps)
            else:
                from domblar.chord_theory import Voices
                if not type(chords_or_voices) is Voices:
                    # FIXME: we imply here that we expect chords
                    voices = chords_to_voices(chords_or_voices.evaluate())
                else:
                    voices = chords_or_voices
                assert type(voices) is Voices
                print('voices.events', voices.events)
                self.tracker.queue(voices.events, edo, dur,
                                   sus=sus,
                                   once=once,
                                   loop_from=loop_from,
                                   )

    def __lt__(self, events):
        # FIXME:
        assert self.mode == 'tracker'

        # NOTE: this is some gimmicky
        if type(events) is list:
            assert len(events) == 1
            events = events[0]

        # FIXME: remove scale, edo and config
        self.play(events, None, events.config.edo,
                  dur=events.config.dur,
                  sus=events.config.sus,
                  once=events.config.once
                  )

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

    def rec(self):
        self.client.rec()

    def stop_rec(self):
        self.client.stop_rec()
