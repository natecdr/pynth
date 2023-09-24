from tkinter import *
from tkdial import Dial
from pynth.pynth import Pynth

class PynthGUI(Tk):
    def __init__(self):
        super().__init__()
        
        self.pynth = Pynth()
        
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
            index = int(self.osc1Waveform.curselection()[0])
            self.pynth.osc1.set_waveform(self.osc1Waveform.get(index))
        
        self.osc1Waveform = Listbox(osc1Box, listvariable=self.waveform_list, height=2, exportselection=False)
        self.osc1Waveform.bind("<<ListboxSelect>>", onWaveformChange)
        self.osc1Waveform.grid(row=1, column=0)
        
        osc1Box.grid_propagate(False)
        
        return osc1Box
        
    def _createOsc2Box(self):
        osc2Box = Frame(self.oscBox, width = 300, height = 200, bg="green", highlightbackground="black", highlightthickness=2)
        osc2Box.grid(row=0, column=3)
        
        title = Label(osc2Box, text="osc2")
        title.grid(row=0, column=0)
        
        def onWaveformChange(event):
            index = int(self.osc2Waveform.curselection()[0])
            self.pynth.osc2.set_waveform(self.osc2Waveform.get(index))
        
        self.osc2Waveform = Listbox(osc2Box, listvariable=self.waveform_list, height=2, exportselection=False)
        self.osc2Waveform.bind("<<ListboxSelect>>", onWaveformChange)
        self.osc2Waveform.grid(row=1, column=0)
        
        osc2Box.grid_propagate(False)
            
        return osc2Box
    
    def _createAmpEnvBox(self):
        ampEnvBox = Frame(self.oscBox, width = 200, height = 200, bg="red", border=1, highlightbackground="black", highlightthickness=2)
        ampEnvBox.grid(row=0, column=2)
        
        title = Label(ampEnvBox, text="ampEnv")
        title.grid(row=0, column=0)
        
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
        self.pynth.play(self.pitchSlider.get(), 1, 44100)
        
    

# def run():
#     #Window setup
#     window = Tk()
#     window.title("Pynth")
#     window.config(bg="gray")    
    
#     #Oscillators & AmpEnv
#     oscBox = createOscBox(window)
    
#     osc1Box = createOsc1Box(oscBox)
    
#     ampEnvBox = createAmpEnvBox(oscBox)
    
#     osc2Box = createOsc2Box(oscBox)
    
#     #Filter, LFO & ModEnvs
#     fxBox = createFxBox(window)
    
#     filterBox = createFilterBox(fxBox)
    
#     LFOBox = createLFOBox(fxBox)

#     modEnv1Box = createModEnv1Box(fxBox)
        
#     modEnv2Box = createModEnv2Box(fxBox)
        
#     #Keyboard & master 
#     keyBox = createKeyBox(window)
    
#     #Mainloop
#     window.mainloop()

#Oscillators & AmpEnv
# def createOscBox(window):
#     oscBox = Frame(window, width=1000, height=200)
#     oscBox.grid(row=0, column=0)
    
#     return oscBox

# def createOsc1Box(oscBox):
#     osc1Box = Frame(oscBox, width = 300, height = 200, bg="purple", highlightbackground="black", highlightthickness=2)
#     osc1Box.grid(row=0, column=1)
    
#     title = Label(osc1Box, text="osc1")
#     title.grid(row=0, column=0)
    
#     osc1Box.grid_propagate(False)
    
#     return osc1Box

# def createOsc2Box(oscBox):
#     osc2Box = Frame(oscBox, width = 300, height = 200, bg="green", highlightbackground="black", highlightthickness=2)
#     osc2Box.grid(row=0, column=3)
    
#     title = Label(osc2Box, text="osc2")
#     title.grid(row=0, column=0)
    
#     osc2Box.grid_propagate(False)
        
#     return osc2Box

# def createAmpEnvBox(oscBox):
#     ampEnvBox = Frame(oscBox, width = 200, height = 200, bg="red", border=1, highlightbackground="black", highlightthickness=2)
#     ampEnvBox.grid(row=0, column=2)
    
#     title = Label(ampEnvBox, text="ampEnv")
#     title.grid(row=0, column=0)
    
#     ampEnvBox.grid_propagate(False)
    
#     return ampEnvBox

#Filter, LFO & ModEnvs
# def createFxBox(window):
#     fxBox = Frame(window, width=1000, height=200, highlightbackground="black", highlightthickness=2)
#     fxBox.grid(row=1, column=0)
    
#     return fxBox

# def createFilterBox(fxBox):
#     filterBox = Frame(fxBox, width=200, height=200, bg="yellow", highlightbackground="black", highlightthickness=2)
#     filterBox.grid(row=0, column = 0)
    
#     title = Label(filterBox, text="filter")
#     title.grid(row=0, column=0)
    
#     filterBox.grid_propagate(False)
    
#     return filterBox

# def createLFOBox(fxBox):
#     LFOBox = Frame(fxBox, width=200, height=200, bg="red", highlightbackground="black", highlightthickness=2)
#     LFOBox.grid(row=0, column = 1)
    
#     title = Label(LFOBox, text="LFO")
#     title.grid(row=0, column=0)
    
#     LFOBox.grid_propagate(False)
    
#     return LFOBox

# def createModEnv1Box(fxBox):
#     modEnv1Box = Frame(fxBox, width=200, height=200, bg="cyan", highlightbackground="black", highlightthickness=2)
#     modEnv1Box.grid(row=0, column = 2)
    
#     title = Label(modEnv1Box, text="modEnv1")
#     title.grid(row=0, column=0)
    
#     modEnv1Box.grid_propagate(False)
    
#     return modEnv1Box

# def createModEnv2Box(fxBox):
#     modEnv2Box = Frame(fxBox, width=200, height=200, bg="blue", highlightbackground="black", highlightthickness=2)
#     modEnv2Box.grid(row=0, column = 3)
    
#     title = Label(modEnv2Box, text="modEnv2")
#     title.grid(row=0, column=0)
    
#     modEnv2Box.grid_propagate(False)
    
#     return modEnv2Box

#Keyboard & master 
def createKeyBox(window):
    keyBox = Frame(window, width=800, height=100)
    keyBox.grid(row=2, column=0)
    
    title = Label(keyBox, text="keyboard")
    title.grid(row=0, column=0)
    
    pitchSlider = Scale(keyBox, from_= 110, to=4186, orient=HORIZONTAL)
    pitchSlider.grid(row=2, column=0)
    
    def playCallback():
        pynth.play(pitchSlider.get(), 1, 44100)
    
    playButton = Button(keyBox, text = "Play", command = playCallback)
    playButton.grid(row=1, column=0, sticky="NSEw")
    
    keyBox.grid_propagate(False)
    
    return keyBox

if __name__ == "__main__" :
    # run()
    pynthGUI = PynthGUI()
    pynthGUI.mainloop()