import numpy as np

class Filter:
    def __init__(self, type = "lowpass", cutoff_frequency = 2000):
        self.type = type
        self.cutoff_frequency = cutoff_frequency
        
        self.dn_1 = 0 #Inner buffer of the filter
    
    def apply_filter(self, signal, sample_rate):
        filter_output = np.zeros_like(signal)
        break_frequency = self.cutoff_frequency
        tan = np.tan(np.pi * break_frequency / sample_rate)
        a1 = (tan - 1) / (tan + 1)
        
        for i in range(len(signal)):
            filter_output[i] = a1 * signal[i] + self.dn_1
        
            self.dn_1 = signal[i] - a1 * filter_output[i]
        
        if self.type == "highpass":
            filter_output *= -1
            
        return (signal + filter_output) * 0.5
        