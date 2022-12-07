import numpy as np
import pynth.waveforms as waveforms
from pynth.wavetable import Wavetable
from pynth.envelope import Envelope
from pynth.utils import *

import matplotlib.pyplot as plt

class Oscillator:
    def __init__(self, synth, wavetable = Wavetable(waveforms.sine), envelope = Envelope(), gain = -10):
        self.synth = synth
        self.wavetable = wavetable
        self.envelope = envelope
        self.gain = gain
        
    def output_signal(self, f, time, sample_rate):
        signal = self.build_signal(f, time, sample_rate)
        release = self.build_signal(f, self.envelope.release, sample_rate, release=True)
            
        signal = np.concatenate((signal, release))
        signal = self.apply_gain(signal)

        return signal
    
    def build_signal(self, f, time, sample_rate, release = False):
        index_increment = f * self.wavetable.n_samples / sample_rate
        
        signal = np.zeros(int(time * sample_rate))
        for i in range(len(signal)):
            signal[i] = interpolate_linearly(self.wavetable, self.wavetable.index)
            signal[i] = self.envelope.apply_envelope(signal[i], i, sample_rate, release=release)
            
            self.wavetable.index = (self.wavetable.index + index_increment) % self.wavetable.n_samples
            
        return signal
    
    def apply_gain(self, signal):
        amplitude = 10 ** (self.gain/20)
        return signal * amplitude
    