import numpy as np
import pynth.waveforms as waveforms
from pynth.wavetable import Wavetable
from pynth.envelope import Envelope
from pynth.utils import *

import matplotlib.pyplot as plt

class Oscillator:
    def __init__(self, wavetable = Wavetable(waveforms.sine), envelope = Envelope(), gain = -10):
        self.wavetable = wavetable
        self.envelope = envelope
        self.gain = gain
        
    def output_signal(self, f, time, sample_rate):
        signal = np.zeros(time * sample_rate)
        
        index_in_wavetable = 0
        index_increment = f * self.wavetable.n_samples / sample_rate
        
        for i in range(len(signal)):
            signal[i] = interpolate_linearly(self.wavetable, index_in_wavetable)
            signal[i] = self.envelope.apply_envelope(signal[i], i, sample_rate)
            
            index_in_wavetable = (index_in_wavetable + index_increment) % self.wavetable.n_samples
        
        signal = self.apply_gain(signal)
        
        plt.plot(signal)
        plt.show()
    
        return signal
        
    def apply_gain(self, signal):
        amplitude = 10 ** (self.gain/20)
        return signal * amplitude
    