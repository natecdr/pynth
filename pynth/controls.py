from tkinter import *

class Slider(Scale):
    def __init__(self, *args, synth_parameter, **kwargs):
        if kwargs.get("orient") == VERTICAL:
            range_bottom = max(synth_parameter.range)
            range_top = min(synth_parameter.range)
        else:
            range_bottom = min(synth_parameter.range)
            range_top = max(synth_parameter.range)
            
        super().__init__(*args, **kwargs, from_ = range_bottom, to=range_top, command=self.onChange)
        self.synth_parameter = synth_parameter
        self.set(self.synth_parameter.value)
        
    def onChange(self, value):
        self.synth_parameter.value = value