import pyOSC3
import math


def freq2midi(freq):
    # 440 - A4_FREQ, 69 - A4_MIDI
    pitch_bend_sensitivity = 48  # MPE
#     pitch_bend_sensitivity = 24  # MPE
    # pitch_bend_sensitivity = 2  # normal
    bended_note = 69 + 12 * math.log(freq / 440, 2)
    # assume that bend should be in 8192+[0..8192)/pitch_bend_sensitivity range
    note = math.floor(bended_note)
    bend = int(8192 * ((bended_note - note) / pitch_bend_sensitivity + 1))
    return note, bend


def send_msg(client, address, data, timetag=0):
    bundle = pyOSC3.OSCBundle(time=timetag)
    msg = pyOSC3.OSCMessage(address=address)
    msg.append(data)
    bundle.append(msg)
    client.send(bundle)


def send_note(synth_idx, freq=None, dur=0.25, timetag=0, channel=0):
    if freq is None:
        return
    # todo:
    # if freq is not None:
    #     data += ['freq', freq]
    data = [synth_idx]
    note, bend = freq2midi(freq)
    data.extend([note, bend, dur, channel])
    send_msg('/tracker', data, timetag=timetag)
