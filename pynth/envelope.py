from pynth.parameter_types import FloatParameter

class Envelope:
    def __init__(self, synth, attack = 0, decay = 0, sustain = 1, release = 0.1, links = []):
        self.synth = synth
        self.attack = FloatParameter(attack, (0, 1))
        self.decay = FloatParameter(decay, (0, 1))
        self.sustain = FloatParameter(sustain, (0, 1))
        self.release = FloatParameter(release, (0, 1))
        self.links = links
        
    def get_envelope_value(self, index, sample_rate, release = False):
        time = index / sample_rate
        
        if release:
            return self.get_release(time)
        
        if time < self.attack.value:
            return self.get_attack(time)
        elif time < self.attack.value + self.decay.value:
            return self.get_decay(time)
        else:
            return self.sustain.value
        
    def get_release(self, time):
        return (1 - time/self.release.value) * self.sustain.value
        
    def get_attack(self, time):
        return time/self.attack.value
    
    def get_decay(self, time):
        decay_weight = (time - self.attack.value) / self.decay.value
        
        attenuation = (1 - (1 - self.sustain.value) * decay_weight)
        
        return attenuation
        