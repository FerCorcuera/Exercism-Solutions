import random
import math
class Character:
    def __init__(self):
        
        self.strength = (self.ability())
        self.dexterity = (self.ability())
        self.constitution = (self.ability())
        self.intelligence = (self.ability())
        self.wisdom = (self.ability())
        self.charisma = (self.ability())
        self.hitpoints = 10 + modifier(self.constitution)
        
    def ability(self):
        randoms = [random.randint(1,6) for x in range(4)]
        randoms.sort()
        randoms = randoms[1::]
        return sum(randoms)

def modifier(value):
    return math.floor((value - 10)/2)
