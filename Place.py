import random
from Enemy001 import Enemy
import Weapon001
import Artefact
import Coat


def fight(me, enemys: list):
    print("Your enemies are:")
    for enemy in range(len(enemys)):
        print("\t\t" + str(enemy + 1), "-", enemys[enemy].name + ":health -", enemys[enemy].health, "damage -",
              enemys[enemy].damage, "")

    print("You:")
    print("\t\t" + me.name, "-", me.health)

    while True:
        if me.health < 1:
            break
        points_of_motion = 3
        print("\nYou have", points_of_motion, " points of motion")
        while points_of_motion > 0:
            print("""
        1 - Attack the enemy by your weapon
        2 - Use the artefact
        3 - Take on the coat
        4 - Take off the coat
             """)
            choice = input("Print here your choice:")
            if choice == "1":
                num = 0
                weapons = []
                print("You:\n""\t\t%s - health:%s\n---------------------------------------" % (me.name, me.health))
                print("Your enemies are:\n")
                for enemy in enemys:
                    num += 1
                    print("\t\t%s - %s:health - %s" % (num, enemy.name, enemy.health))
                print("---------------------------------------\nYour weapon:\n")
                for object in range(len(me.inventory)):
                    if type(me.inventory[object]) == Weapon001.Weapon:
                        print("\t   ", (object + 1), "-", me.inventory[object].name, ":damage - ",
                              me.inventory[object].damage)
                        weapons.append(me.inventory[object])
                print("---------------------------------------")
                try:
                    enemy_for_attack = int(input("Enemy:"))
                except ValueError or IndexError:
                    print("That's not integer or number is out of range od list.")
                    continue
                try:
                    weapon_for_killing = int(input("Weapon:"))
                except ValueError or IndexError:
                    print("That's not integer or number is out of range of list.")
                    continue
                me.attack(enemys[enemy_for_attack - 1], weapons[weapon_for_killing - 1])
                if enemys[enemy_for_attack - 1].health < 1:
                    enemys.remove(enemys[enemy_for_attack - 1])
                if len(enemys) == 0:
                    break
                points_of_motion -= 1

            elif choice == "2":
                num = 0
                artefacts = []
                for subject in me.inventory:
                    if type(subject) == Artefact.Artefact:
                        num += 1
                        print("%s - %s" % (num, subject.name))
                        artefacts.append(subject)
                print()
                choice = input("Print here your choice:")
                if len(artefacts) > int(choice) > 0:
                    artefacts[int(choice) - 1].activate_the_artefact(me)
                    points_of_motion -= 1
                else:
                    print("That's bad choice.")

            elif choice == "3":
                num = 0
                coats_of_armour = []
                for subject in me.inventory:
                    if type(subject) == Coat.Coat:
                        num += 1
                        print("%s - %s" % (num, subject.name))
                        coats_of_armour.append(subject)
                print()
                choice = input("Print here your choice:")
                if len(coats_of_armour) > int(choice) > 0:
                    coats_of_armour[int(choice) - 1].wear_the_coat(me)
                    points_of_motion -= 1
                else:
                    print("That's bad choice.")

            elif choice == "4":
                for coat in me.inventory:
                    if coat.name == me.worn_armour:
                        coat.take_off_the_coat(me)

            else:
                print("there is no such command.")
                continue
        if len(enemys) < 1:
            break

        for enemy in enemys:
            for subject in range(len(me.inventory) - 1):
                if type(me.inventory[subject]) == Coat.Coat:
                    if me.inventory[subject].name == me.worn_armour:
                        if me.inventory[subject].cunning < 1:
                            me.inventory[me.inventory[subject]].take_off_the_coat(me)
            enemy.attack(me)
            if me.health < 1:
                break

def create_the_coat():
    names = [""]

def create_the_weapon():
    names = ["Sword", "Axe", "Hammer",
             "Spear", "Heavy two-handed dual axe", "Sabre", "Baton",
             "Two-handed sword", "Two-handed Axe", "Two-handed hammer"]
    name = random.choice(names)
    damage = None
    cunning = None
    price = None
    weight = None
    if name == "Sword" or name == "Axe" or name == "Hammer":
        damage = random.randrange(45, 70)
        cunning = random.randrange(35, 60)
        price = random.randrange(70, 110)
        weight = random.randrange(3, 6)
    elif name == "Sabre" or name == "Baton":
        damage = random.randrange(30, 80)
        cunning = random.randrange(45, 50)
        price = random.randrange(60, 100)
        weight = random.randrange(3, 5)
    elif name == "Heavy two-handed axe" or name == "Two-handed sword" or name == "Two-handed Axe" or name == "Two-handed hammer":
        damage = random.randrange(80, 120)
        cunning = random.randrange(80, 110)
        price = random.randrange(100, 180)
        weight = random.randrange(7, 12)
    else:
        damage = random.randrange(45, 90)
        cunning = random.randrange(50, 100)
        price = random.randrange(80, 120)
        weight = random.randrange(1, 3)

    return Weapon001.Weapon(name, damage, cunning, price, weight)

def create_the_artefact():
    names = ["Ring of Venguir's protecter", "wizard's bracelet",
             "Ring of Levinor's king", "Vur's ring"]
    return Artefact.Artefact(random.choice(names))

class Place():
    Number_of_places = 0
    def __init__(self, name):
        self.name = name
        self.stages = 3
        self.flag = 0
        self.flag_of_mission = 0
        self.enemies = []
        self.trunk = []
        self.__making_enemies_in_place()
        self.__making_trunks_in_place()
        Place.Number_of_places += 1

    def walk_in_the_place(self, me):
        choice = None
        print("There are enemys at all stages.\nYou should kill them all")
        while True:
            for stage in range(self.stages):
                print("\t\t", stage + 1, "- stage")
            print("\t\t 4 - Exit from", self.name)
            choice = input("Where do you want to go:")
            if 4 >= int(choice) > 0:
                if choice == "4":
                    break
                if len(self.enemies[int(choice) - 1]) == 0:
                    print("There are nobody on this stage")
                    break
                else:
                    fight(me, self.enemies[int(choice) - 1])
                    if me.health < 1:
                        break
                    if self.flag == int(choice) and len(self.trunk) > 0:
                        print("There is a trunk ")
                        for object in range(len(self.trunk)):
                            print(object + 1, "-", object.name)
                        choice = input("Print here what do you want to take:")
                        if len(self.trunk) > choice > 0:
                            me.add_to_inventory(self.trunk[int(choice) - 1])
                            self.trunk.remove(self.trunk[int(choice) - 1])
                        else:
                            print("There is no such command")
            else:
                continue

    def __making_trunks_in_place(self):
        for i in range(5):
           n = random.randrange(1, 3)
           if n == 1:
                self.trunk.append(create_the_weapon())
           else:
               self.trunk.append(create_the_artefact())
        if Place.Number_of_places == 2:
           self.trunk.append(Artefact.Artefact("Black metal"))
        elif Place.Number_of_places == 5:
            self.trunk.append(Artefact.Artefact("Tools"))


    def __making_enemies_in_place(self):
        for group in range(self.stages):
            self.enemies.append([])
            for i in range(random.randrange(3, 10)):
                if self.name == "Cave":
                    self.enemies[group].append(random.choice([Enemy(random.choice(["Orc", "Goblin"]), random.randrange(15, 45), random.randrange(70, 110)),
                                               Enemy(random.choice(["Ogre", "Throll"]), random.randrange(35, 60), random.randrange(70, 110)),
                                               Enemy("Bandit", random.randrange(10, 30), random.randrange(70, 90)),
                                               Enemy("Spider", random.randrange(15, 60), random.randrange(10, 40))]))
                elif self.name == "Lost castle":
                    self.enemies[group].append(random.choice([Enemy(random.choice(["Devil's slave", "Demon"]), random.randrange(80, 120), random.randrange(90, 120)),
                                               Enemy("Undead knight", random.randrange(110, 140), random.randrange(120, 180)),
                                               Enemy("Skeleton", random.randrange(10, 30), random.randrange(25, 50)),
                                               Enemy("Spider",  random.randrange(15, 60), random.randrange(10, 40)),
                                               Enemy("Cult priest", random.randrange(10, 50), random.randrange(10, 50)),
                                               Enemy("Zombie", random.randrange(25, 50), random.randrange(10, 30))]))
                elif self.name == "Camp of Burglars and Slayers":
                    self.enemies[group].append(random.choice([Enemy(random.choice(["Bandit", "Thief"]), random.randrange(10, 30), random.randrange(70, 90)),
                                               Enemy("Housebraker", random.randrange(30, 60), random.randrange(45, 80)),
                                               Enemy("Deserter", random.randrange(50, 85), random.randrange(30, 70))]))
                elif self.name == "Dungeon":
                    self.enemies[group].append(random.choice([Enemy("Minotaur", random.randrange(110, 140), random.randrange(130, 190)),
                                               Enemy("Skeleton", random.randrange(10, 30), random.randrange(25, 50)),
                                               Enemy(random.choice(["Throll", "Ogre"]), random.randrange(35, 60), random.randrange(90, 150)),
                                               Enemy("Dragon", random.randrange(180, 300), random.randrange(250, 400)),
                                               Enemy("Spider", random.randrange(15, 60), random.randrange(10, 40)),
                                               Enemy("Minotaur's chief", random.randrange(125, 175), random.randrange(150, 210)),
                                               Enemy("Zombie", random.randrange(25, 50), random.randrange(10, 30))]))
                elif self.name == "Mountains":
                    self.enemies[group].append(random.choice([Enemy("Uaeig", random.randrange(120, 180), random.randrange(150, 250)),
                                               Enemy("Mountain bandit", random.randrange(10, 30), random.randrange(50, 90)),
                                               Enemy("Berserk", random.randrange(90, 150), random.randrange(50, 90))]))

