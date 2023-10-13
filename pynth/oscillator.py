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
        self.gain = -10
        self.volume = FloatParameter(1, (0, 1))
        
    def output_signal(self, f, time):
        signal = self.build_signal(f, time)
        signal = self.apply_gain(signal)

        return signal
    
    def build_signal(self, f, time, release = False):
        signal = np.zeros(int(time*self.synth.SAMPLE_RATE))
        for i in range(time * self.synth.SAMPLE_RATE):
            signal[i] = next(self)
            
        return signal
    
    def chunks(self):
        while True:
            chunk = [next(self) for _ in range(self.synth.BUFFER_SIZE)]
            yield chunk 

    def apply_gain(self, signal):
        amplitude = 10 ** (self.gain/20)
        return signal * amplitude * self.volume.value

    def set_waveform(self, waveform):
        self.wavetable.set_waveform(waveforms.get_waveform(waveform))
        
    def __next__(self):
        index_increment = self.synth.frequency.value * self.wavetable.n_samples / self.synth.SAMPLE_RATE
        val = self.wavetable[self.wavetable.index + index_increment]
        return val
