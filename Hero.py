from random import randrange

class Hero():
    def __init__(self, name):
        self.level = 1
        self.XP = 0
        self.name = name
        self.money = 100
        self.strength = 4
        self.worn_armour = ""
        self.dexterity = 3
        self.health = 100
        self.max_weight = 50
        self.missions = []
        self.inventory = []
        self.__limitation_of_health = 100
        self.damage = self.strength * 3
        self.__limitation_of_XP = 250
        self.__points_of_skill = 3

    def attack(self, enemy, weapon):
        chance = randrange(1, 30)
        trunk_of_health = enemy.health
        print("Take this,dirty bastard!!!")
        if chance == 11:
            enemy.health = 1000
            enemy.health -= weapon.damage + self.damage
            enemy.health = trunk_of_health
        else:
            enemy.health -= weapon.damage + self.damage
            weapon.cunning -= randrange(2,8)
            if enemy.health < 1:
                enemy.die()
                self.money += randrange(1, 25)
                self.XP += (0.75*(enemy.health + enemy.damage))*2
                if self.__limitation_of_XP <= self.XP:
                    self.__increase_of_level()

    def add_to_inventory(self, subject):
        weight = 0
        for object in self.inventory:
            weight += object.weight
        if weight + subject.weight > self.max_weight:
            print("Sorry you can't take anything")
        else:
            self.inventory.append(subject)

    def throw_out_of_inventory(self, subject):
        self.inventory.remove(subject)

    def die(self):
        print("Kha..khaaaaaaaaa...")

    def __increase_of_level(self):
        self.level += 1
        self.XP = 0
        self.__limitation_of_XP += 200
        self.__limitation_of_health += 20
        self.health = self.__limitation_of_health
        while self.__points_of_skill > 1:
            print("""What skill you want to make higher
                    1 - strength
                    2 - dextirity

            You have %s"""%(self.__points_of_skill))

            choice = input("\nPrint here your cohice:")
            if choice == "1":
                self.strength += 1
                self.__points_of_skill -= 1
            elif choice == "2":
                self.dexterity += 1
                self.__points_of_skill -= 1
            else:
                print("There is no such command")
                continue