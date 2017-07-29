'''
Created on Jul 18, 2017

@author: Ranaar Araajakata
'''

import numpy as np
from enum import Enum

class EnergyType():
    pass

class Energy(object):
    def __init__(self, growthFunc, types, fit=None , liquidity=1, doBalancing=True):
        if not issubclass(types, Enum) or not issubclass(types, EnergyType): 
            class IllegalElementType(Exception):
                pass
            
            raise IllegalElementType()
        
        self.__doBalancing = doBalancing
        self.__growthFunction = growthFunc
        self.__energy_types = types
        self.__size = len(types)
        self.__types = list(types)
        
        if self.__size == 0:
            class IllegalTypeCount(Exception):
                    def __init__(self , message):
                        super(IllegalTypeCount , self).__init__(message)
            
            raise IllegalTypeCount('{0} cannot have zero types of energy'.format(type(self).__name__))
        
        # current amount of energy
        self.ele_val = np.zeros((self.__size))
        self.__ele_ind = {}
        
        for i in types:
            if not isinstance(i, types):
                class IllegalElementError(Exception):
                    pass
                raise IllegalElementError()
            
            self.__ele_ind[i] = i.value - 1
            
        self.__fit = None
        
        if self.__doBalancing:
            if liquidity > 1 or liquidity <= 0:
                class IllegalLiquidityError(Exception):
                    pass
                
                raise IllegalLiquidityError()
            
            # how well one fits with each type of energy
            if(fit == None):
                self.__fit = np.random.rand((self.__size) , dtype=np.float64)
            elif isinstance(fit, np.ndarray):
                self.__fit = fit
            else:
                self.__fit = np.zeros((self.__size) , dtype=np.float64)
                for i in range(0 , self.__size):
                    self.__fit[i] = fit[i]
            
            # make the fit matrix a matrix of percentages
            self.__fit = self.__fit / self.__fit.sum()
            
            # Create element balancing matrix
            self.__balancingMatrix = np.zeros((self.__size, self.__size))
            
            for i in range(0 , self.__size):
                for j in range(0 , self.__size):
                    val = self.__fit.item(i) - self.__fit.item(j)
                    self.__balancingMatrix[i][j] = 1 / (1 + np.exp(-20 * val))
                    if i == j:
                        self.__balancingMatrix[i][j] = 0
                    
            for i in range(0 , self.__size):
                anma_sum = 0
                for j in range(0 , self.__size):
                    anma_sum -= self.__balancingMatrix.item((j, i))
                self.__balancingMatrix[i][i] = anma_sum
                
            self.__balancingMatrix *= liquidity
            
    def __str__(self):
        return self.getEnergyParts().__str__()
    
    def isBalancing(self):
        return self.__doBalancing
    
    def getFit(self):
        return None if self.__fit is None else self.__fit.copy()
    
    def getEnergyParts(self):
        parts = {}
        
        for i in self.__energy_types:
            val = self.getEnergy(i)
            parts[i] = val
        
        return parts
    
    def getEnergy(self , element=None):
        if element is None:
            return self.ele_val.sum()
        elif isinstance(element, self.__energy_types):
            return self.ele_val[self.__ele_ind[element]]
    
    def getElementType(self):
        return self.__energy_types
    
    def addEnergy(self , amount , element=None):
        if amount > 0:
            if element is not None and isinstance(element, self.__energy_types):
                self.ele_val[self.__ele_ind[element]] += amount
            elif self.__fit == None:
                class FunctionNotDefinedError(Exception):
                    def __init__(self , message):
                        super(FunctionNotDefinedError , self).__init__(message)
                
                raise FunctionNotDefinedError('add energy not defined for non-balancing energies without element specification')
            else:
                self.ele_val = self.ele_val + self.__fit * amount
    
    def update(self, dt):
        self.ele_val += self.__growthFunction(self.ele_val) * dt
        
        if self.__doBalancing:
            
            if np.isnan(self.ele_val.sum()):
                class NANError(Exception):
                    pass
                
                raise NANError()
            
            # do element-wise adjustment
            self.ele_val += self.__balancingMatrix.dot(self.ele_val) * dt
