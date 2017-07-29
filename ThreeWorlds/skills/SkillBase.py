'''
Created on Jul 21, 2017

@author: Ranaar Araajakata
'''

from energy.EnergyBase import Energy

class Skill(object):
    def __init__(self, energyType , energyCost):
        if not issubclass(energyType.getEnergy(), Energy) and energyType.getEnergy() is not Energy:
            class IllegalEnergyTypeError(Exception): 
                pass
            
            raise IllegalEnergyTypeError()
        
        if energyCost <= 0:
            class InvalidEnergyCostError(Exception):
                pass
            
            raise InvalidEnergyCostError()
        
        self.energyType = energyType
        self.energyCost = energyCost
        
    def getCost(self):
        return self.energyCost
    
    def getCostType(self):
        return self.energyType
