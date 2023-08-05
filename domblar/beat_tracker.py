from copy import deepcopy
import threading
import time

from domblar.sc3.client import SC3Client
from domblar.patterns import Patternable

class BeatTracker():
    def __init__(self, client: SC3Client):
        self.client = client
        self.running = False
        self.thread_is_started = False
        self.d = None
        self.beat_count = 0
        self.sleep_time = 1.0
        self.next_time = None
        self.last_time = None
        self.latency = 0.1

        self.clear()

        self.start()

    def clear(self):
        self.events = {}
        self.next_events = {}

    def eternal_run(self):
        while True:
            self.single_run()
            time.sleep(self.sleep_time)

    def get_dur(self):
        assert self.d is not None
        # FIXME: magic constant 2
        return 60.0 / (self.d.bpm * 2)  # 60 = number of seconds in 1 minute

    def is_time_to_sync(self):
        # FIXME: magic constant 8
        return self.beat_count % 8 == 0

    def single_run(self):
        if self.next_events and self.is_time_to_sync():
            for synth in self.next_events:
                self.events[synth] = deepcopy(self.next_events[synth])
            self.next_events = {}

        if not self.running:
            return

        bpm_dur = self.get_dur()
        self.sleep_time = bpm_dur / 10

        if not self.events:
            return

        cur_time = time.time()
        if self.last_time:
            self.next_time = self.last_time + bpm_dur
        if self.next_time is None:
            timetag = cur_time + self.latency
            schedule_events = True
        else:
            timetag = self.next_time
            schedule_events = (timetag < cur_time + 2 * self.sleep_time)
        if schedule_events:
            if timetag >= cur_time:
                for synth_idx, event in self.events.items():
                    send_note_dur = bpm_dur

                    note = event.notes[self.beat_count % len(event.notes)]
                    freq = self.d.scale.get_freq(note)

                    # TODO: automate going through these params
                    kwargs_keys = [
                        'amp',
                        'pan',
                        'mix', # TODO: room, damp
                        'lpf', 'lpr',
                    ]
                    kwargs = {}
                    for key in kwargs_keys:
                        kwargs[key] = getattr(event, f'{key}_')
                        if isinstance(kwargs[key], Patternable):
                            kwargs[key] = kwargs[key].get_val(self.beat_count)

                    self.client.send_note(
                        synth_idx,
                        timetag=timetag, channel=0,
                        freq=freq, dur=send_note_dur,
                        **kwargs
                    )
            self.last_time = timetag
            self.beat_count += 1
            self.next_time = self.last_time + bpm_dur

    def print_state(self):
        if self.running:
            print("I'm alive")
        else:
            print("Sleeping...")

    def stop(self):
        self.running = False
        self.next_time = None
        self.last_time = None

    def start(self):
        self.clear()
        if not self.thread_is_started:
            self.thread_is_started = True
            thread = threading.Thread(target=self.eternal_run)
            thread.start()

    def queue(self, track_idx, events, d):
        if self.d is None:
            self.d = d
        if not self.running:
            self.beat_count = 0  # FIXME: maybe add difference between stop/pause
        self.running = True

        if track_idx in self.next_events:
            print("Can't queue, please wait...")
            return False
        self.next_events[track_idx] = deepcopy(events)
        print('Queued!')
        return True
