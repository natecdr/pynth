from typing import Any

class FloatParameter:
    def __init__(self, value : float, range : tuple):
        self._value = value
        self._range = range
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = float(value)
        
    @property
    def range(self):
        return self._range
    
    