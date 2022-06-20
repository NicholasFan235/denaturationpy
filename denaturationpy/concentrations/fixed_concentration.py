from ._concentration import DynamicConcentration, Concentration


class FixedConcentration(Concentration):
    def __init__(self, name:str, c0:float=0):
        self.c0 = c0
        super().__init__(name)

    def concentration(self, t, y):
        return self.c0

class FixedDynamicConcentration(Concentration):
    def __init__(self, name:str, c0:float=0):
        super().__init__(name, c0)
    
    def rhs(self, t:float, y, rhs):
        rhs[self.index] = 0
