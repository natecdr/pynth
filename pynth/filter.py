import numpy as np

class Filter:
    def __init__(self, type = "lowpass", cutoff_frequency = np.inf):
        self.type = type
        self.cutoff_frequency = cutoff_frequency
    
    