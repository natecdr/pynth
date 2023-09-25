import numpy as np
from scipy import signal

def sine(x):
    return np.sin(x)

def saw(x):
    return (x + np.pi) / np.pi % 2 -1

def square(x):
    return signal.square(x)

def triangle(x):
    return abs(saw(x)) * 2 - 1 

def get_waveform(waveform : str):
    waveforms = {
        "sine": sine,
        "saw": saw,
        "square" : square,
        "triangle": triangle
    }
    
    return waveforms[waveform]