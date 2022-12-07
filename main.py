from pynth.pynth import Pynth
from pynth.wavetable import Wavetable
import pynth.waveforms as waveforms
import matplotlib.pyplot as plt

pynth = Pynth()
pynth.osc1.wavetable = Wavetable(waveforms.sawtooth)
pynth.play(440, 1, 44100)