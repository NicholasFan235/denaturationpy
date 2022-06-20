from ._concentration import DynamicConcentration, Concentration
import numpy as np

class ExponentialConcentration(Concentration):
    def __init__(self, name:str, c0:float, k:float, c1:float=0):
        self.c0 = c0
        self.k = k
        self.c1 = c1
        super().__init__(name)
    
    def concentration(self, t:float, y):
        return self.c1 + self.c0 * np.exp(-self.k*t)

class ExponentialDynamicConcentration(DynamicConcentration):
    def __init__(self, name:str, k:float=0, c0:float=0):
        self.k = k
        super().__init__(name, c0)
    
    def rhs(self, t: float, y, rhs):
        rhs[self.index] = -self.k * y[self.index]
