import numpy as np
import matplotlib.pyplot as plt

def interpolate_linearly(wavetable, index_in_wavetable):
    lower_index = int(np.floor(index_in_wavetable))
    upper_index = (lower_index + 1) % wavetable.n_samples
    
    upper_index_weight = index_in_wavetable - lower_index
    lower_index_weight = 1 - upper_index_weight
    
    return wavetable[lower_index] * lower_index_weight + wavetable[upper_index] * upper_index_weight

def plot_waveform(waveform):
    phases = np.arange(0, 2*np.pi, 0.01)
    values = np.apply_along_axis(waveform, 0, phases)

    plt.plot(phases, values)        
    plt.show()