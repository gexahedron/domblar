import pyOSC3
from domblar.music_math import freq_to_midi


class SC3Client:
    def __init__(self, ip='127.0.0.1', port=57120):
        self.client = pyOSC3.OSCClient()
        self.client.connect((ip, port))

    def send_msg(self, address, data, timetag=0):
        """TODO: _summary_

        Args:
            client (_type_): _description_
            address (_type_): _description_
            data (_type_): _description_
            timetag (int, optional): _description_. Defaults to 0.
        """
        bundle = pyOSC3.OSCBundle(time=timetag)
        msg = pyOSC3.OSCMessage(address=address)
        msg.append(data)
        bundle.append(msg)
        self.client.send(bundle)

    def send_note(self, synth_idx, freq=None, dur=0.25, timetag=0, channel=0):
        """TODO:_summary_

        Args:
            synth_idx (_type_): _description_
            freq (_type_, optional): _description_. Defaults to None.
            dur (float, optional): _description_. Defaults to 0.25.
            timetag (int, optional): _description_. Defaults to 0.
            channel (int, optional): _description_. Defaults to 0.
        """
        if freq is None:
            return
        # TODO:
        # if freq is not None:
        #     data += ['freq', freq]
        data = [synth_idx]
        note, bend = freq_to_midi(freq)
        data.extend([note, bend, dur, channel])
        self.send_msg('/play', data, timetag=timetag)

    def stop_server(self):
        self.send_msg('/stop_server', [])
