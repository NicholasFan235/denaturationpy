
class Concentration:
    def __init__(self, name: str):
        self._name = name

    def concentration(self, t:float, y):
        raise NotImplementedError
    
    def name(self):
        return [self._name]

class DynamicConcentration(Concentration):
    def __init__(self, name: str, c0:float):
        self.c0 = c0
        super().__init__(name)
    
    def _bind(self, index:int):
        self.index = index
        return 1
    
    def rhs(self, t:float, y, rhs):
        raise NotImplementedError
    
    def y0(self, y0):
        y0[self.index] = self.c0

    def concentration(self, t:float, y):
        return y[self.index]
