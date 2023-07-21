import time

import pyOSC3

from domblar.music_math import freq_to_midi


class SC3Client:
    def __init__(self, ip='127.0.0.1', port=57120):
        self.client = pyOSC3.OSCClient()
        self.client.connect((ip, port))
        # TODO:
        # self.server = pyOSC3.OSCServer((ip, 7771))

    def send_msg(self, address, data=[], timetag=0, sleep=None):
        bundle = pyOSC3.OSCBundle(time=timetag)
        msg = pyOSC3.OSCMessage(address=address)
        msg.append(data)
        bundle.append(msg)
        self.client.send(bundle)
        if sleep:  # for some heavy operations
            time.sleep(sleep)

    def send_note(self, synth_idx, freq=None, dur=0.25, amp=1.0, timetag=0, channel=0,
                  lpf=None, lpr=1.0):
        if freq is None:
            return
        # FIXME
        if lpf is None:
            lpf = 20000.0
        data = [synth_idx]
        note, bend = freq_to_midi(freq, synth_idx)
        # FIXME: maybe there's a better way to do this? instead of 0 state
        state = 0  # 0 means a non-drone note with finite duration
        # FIXME: move 127 to shared-Python/SuperCollider-constants config file
        data.extend([note, bend, dur, int(amp * 127), channel, state,
                     int(lpf * 127), int(lpr * 127)])
        self.send_msg('/play', data, timetag=timetag)

    def stop_server(self):
        self.send_msg('/stop_server', [])

    def open_editor(self, synth_idx):
        self.send_msg('/open_editor', data=[synth_idx])

    def save_preset(self, synth_idx, preset_name):
        self.send_msg('/save_preset', data=[synth_idx, preset_name])

    def load_preset(self, synth_idx, preset_name):
        self.send_msg('/load_preset', data=[synth_idx, preset_name])

    def set_param(self, synth_idx, param, val):
        self.send_msg('/set_param', data=[synth_idx, param, val])

    def print_params(self, synth_idx):
        # TODO: rename param?
        # i have clash in terminology (params here, and params in synth like amp or room)
        self.send_msg('/print_params', data=[synth_idx])

    # FIXME: convert this into resource handling, or into a decorator
    def rec(self):
        self.send_msg('/record', [])
        time.sleep(2)

    def stop_rec(self):
        time.sleep(5)
        self.send_msg('/stop_recording', [])
