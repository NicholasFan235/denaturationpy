from .concentrations._concentration import Concentration, DynamicConcentration
from scipy.integrate import solve_ivp
import numpy as np
import pandas as pd

class System:
    def __init__(self, temperature:float):
        self.temperature = temperature
        self._dynamic_concentrations = []
        self._concentrations = []
        self._n_equations = 0
        self.t = 0; self.y = None
    
    def add_concentration(self, concentration):
        assert isinstance(concentration, Concentration),\
            "concentration must be child of Concentration"
        if isinstance(concentration, DynamicConcentration):
            self._n_equations += concentration._bind(self._n_equations)
            self._dynamic_concentrations.append(concentration)
        elif isinstance(concentration, Concentration):
            self._concentrations.append(concentration)
        
    def add_concentrations(self, concentrations):
        for c in concentrations: self.add_concentration(c)
        
    def rhs(self, t:float, y):
        rhs = np.zeros_like(y)
        for c in self._dynamic_concentrations:
            c.rhs(t, y, rhs)
        return rhs
    
    def y0(self):
        y0 = np.zeros((self._n_equations))
        for c in self._dynamic_concentrations:
            c.y0(y0)
        return y0
    
    def solve(self, t_final, n_eval=1000, **kwargs):
        kwargs['t_eval'] = np.linspace(self.t, self.t+t_final, n_eval)
        sol = solve_ivp(self.rhs, [self.t, self.t+t_final], self.y0() if self.y is None else self.y, **kwargs)
        self.t += t_final
        self.y = sol.y[:, -1]

        y = np.zeros((sol.t.shape[0], self._n_equations + len(self._concentrations)))
        y[:, :self._n_equations] = sol.y.T
        for i, c in enumerate(self._concentrations):
            for j,t in enumerate(sol.t):
                y[j,self._n_equations+i] = c.concentration(t,None)

        self.sol = sol

        column_names = ['t']
        for c in self._dynamic_concentrations + self._concentrations: column_names += c.name()
        return pd.DataFrame(np.concatenate((sol.t.reshape(-1,1),y), axis=1), columns=column_names)

