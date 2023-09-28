import numpy as np
import matplotlib.pyplot as plt
from pynth.parameter_types import FloatParameter
import math

class Wavetable:
    def __init__(self, waveform, n_samples = 2048):
        self.n_samples = n_samples
        self.set_waveform(waveform)
        self.index = 0
        self.phase = FloatParameter(0, (0, 360))
        self.build_wavetable()
    
    def set_waveform(self, waveform):
        self.waveform = waveform
        self.build_wavetable()
            
    def build_wavetable(self):
        self.wavetable = [self.waveform(2 * np.pi * i / self.n_samples) for i in range(self.n_samples)]
                    
    def __getitem__(self, index):
        self.index = int((index + int(self.phase.value/360 * self.n_samples)) % self.n_samples)
        return self.wavetable[self.index]
    