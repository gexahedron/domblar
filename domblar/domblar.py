import platform
import time
from enum import Enum, auto

from domblar.chord_theory import chords_to_voices
from domblar.players import play, play_non_edo
from domblar.sc3.instruments import assign_instrument, setup_instruments
from domblar.tracker import Tracker
from domblar.beat_tracker import BeatTracker


class Mode(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    analysis = auto()
    tracker = auto()
    beat_tracker = auto()
    once = auto()


class Domblar:
    def __init__(self, context, synth_count=None, mode='once'):
        self.client = None
        if context != 'python-sc3':
            from domblar.sc3.client import SC3Client
            self.client = SC3Client()
            assert synth_count is not None
        self.synth_count = synth_count
        self.context = context
        self.mode = mode
        self.instruments = {}

        # beat_tracker mode specifics:
        self.cur_track = None
        self.chroma = None
        self.scale = None
        self.bpm = None
        if self.mode == Mode.beat_tracker:
            self.beat_tracker = BeatTracker(client=self.client)

        self.setup_context(context)

        self.tmp_preset_name = 'instrument_preset'

        if self.mode != Mode.analysis:
            self.synths = setup_instruments(
                self.client,
                synth_count,
                self.context, self.vst_name, self.init_preset_name,
                self.pitch_bend_sensitivity)
            self.tracker = Tracker(client=self.client, synth_count=synth_count)

    def setup_context(self, context):
        match context:
            case 'portafm':
                FIXME: 1. MPE -> Normal; 48 -> 2
                self.vst_name = 'chipsynth PortaFM'
                # FIXME - create preset
                # self.init_preset_name = 'portafm_preset'
                self.init_preset_name = None
                self.pitch_bend_sensitivity = 48
            case 'md':
                self.vst_name = 'chipsynth MD'
                # FIXME - create preset
                # self.init_preset_name = 'md_preset'
                self.init_preset_name = None
                self.pitch_bend_sensitivity = 2
            case 'dexed':
                self.vst_name = 'Dexed.vst3'
                self.init_preset_name = 'dexed_preset'
                self.pitch_bend_sensitivity = 48
            case 'opl':
                match platform.system():
                    case 'Linux':
                        self.vst_name = 'OPL.so'
                    case _:  # 'Darwin' (MacOS) or 'Windows'
                        self.vst_name = 'OPL.vst3'
                self.init_preset_name = None
                self.pitch_bend_sensitivity = 1
            case 'tyrelln6':
                match platform.system():
                    case 'Linux':
                        self.vst_name = 'TyrellN6.64.so'
                    case _:  # 'Darwin' (MacOS) or 'Windows'
                        self.vst_name = 'TyrellN6.vst'
                self.init_preset_name = None
                self.pitch_bend_sensitivity = 2
            case 'python-sc3':
                self.vst_name = None
                pass
            case _:
                print(f'Unknown vst/context: {context}')
                assert False

        self.tmp_preset_name = 'instrument_preset'

        if self.mode != Mode.analysis and self.vst_name is not None:
            self.synths = setup_instruments(
                self.client,
                synth_count,
                self.context, self.vst_name, self.init_preset_name,
                self.pitch_bend_sensitivity)
            self.tracker = Tracker(client=self.client, synth_count=synth_count)

    def set_synth(self, synth_idx, synth_name, synth_name2=None, proportion=None,
                  shift=0, param_count=None):
        if self.mode == Mode.analysis:
            return
        if synth_idx in self.instruments and self.instruments[synth_idx] == synth_name:
            return
        import importlib
        import sys
        importlib.reload(sys.modules['domblar.sc3.instruments'])
        from domblar.sc3.instruments import update_instruments
        self.synths = update_instruments(self.context)
        assign_instrument(synth_idx, synth_name, self.synths, self.client,
                            synth_name2=synth_name2, proportion=proportion,
                            shift=shift, param_count=param_count)

    def set_param(self, synth_idx, param, val: float):
        # assuming that val is float and in [0..1] range
        assert 0 <= val <= 1
        # FIXME: move 127 to shared-Python/SuperCollider-constants config file
        self.client.set_param(synth_idx, param, int(val * 127))

    def play_non_edo(self, chords_or_voices,
                     dur=0.25, sus=None, delay=None, synth_idx=[0], rep=1,
                     muls=[], amps=[], voice_amps=[],
                     once=False, loop_from=0):
        if self.mode != Mode.analysis:
            assert self.mode == Mode.once
            # FIXME: remove this, by reusing tracker
            play_non_edo(chords_or_voices, self.client,
                 dur=dur, sus=sus, delay=delay, synth_idx=synth_idx,
                 muls=muls, rep=rep,
                 amps=amps, voice_amps=voice_amps,
                 )

    # FIXME: default values
    # FIXME: parameters are copied from inner methods
    def play(self, chords_or_voices, scale, edo,
             dur=0.25, sus=None, delay=None, synth_idx=[0], rep=1,
             muls=[], amps=[], voice_amps=[],
             once=False, loop_from=0):
        match self.mode:
            case Mode.analysis:
                return
            case Mode.once:
                # FIXME: remove this, by reusing tracker
                play(chords_or_voices, scale, edo, self.client,
                        dur=dur, sus=sus, delay=delay, synth_idx=synth_idx,
                        muls=muls, rep=rep,
                        amps=amps, voice_amps=voice_amps,
                        )
            case Mode.tracker:
                from domblar.chord_theory import Voices
                if not type(chords_or_voices) is Voices:
                    # FIXME: we assume here that we expect chords
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
            case Mode.beat_tracker:
                # FIXME
                assert False


    def __lt__(self, events):
        assert self.mode in [Mode.tracker, Mode.beat_tracker]

        # NOTE: this is a fancy thing,
        # to allow notation such as "<["
        if isinstance(events, list):
            assert len(events) == 1
            events = events[0]

        if self.mode == Mode.tracker:
            # FIXME: remove scale, edo and config
            self.play(events, None, events.config.edo,
                    dur=events.config.dur,
                    sus=events.config.sus,
                    once=events.config.once
                    )
        else:  # self.mode == Mode.beat_tracker
            print('events', type(events))
            print(events.notes)
            if events.instrument is not None:
                self.set_synth(self.cur_track, events.instrument)
            self.beat_tracker.queue(self.cur_track, events, self)

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

    def finetune(self, synth_idx=0, state=0):
        match state:
            case 0:
                self.open_editor(synth_idx)
            case 1:
                # transfer instrument to all synths
                self.save_preset(synth_idx)
                time.sleep(0.5)
                for i in range(self.synth_count):
                    self.load_preset(i)
            case _:
                self.print_params(synth_idx)

    def rec(self):
        self.client.rec()

    def stop_rec(self):
        self.client.stop_rec()

    def __getitem__(self, item):
        assert isinstance(item, int)
        self.cur_track = item
        return self
