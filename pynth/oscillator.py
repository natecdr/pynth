import numpy as np
import pynth.waveforms as waveforms
from pynth.wavetable import Wavetable
from pynth.envelope import Envelope
from pynth.filter import Filter
from pynth.utils import *
from pynth.parameter_types import FloatParameter

class Oscillator:
    def __init__(self, synth):
        super().__init__()
        
        self.synth = synth
        self.wavetable = Wavetable(waveforms.sine)
        self.ampEnv = synth.ampEnv
        self.filter = synth.filter
        self.gain = -10
        self.volume = FloatParameter(1, (0, 1))
        
    def output_signal(self, f, time):
        signal = self.build_signal(f, time)
        release_signal = self.build_signal(f, self.ampEnv.release.value, release=True)
            
        signal = np.concatenate((signal, release_signal))
        
        signal = self.apply_gain(signal)
        
        return signal
    
    def build_signal(self, f, time, release = False):
        index_increment = f * self.wavetable.n_samples / self.synth.SAMPLE_RATE

        signal = np.zeros(int(time * self.synth.SAMPLE_RATE))
        for isignal in range(0, len(signal), self.synth.BUFFER_SIZE):
            buffer = self.build_buffer(signal, isignal, index_increment, release)
            signal[isignal:isignal+self.synth.BUFFER_SIZE] = buffer
            
        return signal
    
    def build_buffer(self, signal, isignal, index_increment, release):
        buffer = np.zeros(min(len(signal) - isignal, self.synth.BUFFER_SIZE)) # Initialize buffer
        for ibuffer in range(len(buffer)):
            buffer[ibuffer] = interpolate_linearly(self.wavetable, self.wavetable.index)
            buffer[ibuffer] = self.ampEnv.apply_envelope(buffer[ibuffer], isignal + ibuffer, self.synth.SAMPLE_RATE, release=release)
            
            self.wavetable.index = (self.wavetable.index + index_increment) % self.wavetable.n_samples
        
        # buffer = self.filter.apply_filter(buffer, self.synth.SAMPLE_RATE)
        return buffer
    
    def apply_gain(self, signal):
        amplitude = 10 ** (self.gain/20)
        return signal * amplitude * self.volume.value

    def set_waveform(self, waveform):
        self.wavetable.set_waveform(waveforms.get_waveform(waveform))
        