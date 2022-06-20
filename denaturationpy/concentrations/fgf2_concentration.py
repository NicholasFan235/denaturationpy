import numpy as np
from ._concentration import DynamicConcentration, Concentration
from scipy.constants import gas_constant, Boltzmann, Planck

class FGF2Concentration(DynamicConcentration):
    def __init__(self, name: str, system,
                 ln_kf0:float=-1.4, ln_ku0:float=-10.4,
                 delta_Cp:float=7160, beta_fold:float=-0.62, beta_unfold:float=0.38, 
                 tH_fold:float=315, tH_unfold=119,
                 agg_Ea:float=35600, agg_Tf:float=658.7,
                 beta_t:float=0.82, misfold_prob=0.5,
                 kf2_enthalpy:float=34000, kf2_entropy:float=-200):
        self._name = name
        self.ln_kf0 = ln_kf0
        self.ln_ku0 = ln_ku0
        self.t0 = 298.3
        self.delta_G0 = (ln_kf0-ln_ku0) * gas_constant * self.t0
        self.delta_Cp = delta_Cp; self.beta_fold = beta_fold; self.beta_unfold = beta_unfold
        self.tH_fold = tH_fold; self.tH_unfold = tH_unfold
        self.agg_Ea = agg_Ea; self.agg_Tf = agg_Tf
        self.denaturants = [] # [(concentration, mf, mu)]
        self.system = system
        self.beta_t = beta_t
        self.misfold_prob = misfold_prob
        self.kf2_enthalpy = kf2_enthalpy; self.kf2_entropy = kf2_entropy
        self.c0 = np.array([1,0,0,0])
    
    def set_initial(self, native, denatured:float=0, aggregated:float=0):
        self.c0 = np.array([native, denatured, 0, aggregated])
    
    def name(self):
        return [f'{self._name}_native', f'{self._name}_denatured', f'{self._name}_misfolded', f'{self._name}_aggregated']

    def add_denaturant(self, concentration:Concentration, m_value:float, m_folding:float=None):
        if m_folding is None:
            assert self.beta_t is not None, "Require protein's Tanford Beta value or m_folding"
            m_folding = -m_value * self.beta_t
        self.denaturants.append((concentration, m_folding, m_value+m_folding))
    
    def ln_kf(self, t, y):
        tH = self.tH_fold
        Cp = self.delta_Cp * self.beta_fold
        temp = self.system.temperature
        return self.ln_kf0 + (1+Cp/gas_constant)*np.log(temp/self.t0) + \
            (Cp/gas_constant)*(1/temp - 1/self.t0)*tH + \
            self._denaturant_contribution(t, y, True)
    
    def ln_kf2(self, t, y):
        temp = self.system.temperature
        return np.log(Boltzmann*temp/Planck) + self.kf2_entropy/gas_constant - self.kf2_enthalpy/(gas_constant*temp)
    
    def ln_ku(self, t, y):
        tH = self.tH_unfold
        Cp = self.delta_Cp * self.beta_unfold
        temp = self.system.temperature
        return self.ln_ku0 + \
            (1+Cp/gas_constant)*np.log(temp/self.t0) + \
            (Cp/gas_constant)*(1/temp - 1/self.t0)*tH + \
            self._denaturant_contribution(t, y, False)

    def _bind(self, index:int):
        self.index = index
        return 4
    
    def y0(self, y0):
        y0[self.index:self.index+4] = self.c0
    
    def rhs(self, t:float, y, rhs):
        kf = np.exp(self.ln_kf(t, y))
        ku = np.exp(self.ln_ku(t, y))
        kAgg = np.exp(self.agg_Ea/gas_constant * (1/self.agg_Tf - 1/self.system.temperature))
        kf2 = np.exp(self.ln_kf2(t, y))
        N,U,M,F = y[self.index:self.index+4]
        rhs[self.index] = (1-self.misfold_prob)*kf*U - ku*N + kf2*M
        rhs[self.index+1] = ku*(N+M)- (kf+kAgg)*U
        rhs[self.index+2] = self.misfold_prob*kf*U - (kf2+ku)*M
        rhs[self.index+3] = kAgg*U
        #print(f'M={self.misfold_prob*ku*kf/((ku+kf2)*(kf+ku))}')
    
    def _denaturant_contribution(self, time:float, y, folding:bool=True):
        i = 1 if folding else 2
        contribution = 0
        for denaturant in self.denaturants:
            contribution -= denaturant[0].concentration(time, y)*denaturant[i] / (gas_constant * self.system.temperature)
        return contribution
