class FloatParameter:
    def __init__(self, value : float, range : tuple):
        self._base_value = value
        self._value = value
        self._range = range
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value : float):
        self._value = float(value)
        
    @property
    def base_value(self):
        return self._base_value
    
    @base_value.setter
    def base_value(self, value : float):
        self._base_value = float(value)
        self._value = float(value)
        
    @property
    def range(self):
        return self._range