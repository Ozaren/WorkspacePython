'''
Created on Jul 16, 2017

@author: Ranaar Araajakata
'''

from energy.EnergyBase import Energy
from enum import Enum
from enum import auto

class AnmaType(Enum):
    ELECTRICITY = auto()
    AIR = auto()
    WATER = auto()
    EARTH = auto()
    FROST = auto()
    PC1 = auto()
    HEAT = auto()
    PC2 = auto()
    
    def getEnergy(self):
        return Anma
    
class Anma(Energy):
    def growth_function(self , anma):
        return (1 - anma / self.max_anma) * (self.p0 + self.p1 * anma / self.max_anma)
    
    def __init__(self, max_anma , p0 , p1, fit=None , liquidity=1):
        super(Anma, self).__init__(self.growth_function , AnmaType , fit , liquidity)
        self.max_anma = max_anma
        self.p0 = p0
        self.p1 = p1
