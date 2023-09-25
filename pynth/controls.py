from tkinter import *

class Slider(Scale):
    def __init__(self, *args, synth_parameter, **kwargs):
        super().__init__(*args, **kwargs, from_ = max(synth_parameter.range), to=min(synth_parameter.range), command=self.onChange)
        self.synth_parameter = synth_parameter
        self.set(self.synth_parameter.value)
        
    def onChange(self, value):
        self.synth_parameter.value = value