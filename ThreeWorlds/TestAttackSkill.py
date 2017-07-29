'''
Created on Jul 22, 2017

@author: Ranaar Araajakata
'''

from skills.SkillTypes import Heal, HealOverTime, Attack, AttackOverTime, Resistance, AreaOfEffect
from skills.SkillBase import Skill 

from energy.anma.AnmaEnergy import AnmaType
from energy.mulai.MulaiEnergy import MulaiType
from energy.iratta.IrattaEnergy import IrattaType

class BasicAttackSkill(Skill , Attack):
    def __init__(self):
        Skill.__init__(self, energyType=IrattaType.LEISTUNG, energyCost=30)
        Attack.__init__(self, damage=20)

class BasicResistanceSkill(Skill , Resistance):
    def __init__(self):
        Skill.__init__(self, energyType=AnmaType.EARTH, energyCost=20)
        Resistance.__init__(self, res=20 , res_types=[BasicAttackSkill])

class BasicHealSkill(Skill , Heal):
    def __init__(self):
        Skill.__init__(self, energyType=MulaiType.TALA, energyCost=10)
        Heal.__init__(self, heal=20)

class AdvAttackSkill(Skill , AttackOverTime, AreaOfEffect):
    def __init__(self):
        Skill.__init__(self, energyType=IrattaType.ANRUF, energyCost=10)
        AttackOverTime.__init__(self, damage=50, attack_time=60)
        AreaOfEffect.__init__(self, radius=50)

class AdvHealSkill(Skill , HealOverTime, AreaOfEffect):
    def __init__(self):
        Skill.__init__(self, energyType=MulaiType.SIRSA, energyCost=10)
        HealOverTime.__init__(self, heal=5, heal_time=120)
        AreaOfEffect.__init__(self, radius=200)

bas = BasicAttackSkill()
brs = BasicResistanceSkill()
bhs = BasicHealSkill()
aas = AdvAttackSkill()
ahs = AdvHealSkill()

print(type(bas).__name__)
print(bas.getCostType())
print(bas.getCost())
print(bas.getDamage())
print()

print(type(brs).__name__)
print(brs.getCostType())
print(brs.getCost())
print(brs.getResistance())
print(brs.getResistTypes())
print()

print(type(bhs).__name__)
print(bhs.getCostType())
print(bhs.getCost())
print(bhs.getHeal())
print()

print(type(aas).__name__)
print(aas.getCostType())
print(aas.getCost())
print(aas.getDamage())
print(aas.getAttackTime())
print(aas.getRange())
print()

print(type(ahs).__name__)
print(ahs.getCostType())
print(ahs.getCost())
print(ahs.getHeal())
print(ahs.getHealTime())
print(ahs.getRange())
print()
