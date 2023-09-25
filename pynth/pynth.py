from pynth.oscillator import Oscillator
from pynth.envelope import Envelope
from pynth.filter import Filter
import sounddevice as sd


class Pynth:
    BUFFER_SIZE = 1024
    
    def __init__(self):
        self.ampEnv = Envelope()
        self.filter = Filter()
        
        self.osc1 = Oscillator(self)
        self.osc2 = Oscillator(self)
        
    def play(self, f, time, sample_rate):
        osc1_signal = self.osc1.output_signal(f, time, sample_rate)
        osc2_signal = self.osc2.output_signal(f, time, sample_rate)
        
        signal = osc1_signal + osc2_signal
        
        sd.play(signal, sample_rate)
        sd.wait()
        