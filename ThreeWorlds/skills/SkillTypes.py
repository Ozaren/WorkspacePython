'''
Created on Jul 24, 2017

@author: Ranaar Araajakata
'''
class AreaOfEffect(object):
    def __init__(self , radius, *args, **kwargs):
        self.__radius = radius
    
    def getRange(self):
        return self.__radius

class Summon(object):
    def __init__(self , summon_type , summon_time , summon_life_time, *args, **kwargs):
        self.__summon_type = summon_type
        self.__summon_time = summon_time
        self.__summon_life_time = summon_life_time
    
    def getSummonType(self):
        return self.__summon_type
    
    def getSummonTime(self):
        return self.__summon_time
    
    def getSummonLifeTime(self):
        return self.__summon_life_time
    
class Resistance(object):
    def __init__(self, res , res_types, *args, **kwargs):
        self.__res = res
        self.__res_types = tuple(res_types)
        
    def getResistance(self):
        return self.__res
    
    def getResistTypes(self):
        return self.__res_types
    
class Attack(object):
    def __init__(self, damage, *args, **kwargs):
        self.__damage = damage
        
    def getDamage(self):
        return self.__damage

class AttackOverTime(Attack):
    def __init__(self, damage , attack_time, *args, **kwargs):
        Attack.__init__(self, damage, *args, **kwargs)
        self.__attack_time = attack_time
        
    def getAttackTime(self):
        return self.__attack_time
    
class Heal(object):
    def __init__(self , heal, *args, **kwargs):
        self.__heal = heal
        
    def getHeal(self):
        return self.__heal

class HealOverTime(Heal):
    def __init__(self, heal , heal_time, *args, **kwargs):
        Heal.__init__(self, heal, *args, **kwargs) 
        self.__heal_time = heal_time
        
    def getHealTime(self):
        return self.__heal_time