'''
Created on Jul 18, 2017

@author: Ranaar Araajakata
'''

from energy.EnergyBase import Energy
from enum import Enum
from enum import auto

class IrattaType(Enum):
    LEISTUNG = auto()  # power
    ANRUF = auto()  # summon
    SINN = auto() # sense
    ANDERN = auto() # transform
    
    def getEnergy(self):
        return Iratta
    
class Iratta(Energy):
    '''
    classdocs
    '''
    
    def growth_function(self , iratta):
        return (1 - iratta / self.max_iratta) * self.production
    
    def __init__(self, max_iratta , production, fit=None , liquidity=1):
        super(Iratta, self).__init__(self.growth_function , IrattaType , fit , liquidity)
        self.max_iratta = max_iratta
        self.production = production
