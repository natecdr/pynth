from pynth.oscillator import Oscillator
from pynth.envelope import Envelope
from pynth.filter import Filter
import pynth.waveforms as waveforms
from pynth.utils import *
import sounddevice as sd
from scipy.fft import fft, fftfreq


class Pynth:
    BUFFER_SIZE = 1024
    SAMPLE_RATE = 48000
    
    def __init__(self):
        
        self.ampEnv = Envelope()
        self.filter = Filter()
        
        self.osc1 = Oscillator(self)
        self.osc2 = Oscillator(self)
        
        
    def play(self, f, time):
        osc1_signal = self.osc1.output_signal(f, time, self.SAMPLE_RATE)
        osc2_signal = self.osc2.output_signal(f, time, self.SAMPLE_RATE)
        
        till = 100
        fig = plt.figure()
        ax = fig.subplot_mosaic("""A
                                   B
                                   C""")
        
        ax["A"].plot(osc1_signal[:till])
        ax["B"].plot(osc2_signal[:till])
        ax["C"].plot((osc1_signal + osc2_signal)[:till])
        
        plt.show()
        
        self.plot_fft(osc1_signal)
        
        signal = osc1_signal + osc2_signal
        
        sd.play(signal, self.SAMPLE_RATE)
        sd.wait()
        
    def plot_fft(self, sig, rng=(0, 20000)):
        xf, yf = self.fft(sig)
        n = sig.shape[0]
        plt.plot(xf, 2.0/n * np.abs(yf[:n//2]))
        plt.xlabel("Frequency [Hz]")
        plt.ylabel("Amplitude")
        plt.title("FFT")
        plt.xlim(*rng)
        plt.grid()
        plt.show()
        
    def fft(self, sig):
        n = sig.shape[0]
        t = 1. / self.SAMPLE_RATE
        # calculate fft amplitudes
        yf = fft(sig, n)
        # calculate fft frequencies
        xf = fftfreq(n, t)[:n//2]
        return xf, yf