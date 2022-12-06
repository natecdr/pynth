import numpy as np

class Wavetable:
    def __init__(self, waveform, n_samples = 64):
        self.waveform = waveform
        self.n_samples = n_samples
        self.build_wavetable()
        
    def build_wavetable(self):
        self.wavetable = np.zeros(self.n_samples)
        
        for i in range(self.n_samples):
            self.wavetable[i] = self.waveform(2 * np.pi * i/self.n_samples)
            
    def __getitem__(self, index):
        return self.wavetable[index]