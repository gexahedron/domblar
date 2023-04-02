import ipywidgets as widgets
from ipywidgets import GridspecLayout
from IPython.display import display

from copy import deepcopy
import threading
import time

from domblar.edo import get_freq


class Tracker():
    def __init__(self, client, synth_count):
        self.client = client
        self.running = False
        self.thread_is_started = False
        # FIXME
        self.thread2_is_started = False

        # FIXME: well, there's a lot to fix here
        self.clear()
        self.d = None
        self.dur = 0.25
        self.synth_idx = None
        self.voice_amps = []
        # FIXME: this is just a separate fixme for this atrocity
        self.sleep_time = 4 * self.dur
        self.rep = 1
        self.loop = True

        self.start(synth_count)

    def clear(self):
        self.voices = None
        self.edo = None
        self.sus = None
        self.loop_from = 0
        self.loop_idx = 0

        self.next_voices = None
        self.next_edo = None
        self.next_sus = None
        self.next_dur = None
        self.next_loop_from = None
        self.set_synth_query = None

    def eternal_run(self):
        while True:
            self.single_run()

    def set_synth_monitor(self):
        while True:
            if self.set_synth_query is not None:
                # FIXME: this appoarch is very hiccup-y
                reps, whole_dur, synth_idx,\
                    instr1, instr2, shift, param_count = self.set_synth_query
                self.set_synth_query = None

                dur = whole_dur / reps
                for prop in range(reps):
                    self.d.set_synth(synth_idx, instr1, instr2,
                                     1.0 - prop / reps,
                                     shift, param_count)
                    time.sleep(dur)
            else:
                time.sleep(self.dur)

    def modulate_synth(self,
                       reps, whole_dur, synth_idx,
                       instrument1, instrument2,
                       shift=0, param_count=None):
        self.set_synth_query = (reps, whole_dur, synth_idx,
                                instrument1, instrument2,
                                shift, param_count)

    # FIXME: remove dependence on edo and scale
    def schedule(self):
        # FIXME: this method is too big and messy
        if self.synth_idx is None:
            self.synth_idx = list(range(len(self.voices)))
        if type(self.rep) is list:
            assert len(self.synth_idx) == len(self.rep)
        else:
            self.rep = [self.rep] * len(self.synth_idx)
        last_reps = [0] * len(self.synth_idx)

        scale = list(range(self.edo))

        last_event_idx = [0] * len(self.voices)
        if self.loop_idx > 0:
            last_event_idx = [self.loop_from] * len(self.voices)
        last_event_time = [0] * len(self.voices)
        final_sleep = 0
        start_time = time.time()
        self.latency = 0  # 0.02  # FIXME: remove
        beats_ahead = 2  # FIXME: also move this somewhere else
        total_beat_count = 0
        for event in self.voices[0]:
            total_beat_count += event[1]

        progressed = True
        waiting = False
        while self.running and (progressed or waiting):
            progressed = False
            waiting = False
            for voice_idx in range(len(self.voices)):
                if not self.running:
                    break
                if last_event_idx[voice_idx] >= len(self.voices[voice_idx]):
                    continue
                waiting = True
                cur_beat = (time.time() - start_time) / self.dur
                self.progress.value = cur_beat / total_beat_count
                if last_event_time[voice_idx] > cur_beat + beats_ahead:
                    continue

                note, note_beat_count = self.voices[voice_idx][last_event_idx[voice_idx]]
                freq = get_freq(note, scale, self.edo)
                send_note_dur = self.dur
                if self.sus:
                    send_note_dur = self.sus
                send_note_dur *= note_beat_count
                amp = 1.0
                # FIXME:
                # if self.voice_amps:
                    # amp *= self.voice_amps[voice_idx]
                amp *= self.voice_amps[voice_idx].value

                cur_beat = (time.time() - start_time) / self.dur
                if last_event_time[voice_idx] > cur_beat + beats_ahead:
                    continue
                # FIXME: is it a right formula though?
                # i mean, the thing with latency
                timetag = start_time + last_event_time[voice_idx] * self.dur + self.latency
                final_sleep = max(final_sleep, timetag + note_beat_count * self.dur)

                self.client.send_note(
                    self.synth_idx[voice_idx] + last_reps[voice_idx],
                    freq=freq, dur=send_note_dur, amp=amp,
                    timetag=timetag, channel=0) # TODO: for MPE with channels use channel=note_idx
                last_reps[voice_idx] = (last_reps[voice_idx] + 1) % self.rep[voice_idx]

                last_event_idx[voice_idx] += 1
                last_event_time[voice_idx] += note_beat_count
                progressed = True

            if waiting and not progressed:
                # sleep 1 beat
                time.sleep(self.dur)

        if self.running:
            time.sleep(final_sleep - time.time())

    def single_run(self):
        play = self.loop
        if self.next_voices is not None:
            play = True
            self.loop_idx = 0
            self.voices = deepcopy(self.next_voices)
            self.edo = self.next_edo
            self.dur = self.next_dur
            self.sus = self.next_sus
            self.loop_from = self.next_loop_from
            # FIXME
            self.sleep_time = 4 * self.dur

            self.next_voices = None
        if self.running and self.voices and play:
            self.schedule()
            self.loop_idx += 1
        else:
            time.sleep(self.sleep_time)

    def print_state(self):
        if self.running:
            print("I'm alive")
        else:
            print("Sleeping...")

    def stop(self):
        self.running = False

    def setup_dashboard(self):
        self.voice_amps = []
        for idx in range(self.synth_count):
            layout = widgets.Layout(width='75%')
            # if idx == 0:
                # layout = widgets.Layout(width='95%')
            self.voice_amps.append(
                widgets.FloatSlider(
                    min=0,
                    max=2.0,
                    step=0.05,
                    description=f'Vol{idx}',  # TODO/FIXME: maybe it should be idx+1?
                    value=1.0,
                    orientation='vertical',
                    layout=layout,
                    readout_format='.1f',
                )
            )
        self.progress = widgets.FloatProgress(
            value=0.0,
            min=0,
            max=1.0,
            step=0.01,
            description='Loop %',
            bar_style='info',
            orientation='horizontal',
            layout=widgets.Layout(width='80%')
        )

    def show_dashboard(self):
        grid = GridspecLayout(9, len(self.voice_amps), width='50%')
        grid[0, :] = self.progress
        for voice_amp_idx, voice_amp in enumerate(self.voice_amps):
            grid[1:, voice_amp_idx] = voice_amp
        display(grid)

    def start(self, synth_count):
        self.synth_count = synth_count
        self.clear()
        self.running = True
        if not self.thread_is_started:
            self.thread_is_started = True
            thread = threading.Thread(target=self.eternal_run)
            thread.start()
        # FIXME: remove?
        if not self.thread2_is_started:
            self.thread2_is_started = True
            thread2 = threading.Thread(target=self.set_synth_monitor)
            thread2.start()

        self.setup_dashboard()

    # FIXME: rename
    def queue(self, voices, edo, dur, sus=None, once=False, loop_from=0):
        # FIXME:
        if once is None:
            once = False

        self.running = True

        if self.next_voices:
            print("Can't queue, please wait...")
            return False
        self.next_voices = deepcopy(voices)
        self.next_edo = edo
        self.next_sus = sus
        self.next_dur = dur
        self.next_loop_from = loop_from
        self.loop = not once
        print('Queued!')
        return True
