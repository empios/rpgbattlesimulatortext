import random
from classes.inventory import Inventory

class Character:
    def __init__(self, hp, mp, atk, defence, magic, item):
        self.maxhp = hp
        # current
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atklow = atk - 20
        self.atkhigh = atk + 20
        self.defence = defence
        self.magic = magic
        self.action = ["Attack", "Magic", "Items"]
        self.item = item

    def getHp(self):
        return self.hp

    def getMaxHp(self):
        return self.maxhp

    def getMp(self):
        return self.mp

    def getMaxMp(self):
        return self.maxmp

    def generateDamage(self):
        return random.randrange(self.atklow, self.atkhigh)

    def generateDmgWithDefence(self):
        dmgdef = self.generateDamage()
        return dmgdef * (self.defence / 100)

    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
        return self.hp

    def takeManaCost(self, cost):
        self.mp -= cost

    def chooseAction(self):
        i = 1
        print("Actions")
        for item in self.action:
            print(str(i) + ":" + item)
            i += 1

    def chooseMagic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":" + spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def chooseEnemyMagic(self):
        magicSelect = random.randrange(0, len(self.magic))
        spell = self.magic[magicSelect]
        dmg = spell.generateDamage()
        print("ENEMY USE:", spell.name)
        if self.mp < spell.cost:
            self.chooseEnemyMagic()
        else:
            return dmg

    def chooseItem(self):
        i = 1
        print("Items")
        for items in self.item:
            if items.types == "attack":
                print(str(i) + ":" + items.name, "(attack:", str(items.properties) + ")")
                i += 1
            elif items.types == "potion":
                print(str(i) + ":" + items.name, "(heals:", str(items.properties) + ")")
                i += 1

    def heal(self, heal):
        self.hp += heal
        if self.hp >= self.maxhp:
            self.hp = self.maxhp
        return self.hp
