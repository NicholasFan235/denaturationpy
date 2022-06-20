import numpy as np
from ._concentration import DynamicConcentration, Concentration
from scipy.constants import gas_constant

class EquilibriumUnfoldingConcentration(DynamicConcentration):
    def __init__(self, name: str, system, ln_kf0:float, ln_ku0:float,
                 delta_Cp:float, beta_fold:float, tH_fold:float, tH_unfold:float, beta_t:float=None, kf_scaling:float=1):
        self._name = name
        self.ln_kf0 = ln_kf0
        self.ln_ku0 = ln_ku0
        self.t0 = 298.3
        self.delta_G0 = (ln_kf0-ln_ku0) * gas_constant * self.t0
        self.delta_Cp = delta_Cp
        self.beta_fold = beta_fold
        self.tH_fold = tH_fold
        self.tH_unfold = tH_unfold
        self.kf_scaling=kf_scaling
        self.denaturants = [] # [(concentration, mf, mu)]
        self.system = system
        self.beta_t = beta_t
        self.c0 = np.array([1,0])
    
    def set_initial(self, native, denatured):
        self.c0 = np.array([native, denatured])
    
    def name(self):
        return [f'{self._name}_native', f'{self._name}_denatured']

    def add_denaturant(self, concentration:Concentration, m_value:float, m_folding:float=None):
        if m_folding is None:
            assert self.beta_t is not None, "Require protein's Tanford Beta value or m_folding"
            m_folding = -m_value * self.beta_t
        self.denaturants.append((concentration, m_folding, m_value+m_folding))
    
    def ln_kf(self, t, y):
        return self.ln_kf0 + \
            self._temperature_contribution(self.system.temperature) + \
            self._denaturant_contribution(t, y, True)
    
    def ln_ku(self, t, y):
        return self.ln_ku0 + \
            self._temperature_contribution(self.system.temperature) + \
            self._denaturant_contribution(t, y, False)

    def _bind(self, index:int):
        self.index = index
        return 2
    
    def y0(self, y0):
        y0[self.index:self.index+2] = self.c0
    
    def rhs(self, t:float, y, rhs):
        kf = np.exp(self.ln_kf(t, y))
        ku = np.exp(self.ln_ku(t, y))
        rhs[self.index] = self.kf_scaling*kf*y[self.index+1] - ku*y[self.index]
        rhs[self.index+1] = ku*y[self.index] - self.kf_scaling*kf*y[self.index+1]

    def _temperature_contribution(self, temp:float, folding:bool=True):
        if folding:
            tH = self.tH_fold
            Cp = self.delta_Cp * self.beta_fold
        else:
            tH = self.tH_unfold
            Cp = self.delta_Cp * (1+self.beta_fold)
        return (1+Cp/gas_constant)*np.log(temp/self.t0) + \
            (Cp/gas_constant)*(1/temp - 1/self.t0)*tH
    
    def _denaturant_contribution(self, time:float, y, folding:bool=True):
        i = 1 if folding else 2
        contribution = 0
        for denaturant in self.denaturants:
            contribution -= denaturant[0].concentration(time, y)*denaturant[i] / (gas_constant * self.system.temperature)
        return contribution
