import numpy as np
import pynth.waveforms as waveforms
from pynth.wavetable import Wavetable
from pynth.envelope import Envelope
from pynth.filter import Filter
from pynth.utils import *
from pynth.parameter_types import FloatParameter
import time

class Oscillator:
    def __init__(self, synth):
        super().__init__()

        self.synth = synth
        self.wavetable = Wavetable(waveforms.sine)
        self.gain = -10
        self.volume = FloatParameter(1, (0, 1))
        
    def chunks(self):
        while True:
            chunk = [next(self) for _ in range(self.synth.BUFFER_SIZE)]
            yield chunk 

    def apply_gain(self, signal):
        amplitude = 10 ** (self.gain/20)
        return signal * amplitude * self.volume.value
    
    def apply_gain_single_val(self, val):
        amplitude = 10 ** (self.gain/20)
        return val * amplitude * self.volume.value


    def set_waveform(self, waveform):
        # self.waveform = waveforms.get_waveform(waveform)
        self.wavetable.set_waveform(waveforms.get_waveform(waveform))