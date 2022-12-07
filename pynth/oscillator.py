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
        for isignal in range(0, len(signal), self.synth.BUFFER_SIZE):
            buffer = np.zeros(min(len(signal) - isignal, self.synth.BUFFER_SIZE))
            for ibuffer in range(len(buffer)):
                buffer[ibuffer] = interpolate_linearly(self.wavetable, self.wavetable.index)
                buffer[ibuffer] = self.envelope.apply_envelope(buffer[ibuffer], isignal + ibuffer, sample_rate, release=release)
                
                self.wavetable.index = (self.wavetable.index + index_increment) % self.wavetable.n_samples
            signal[isignal:isignal+self.synth.BUFFER_SIZE] = buffer
            
        return signal
    
    def apply_gain(self, signal):
        amplitude = 10 ** (self.gain/20)
        return signal * amplitude
    