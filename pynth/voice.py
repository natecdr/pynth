from pynth.wavetable import Wavetable
import time

class Voice:
    def __init__(self, synth, frequency):
        self.synth = synth
        self.frequency = frequency
        self.start_time = time.time()
        self.released = False
        
        self.osc1Voice = OscVoice(self.synth.osc1, self.frequency)
        self.osc2Voice = OscVoice(self.synth.osc2, self.frequency)

        self.ampEnvVoice = EnvVoice(self.synth.ampEnv)
        self.modEnv1Voice = EnvVoice(self.synth.modEnv1)
        self.modEnv2Voice = EnvVoice(self.synth.modEnv2)
        
    def set_released(self):
        self.released = True
        
        self.ampEnvVoice.set_released()
        self.modEnv1Voice.set_released()
        self.modEnv2Voice.set_released()

    def __next__(self):
        next(self.ampEnvVoice)
        next(self.modEnv1Voice)
        next(self.modEnv2Voice)
        
        osc1_val = next(self.osc1Voice)
        osc2_val = next(self.osc2Voice)
        
        val = osc1_val + osc2_val
        
        return val
    
class OscVoice:
    def __init__(self, osc, frequency):
        self.osc = osc
        self.index_in_wavetable = osc.wavetable.index
        self.frequency = frequency
        
    def __next__(self):
        index_increment = self.frequency.value * self.osc.wavetable.n_samples / self.osc.synth.SAMPLE_RATE
        val, new_index = self.osc.wavetable[self.index_in_wavetable + index_increment]
        
        self.index_in_wavetable = new_index
    
        val = self.osc.apply_gain_single_val(val)
  
        return val
        
class EnvVoice:
    def __init__(self, envelope):
        self.envelope = envelope
        self.index = 0
        self.release = False
        
    def set_released(self):
        self.release = True
        self.index = 0
        
    def __next__(self):
        envelope_value = self.envelope.get_envelope_value(self.index, self.envelope.synth.SAMPLE_RATE, release=self.release)
        for link in self.envelope.links:
            link.value = link.base_value * envelope_value
            
        self.index += 1
        
    
        