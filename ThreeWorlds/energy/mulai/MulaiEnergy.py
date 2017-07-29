'''
Created on Jul 18, 2017

@author: Ranaar Araajakata
'''

from energy.EnergyBase import Energy
from enum import Enum
from enum import auto

class MulaiType(Enum):
    SIRSA = auto() # top
    TALA = auto() # bottom
    
    def getEnergy(self):
        return Mulai
    
class Mulai(Energy):
    '''
    classdocs
    '''
    
    def growth_function(self , mulai):
        return -self.decay_rate * mulai
    
    def __init__(self, decay_rate, __fit=None , __liquidity=1):
        super(Mulai, self).__init__(self.growth_function , MulaiType, doBalancing=False)
        self.decay_rate = decay_rate
