from pynth.oscillator import Oscillator
import sounddevice as sd

class Pynth:
    BUFFER_SIZE = 1024
    
    def __init__(self):
        self.osc1 = Oscillator(self)
        
    def play(self, f, time, sample_rate):
        osc1_signal = self.osc1.output_signal(f, time, sample_rate)
        
        signal = osc1_signal
        sd.play(signal, sample_rate)
        sd.wait()
        print(sd.get_status())
        
        
