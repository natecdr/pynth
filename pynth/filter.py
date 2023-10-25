import numpy as np
from pynth.parameter_types import FloatParameter

class Filter:
    def __init__(self, synth, type = "lowpass", cutoff_frequency = 20000):
        self.synth = synth
        self.type = type
        self.cutoff_frequency = FloatParameter(cutoff_frequency, (20, 20000))
        
        self.dn_1 = 0 #Inner buffer of the filter
    
    def set_type(self, type):
        self.type = type
    
    def apply_filter_single_val(self, val):
        tan = np.tan(np.pi * self.cutoff_frequency.value / self.synth.SAMPLE_RATE)
        a1 = (tan - 1) / (tan + 1)
        
        filter_output = a1 * val + self.dn_1
        self.dn_1 = val - a1 * filter_output
        
        if self.type == "highpass":
            filter_output *= -1
            
        return (val + filter_output) * 0.5
        