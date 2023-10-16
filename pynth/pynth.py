from pynth.oscillator import Oscillator
from pynth.envelope import Envelope
from pynth.filter import Filter
import pynth.waveforms as waveforms
from pynth.utils import *
from pynth.parameter_types import FloatParameter
from pynth.voice import Voice

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
        
        self.ampEnv = Envelope(self, links=[self.osc1.volume, self.osc2.volume])
        
        self.modEnv1 = Envelope(self)
        self.modEnv2 = Envelope(self)
        
        self.frequency = FloatParameter(440, (110, 4181))
        
        self.voice = None
        
        # for _ in range(10):
        #     self.play_sample(next(self.osc1.chunks()))
        
    def play(self, duration):
        self.voice = Voice(self, self.frequency)
        
        signal = np.zeros(int(duration*self.SAMPLE_RATE))
        for i in range(len(signal)):
            signal[i] = next(self.voice)
            
        # signal = self.voice.render_signal(duration)
        
        sd.play(signal, self.SAMPLE_RATE)
        
    def play_sample(self, sample):
        sd.play(sample, self.SAMPLE_RATE)
        # sd.wait()
        
    def stop_playing(self):
        sd.stop()
        self.voice.clear_osc_voices()
        self.voice = None
        
    def plot_waves(self, osc1_signal, osc2_signal):
        def my_fft(sig):
            n = sig.shape[0]
            t = 1. / self.SAMPLE_RATE
            # calculate fft amplitudes
            yf = fft(sig, n)
            # calculate fft frequencies
            xf = fftfreq(n, t)[:n//2]
            return xf, yf
        
        def plot_fft(ax, sig, rng=(0, 20000)):
            xf, yf = my_fft(sig)
            n = sig.shape[0]
            ax.plot(xf, 2.0/n * np.abs(yf[:n//2]))
            ax.set_xlabel("Frequency [Hz]")
            ax.set_ylabel("Amplitude")
            ax.set_xlim(*rng)
            ax.grid()
        
        till = 100
        fig = plt.figure()
        ax = fig.subplot_mosaic("""AD
                                   BE
                                   CF
                                   """)
        
        ax["A"].plot(osc1_signal[:till])
        ax["B"].plot(osc2_signal[:till])
        ax["C"].plot((osc1_signal + osc2_signal)[:till])
        
        plot_fft(ax["D"], osc1_signal)
        plot_fft(ax["E"], osc2_signal)
        plot_fft(ax["F"], osc1_signal + osc2_signal)
        plt.show()    
        