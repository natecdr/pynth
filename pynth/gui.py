from tkinter import *
from tkdial import Dial

def run():
    window = Tk()
    window.title("Pynth")
    window.config(bg="gray")    
    
    #Oscillators & AmpEnv
    oscBox = createOscBox(window)
    
    osc1Box = createOsc1Box(oscBox)
    
    ampEnvBox = createAmpEnvBox(oscBox)
    
    osc2Box = createOsc2Box(oscBox)
    
    #Filter, LFO & ModEnvs
    fxBox = createFxBox(window)
    
    filterBox = createFilterBox(fxBox)
    
    LFOBox = createLFOBox(fxBox)

    modEnv1Box = createModEnv1Box(fxBox)
        
    modEnv2Box = createModEnv2Box(fxBox)
        
    #Keyboard & master 
    keyBox = createKeyBox(window)
    
    window.mainloop()

#Oscillators & AmpEnv
def createOscBox(window):
    oscBox = Frame(window, width=1000, height=200)
    oscBox.grid(row=0, column=0)
    
    return oscBox

def createOsc1Box(oscBox):
    osc1Box = Frame(oscBox, width = 300, height = 200, bg="purple", highlightbackground="black", highlightthickness=2)
    osc1Box.grid(row=0, column=1)
    
    osc1Title = Label(osc1Box, text="osc1")
    osc1Title.grid(row=0, column=0)
    
    osc1Box.grid_propagate(False)
    
    return osc1Box

def createOsc2Box(oscBox):
    osc2Box = Frame(oscBox, width = 300, height = 200, bg="green", highlightbackground="black", highlightthickness=2)
    osc2Box.grid(row=0, column=3)
    
    osc2Title = Label(osc2Box, text="osc2")
    osc2Title.grid(row=0, column=0)
    
    osc2Box.grid_propagate(False)
        
    return osc2Box

def createAmpEnvBox(oscBox):
    ampEnvBox = Frame(oscBox, width = 200, height = 200, bg="red", border=1, highlightbackground="black", highlightthickness=2)
    ampEnvBox.grid(row=0, column=2)
    
    return ampEnvBox

#Filter, LFO & ModEnvs
def createFxBox(window):
    fxBox = Frame(window, width=1000, height=200, highlightbackground="black", highlightthickness=2)
    fxBox.grid(row=1, column=0)
    
    return fxBox

def createFilterBox(fxBox):
    filterBox = Frame(fxBox, width=200, height=200, bg="yellow", highlightbackground="black", highlightthickness=2)
    filterBox.grid(row=0, column = 0)
    
    return filterBox

def createLFOBox(fxBox):
    LFOBox = Frame(fxBox, width=200, height=200, bg="red", highlightbackground="black", highlightthickness=2)
    LFOBox.grid(row=0, column = 1)
    
    return LFOBox

def createModEnv1Box(fxBox):
    modEnv1Box = Frame(fxBox, width=200, height=200, bg="cyan", highlightbackground="black", highlightthickness=2)
    modEnv1Box.grid(row=0, column = 2)
    
    return modEnv1Box

def createModEnv2Box(fxBox):
    modEnv2Box = Frame(fxBox, width=200, height=200, bg="blue", highlightbackground="black", highlightthickness=2)
    modEnv2Box.grid(row=0, column = 3)
    
    return modEnv2Box

#Keyboard & master 
def createKeyBox(window):
    keyBox = Frame(window, width=800, height=100)
    keyBox.grid(row=2, column=0)
    
    return keyBox

if __name__ == "__main__" :
    run()