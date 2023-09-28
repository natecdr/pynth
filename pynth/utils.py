import numpy as np
import matplotlib.pyplot as plt

def plot_waveform(waveform):
    phases = np.arange(0, 2*np.pi, 0.01)
    values = np.apply_along_axis(waveform, 0, phases)

    plt.plot(phases, values)        
    plt.show()