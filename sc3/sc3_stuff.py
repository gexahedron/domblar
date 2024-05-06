# FIXME:
from sc3.base import *
from sc3.synth.server import s
import time
import psutil


def load_sc3():
    if 'started' in globals():
        Platform.killall('scsynth')
        time.sleep(1)
    s.boot()
    time.sleep(3)


def restart():
    for proc in psutil.process_iter():
        try:
            if proc.name() == 'scsynth':
                proc.terminate()
                # TODO: maybe not terminate(), but kill()
                procs = [proc]
                gone, alive = psutil.wait_procs(procs, timeout=3, callback=on_terminate)
                break
        except Exception as _:
            pass
        
    time.sleep(1.0)
    load_sc3()
