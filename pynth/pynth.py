from pynth.oscillator import Oscillator
import sounddevice as sd

class Pynth:
    def __init__(self):
        self.osc1 = Oscillator()
        
    def play(self, f, time, sample_rate):
        osc1_signal = self.osc1.output_signal(f, time, sample_rate)
        
        signal = osc1_signal
        sd.play(signal, sample_rate)
        sd.wait()
        print(sd.get_status())
        
        
