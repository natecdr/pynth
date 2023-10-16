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
        self._wavetable = np.array([self.waveform(2 * np.pi * i / self.n_samples) for i in range(self.n_samples)])
        
    def interpolate_linearly(self, wavetable, index_in_wavetable):
        lower_index = int(np.floor(index_in_wavetable))
        upper_index = (lower_index + 1) % wavetable.n_samples
        
        upper_index_weight = index_in_wavetable - lower_index
        lower_index_weight = 1 - upper_index_weight
        
        return self._wavetable[lower_index] * lower_index_weight + self._wavetable[upper_index] * upper_index_weight
                    
    def __getitem__(self, index):
        index = index % self.n_samples
        phase_adjusted_index = (index + int(self.phase.value/360 * self.n_samples)) % self.n_samples
        return self.interpolate_linearly(self, phase_adjusted_index), index
    