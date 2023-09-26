from pynth.parameter_types import FloatParameter

class Envelope:
    def __init__(self, attack = 0, decay = 0, sustain = 1, release = 0.1, links = []):
        self.attack = FloatParameter(attack, (0, 1))
        self.decay = FloatParameter(decay, (0, 1))
        self.sustain = FloatParameter(sustain, (0, 1))
        self.release = FloatParameter(release, (0, 1))
        self.links = links
        
    def apply_envelope(self, value, index, sample_rate, release = False):
        time = index / sample_rate
        
        if release:
            return self.apply_release(value, time)
        
        if time < self.attack.value:
            return self.apply_attack(value, time)
        elif time < self.attack.value + self.decay.value:
            return self.apply_decay(value, time)
        else:
            return value * self.sustain.value
        
    def apply_release(self, value, time):
        return (1 - time/self.release.value) * self.sustain.value * value
        
    def apply_attack(self, value, time):
        return time/self.attack.value * value
    
    def apply_decay(self, value, time):
        decay_weight = (time - self.attack.value) / self.decay.value
        
        attenuation = (1 - (1 - self.sustain.value) * decay_weight)
        
        return value * attenuation
        