# FIXME:
from sc3.all import *

@synthdef
def reverb(bus:'ar'=0, out=0):
    sig = In.ar(bus, 2)
    sig = FreeVerb.ar(sig, 0.15, 0.9)
    Out.ar(out, sig)
