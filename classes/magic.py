import random


class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generateDamage(self):
        magicdmglow = self.dmg - 10
        magicdmghigh = self.dmg + 10
        return random.randrange(magicdmglow, magicdmghigh)
