import numpy as np
from pynth.parameter_types import FloatParameter

class Filter:
    def __init__(self, type = "lowpass", cutoff_frequency = 20000):
        self.type = type
        self.cutoff_frequency = FloatParameter(cutoff_frequency, (20, 20000))
        
        self.dn_1 = 0 #Inner buffer of the filter
    
    def apply_filter(self, signal, sample_rate):
        filter_output = np.zeros_like(signal)
        tan = np.tan(np.pi * self.cutoff_frequency.value / sample_rate)
        a1 = (tan - 1) / (tan + 1)
        
        for i in range(len(signal)):
            filter_output[i] = a1 * signal[i] + self.dn_1
        
            self.dn_1 = signal[i] - a1 * filter_output[i]
        
        if self.type == "highpass":
            filter_output *= -1
            
        return (signal + filter_output) * 0.5
        