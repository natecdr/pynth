import numpy as np
import matplotlib.pyplot as plt

class Envelope:
    def __init__(self, attack = 0.1, decay = 0.5, sustain = 0.5, release = 0.1):
        self.attack = attack
        self.decay = decay
        self.sustain = sustain
        self.release = release
        
    def apply_envelope(self, value, index, sample_rate):
        time = index / sample_rate
        
        if time < self.attack:
            return self.add_attack(value, time)
        elif time < self.attack + self.decay:
            return self.add_decay(value, time)
        else:
            return value * self.sustain
        
    def add_attack(self, value, time):
        return time/self.attack * value
    
    def add_decay(self, value, time):
        decay_weight = (time - self.attack) / self.decay
        
        attenuation = (1 - (1 - self.sustain) * decay_weight)
        
        return value * attenuation
        