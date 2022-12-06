import numpy as np

def sine(x):
    return np.sin(x)

def sawtooth(x):
    return (x + np.pi) / np.pi % 2 -1