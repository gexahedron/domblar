import pyOSC3
from ..music_math import freq2midi


def send_msg(client, address, data, timetag=0):
    bundle = pyOSC3.OSCBundle(time=timetag)
    msg = pyOSC3.OSCMessage(address=address)
    msg.append(data)
    bundle.append(msg)
    client.send(bundle)


def send_note(client, synth_idx, freq=None, dur=0.25, timetag=0, channel=0):
    if freq is None:
        return
    # TODO:
    # if freq is not None:
    #     data += ['freq', freq]
    data = [synth_idx]
    note, bend = freq2midi(freq)
    data.extend([note, bend, dur, channel])
    send_msg(client, '/tracker', data, timetag=timetag)
