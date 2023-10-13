from pynth.oscillator import Oscillator
from pynth.envelope import Envelope
from pynth.filter import Filter
import pynth.waveforms as waveforms
from pynth.utils import *
from pynth.parameter_types import FloatParameter
import sounddevice as sd
from scipy.fft import fft, fftfreq

import time

class Pynth:
    BUFFER_SIZE = 1024
    SAMPLE_RATE = 48000
    
    def __init__(self):
        # self.filter = Filter()
        
        self.osc1 = Oscillator(self)
        self.osc2 = Oscillator(self)
        
        self.ampEnv = Envelope(links=[self.osc1.volume])
        
        self.modEnv1 = Envelope()
        self.modEnv2 = Envelope()
        
        self.frequency = FloatParameter(440, (110, 4181))
        
        # for _ in range(10):
        #     self.play_sample(next(self.osc1.chunks()))
        
    def play(self, t):
        start = time.time()
        osc1_signal = self.osc1.output_signal(self.frequency.value, t)
        osc2_signal = self.osc2.output_signal(self.frequency.value, t)
        print("Time building sigs :", time.time()-start)
        
        
        signal = osc1_signal + osc2_signal
        
        # self.plot_waves(osc1_signal, osc2_signal)
        
        sd.play(signal, self.SAMPLE_RATE)
        # sd.wait()
        
    def play_sample(self, sample):
        sd.play(sample, self.SAMPLE_RATE)
        # sd.wait()
        
    def stop_playing(self):
        print("Stopped playing")
        sd.stop()
        
    def plot_waves(self, osc1_signal, osc2_signal):
        till = 100
        fig = plt.figure()
        ax = fig.subplot_mosaic("""AD
                                   BE
                                   CF
                                   """)
        
        ax["A"].plot(osc1_signal[:till])
        ax["B"].plot(osc2_signal[:till])
        ax["C"].plot((osc1_signal + osc2_signal)[:till])
        
        self.plot_fft(ax["D"], osc1_signal)
        self.plot_fft(ax["E"], osc2_signal)
        self.plot_fft(ax["F"], osc1_signal + osc2_signal)
        plt.show()    
    
    def plot_fft(self, ax, sig, rng=(0, 20000)):
        xf, yf = self.fft(sig)
        n = sig.shape[0]
        ax.plot(xf, 2.0/n * np.abs(yf[:n//2]))
        ax.set_xlabel("Frequency [Hz]")
        ax.set_ylabel("Amplitude")
        ax.set_xlim(*rng)
        ax.grid()
        
    def fft(self, sig):
        n = sig.shape[0]
        t = 1. / self.SAMPLE_RATE
        # calculate fft amplitudes
        yf = fft(sig, n)
        # calculate fft frequencies
        xf = fftfreq(n, t)[:n//2]
        return xf, yf