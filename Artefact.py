import random

class Artefact():
    def __init__(self, name):
        self.name = name
        self.weight = 1
        self.strength = random.randrange(10, 25)
        self.dexterity = random.randrange(10, 25)
        self.flag = 0
        self.price = self.dexterity + self.strength * 3

    def activate_the_artefact(self, me):
        if self.flag == 0:
            me.strength += self.strength
            me.dexterity += self.dexterity
            self.flag += 1
        elif self not in me.inventory:
            print("This artefact is not in inventory")
        else:
            print("You can't use this artefact")
