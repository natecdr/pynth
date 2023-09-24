import numpy as np

def sine(x):
    return np.sin(x)

def saw(x):
    return (x + np.pi) / np.pi % 2 -1

def get_waveform(waveform : str):
    if waveform == "sine":
        return sine
    elif waveform == "saw":
        return saw
    else:
        raise NotImplementedError("This waveform is not available")