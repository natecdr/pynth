from tkinter import *
from tkdial import Dial
from pynth.pynth import Pynth
from pynth.controls import Slider

class PynthGUI(Tk):
    def __init__(self):
        super().__init__()
        
        self.synth = Pynth()
        
        self.title("Pynth")
        self.config(bg="gray")
        
        self.waveform_list = Variable(value=["sine", "saw"])
        
        #Oscillators & AmpEnv
        self.oscBox = self._createOscBox()
        self.osc1Box = self._createOsc1Box()
        self.osc2Box = self._createOsc2Box()
        self.ampEnvBox = self._createAmpEnvBox()
        
        #Filter, LFO & ModEnvs
        self.fxBox = self._createFxBox()
        self.filterBox = self._createFilterBox()
        self.LFOBox = self._createLFOBox()
        self.modEnv1Box = self._createModEnv1Box()
        self.modEnv2Box = self._createModEnv2Box()
        
        #Keyboard & master 
        self.keyBox = self._createKeyBox()
        
    #Oscillators & AmpEnv
    def _createOscBox(self):
        oscBox = Frame(self, width=1000, height=200)
        oscBox.grid(row=0, column=0)
        
        return oscBox
    
    def _createOsc1Box(self):
        osc1Box = Frame(self.oscBox, width = 300, height = 200, bg="purple", highlightbackground="black", highlightthickness=2)
        osc1Box.grid(row=0, column=1)
        
        title = Label(osc1Box, text="osc1")
        title.grid(row=0, column=0)
        
        def onWaveformChange(event):
            w = event.widget
            index = int(w.curselection()[0])
            self.synth.osc1.set_waveform(w.get(index))
        
        osc1Waveform = Listbox(osc1Box, listvariable=self.waveform_list, height=2, exportselection=False)
        osc1Waveform.bind("<<ListboxSelect>>", onWaveformChange)
        osc1Waveform.select_set(0)
        osc1Waveform.grid(row=1, column=0)
        
        osc1VolumeSlider = Slider(osc1Box, orient=VERTICAL, resolution=0.01, synth_parameter=self.synth.osc1.volume)
        osc1VolumeSlider.grid(row=1, column=1)
        
        osc1Box.grid_propagate(False)
        
        return osc1Box
        
    def _createOsc2Box(self):
        osc2Box = Frame(self.oscBox, width = 300, height = 200, bg="green", highlightbackground="black", highlightthickness=2)
        osc2Box.grid(row=0, column=3)
        
        title = Label(osc2Box, text="osc2")
        title.grid(row=0, column=0)
        
        def onWaveformChange(event):
            w = event.widget
            index = int(w.curselection()[0])
            self.synth.osc2.set_waveform(w.get(index))
        
        osc2Waveform = Listbox(osc2Box, listvariable=self.waveform_list, height=2, exportselection=False)
        osc2Waveform.bind("<<ListboxSelect>>", onWaveformChange)
        osc2Waveform.select_set(0)
        osc2Waveform.grid(row=1, column=0)
        
        osc2VolumeSlider = Slider(osc2Box, orient=VERTICAL, resolution=0.01, synth_parameter=self.synth.osc2.volume)
        osc2VolumeSlider.grid(row=1, column=1)
    
        osc2Box.grid_propagate(False)
            
        return osc2Box
    
    def _createAmpEnvBox(self):
        ampEnvBox = Frame(self.oscBox, width = 300, height = 200, bg="red", border=1, highlightbackground="black", highlightthickness=2)
        ampEnvBox.grid(row=0, column=2)
        
        title = Label(ampEnvBox, text="ampEnv")
        title.grid(row=0, column=0)
            
        attackSlider = Slider(ampEnvBox, orient=VERTICAL, resolution=0.01, synth_parameter=self.synth.ampEnv.attack)
        attackSlider.grid(row=2, column=0)
        attackLabel = Label(ampEnvBox, text="A")
        attackLabel.grid(row=3, column=0)
        
        decaySlider = Slider(ampEnvBox, orient=VERTICAL, resolution=0.01, synth_parameter=self.synth.ampEnv.decay)
        decaySlider.grid(row=2, column=1)
        decayLabel = Label(ampEnvBox, text="D")
        decayLabel.grid(row=3, column=1)
        
        sustainSlider = Slider(ampEnvBox, orient=VERTICAL, resolution=0.01, synth_parameter=self.synth.ampEnv.sustain)
        sustainSlider.grid(row=2, column=2)
        sustainLabel = Label(ampEnvBox, text="S")
        sustainLabel.grid(row=3, column=2)
        
        releaseSlider = Slider(ampEnvBox, orient=VERTICAL, resolution=0.01, synth_parameter=self.synth.ampEnv.release)
        releaseSlider.grid(row=2, column=3)
        releaseLabel = Label(ampEnvBox, text="R")
        releaseLabel.grid(row=3, column=3)
        
        ampEnvBox.grid_propagate(False)
        
        return ampEnvBox
                
    #Filter, LFO & ModEnvs
    def _createFxBox(self):
        fxBox = Frame(self, width=1000, height=200, highlightbackground="black", highlightthickness=2)
        fxBox.grid(row=1, column=0)
        
        return fxBox
    
    def _createFilterBox(self):
        filterBox = Frame(self.fxBox, width=200, height=200, bg="yellow", highlightbackground="black", highlightthickness=2)
        filterBox.grid(row=0, column = 0)
        
        cutoffSlider = Slider(filterBox, orient=HORIZONTAL, synth_parameter=self.synth.filter.cutoff_frequency)
        cutoffSlider.grid(row=1, column=0)
        cutoffLabel = Label(filterBox, text="cutoff")
        cutoffLabel.grid(row = 2, column=0)
        
        title = Label(filterBox, text="filter")
        title.grid(row=0, column=0)
        
        filterBox.grid_propagate(False)
        
        return filterBox
    
    def _createLFOBox(self):
        LFOBox = Frame(self.fxBox, width=200, height=200, bg="red", highlightbackground="black", highlightthickness=2)
        LFOBox.grid(row=0, column = 1)
        
        title = Label(LFOBox, text="LFO")
        title.grid(row=0, column=0)
        
        LFOBox.grid_propagate(False)
        
        return LFOBox
    
    def _createModEnv1Box(self):
        modEnv1Box = Frame(self.fxBox, width=200, height=200, bg="cyan", highlightbackground="black", highlightthickness=2)
        modEnv1Box.grid(row=0, column = 2)
        
        title = Label(modEnv1Box, text="modEnv1")
        title.grid(row=0, column=0)
        
        modEnv1Box.grid_propagate(False)
        
        return modEnv1Box
    
    def _createModEnv2Box(self):
        modEnv2Box = Frame(self.fxBox, width=200, height=200, bg="blue", highlightbackground="black", highlightthickness=2)
        modEnv2Box.grid(row=0, column = 3)
        
        title = Label(modEnv2Box, text="modEnv2")
        title.grid(row=0, column=0)
        
        modEnv2Box.grid_propagate(False)
        
        return modEnv2Box
    
    #Keyboard & master 
    def _createKeyBox(self):
        keyBox = Frame(self, width=800, height=100)
        keyBox.grid(row=2, column=0)
        
        title = Label(keyBox, text="keyboard")
        title.grid(row=0, column=0)
        
        self.pitchSlider = Scale(keyBox, from_= 110, to=4186, orient=HORIZONTAL)
        self.pitchSlider.set(440)
        self.pitchSlider.grid(row=2, column=0)
        
        playButton = Button(keyBox, text = "Play", command = self.play)
        playButton.grid(row=1, column=0, sticky="NSEw")
        
        keyBox.grid_propagate(False)
        
        return keyBox
    
    def play(self):
        self.synth.play(self.pitchSlider.get(), 1, 44100)
        
if __name__ == "__main__" :
    # run()
    pynthGUI = PynthGUI()
    pynthGUI.mainloop()