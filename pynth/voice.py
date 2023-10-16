from pynth.wavetable import Wavetable
import time
from copy import deepcopy

class Voice:
    def __init__(self, synth, frequency):
        self.synth = synth
        self.frequency = frequency
        self.start_time = time.time()
        
        self.osc1Voice = OscVoice(self.synth.osc1, self.synth.frequency)
        self.osc2Voice = OscVoice(self.synth.osc2, self.synth.frequency)
        self.synth.osc1.voices.append(self.osc1Voice)
        self.synth.osc2.voices.append(self.osc2Voice)
        
        self.ampEnvVoice = EnvVoice(self.synth.ampEnv)
        self.modEnv1Voice = EnvVoice(self.synth.modEnv1)
        self.modEnv2Voice = EnvVoice(self.synth.modEnv2)
        
    def render_signal(self, duration):
        osc1_signal = self.synth.osc1.output_signal(self.frequency.value, duration)
        osc2_signal = self.synth.osc2.output_signal(self.frequency.value, duration)
        
        signal = osc1_signal + osc2_signal
        
        return signal
    
    def __next__(self):
        next(self.ampEnvVoice)
        next(self.modEnv1Voice)
        next(self.modEnv2Voice)
        
        osc1_val = next(self.synth.osc1)
        osc2_val = next(self.synth.osc2)
        
        val = osc1_val + osc2_val
        
        return val
        
    def clear_osc_voices(self):
        self.synth.osc1.voices.remove(self.osc1Voice)
        self.synth.osc2.voices.remove(self.osc2Voice)
    
class OscVoice:
    def __init__(self, osc, frequency):
        self.osc = osc
        self.index_in_wavetable = osc.wavetable.index
        self.frequency = frequency
        
class EnvVoice:
    def __init__(self, envelope):
        self.envelope = envelope
        self.index = 0
        
    def __next__(self):
        envelope_value = self.envelope.get_envelope_value(self.index, self.envelope.synth.SAMPLE_RATE, release=False)
        for link in self.envelope.links:
            link.value = link.base_value * envelope_value
            
        self.index += 1
        
    
        