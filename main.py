import random

from classes.game import Character
from classes.magic import Spell
from classes.inventory import Inventory

# Spells
iceBolt = Spell("Ice bolt", 12, 40, "Ice")
fireBolt = Spell("Fire bolt", 5, 15, "Fire")
earthBolt = Spell("Earth bolt", 26, 57, "Earth")
windBolt = Spell("Wind bolt", 1, 10, "Wind")
heal = Spell("Lesser Heal", 2, 10, "White")

# Items
smallPotion = Inventory("Small Potion", "potion", "Heals you for 25hp", 25)
potion = Inventory("Potion", "potion", "Heals you for 100hp", 100)
bomb = Inventory("Bomb", "attack", "Attacks enemy for 350hp", 200)

# Characters
hero = Character(500, 120, 50, 30, [iceBolt, fireBolt, earthBolt, windBolt, heal], [smallPotion, potion, bomb])
enemy = Character(450, 100, 20, 30, [windBolt, earthBolt], [smallPotion, bomb, potion])

running = True

while running:

    # ___PLAYER ACTION____
    print("+==================+")
    hero.chooseAction()
    select = input("Choose action:")
    index = int(select) - 1
    if index == 0:
        dmg = hero.generateDmgWithDefence()
        enemy.takeDamage(dmg)
        print("You hit you enemy for: ", dmg)
        print("His hp is: ", enemy.getHp())
    elif index == 1:
        hero.chooseMagic()
        magic_select = int(input("Choose magic:")) - 1
        spell = hero.magic[magic_select]
        magicdmg = spell.generateDamage()
        spellCost = spell.cost
        currentMana = hero.getMp()
        if spellCost > currentMana:
            print("Not enought mana")
            continue
        if spell.type == "White":
            hero.heal(spell.dmg)
            print("You healed for:", magicdmg, "Your hp:", hero.getHp())
        else:
            hero.takeManaCost(spellCost)
            enemy.takeDamage(magicdmg)
            print("You deal:", magicdmg, "magic dmg with:", spell, "Enemy hp is:", enemy.getHp())
    elif index == 2:
        hero.chooseItem()
        itemSelect = int(input("Choose item:")) - 1
        items = hero.item[itemSelect]
        if items.types == "attack":
            enemy.takeDamage(items.properties)
            print("You deal:", items.properties, "with:", items.name, "Enemy hp is:", enemy.getHp())
        elif items.types == "potion":
            hero.heal(items.properties)
            print("You healed for:", items.properties, "Your hp:", hero.getHp())

    # ______ENEMY TURN______
    enemy_select = random.randrange(0, 3)
    if enemy_select == 0:
        enemy_dmg = enemy.generateDmgWithDefence()
        hero.takeDamage(enemy_dmg)
        print("Enemy attack for:", enemy_dmg)
        print("Your hp is:", hero.getHp())
        print("Your mp is:", hero.getMp())
    elif enemy_select == 1:
        enemyMagicDmg = enemy.chooseEnemyMagic()
        print("Damage:", enemyMagicDmg)
        hero.takeDamage(enemyMagicDmg)
        print("Your hp is:", hero.getHp())
        print("Your mp is:", hero.getMp())

    elif enemy_select == 2:
        if enemy.getHp() < (enemy.getMaxHp()/2):
            itemSelect = random.randrange(0, len(enemy.item) - 2)
        else:
            itemSelect = len(enemy.item) - 1
        items = enemy.item[itemSelect]
        if items.types == "attack":
            hero.takeDamage(items.properties)
            print("Enemy deal:", items.properties, "with:", items.name, "Enemy hp is:", enemy.getHp())
        elif items.types == "potion":
            enemy.heal(items.properties)
            print("Enemy healed for:", items.properties, "Enemy hp:", enemy.getHp())



  # ____END GAME_____
    if enemy.getHp() == 0:
        print("You Win!")
        running = False
    elif hero.getHp() == 0:
        print("Enemy defeats you!")
        running = False
