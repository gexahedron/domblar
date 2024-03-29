from sc3.base import Platform
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
                proc.kill()
                break
        except Exception as _:
            pass
        
    time.sleep(1.0)
    load_sc3()
