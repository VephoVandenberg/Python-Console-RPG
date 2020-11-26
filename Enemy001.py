from random import randrange

class Enemy():
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health

    def __str__(self):
        rep = "\t", self.name + "\nDamage:", self.damage + "\nHealth:", self.health
        return rep

    def attack(self, me):
        num = 15 - int(me.dexterity * 0.5)
        if num < 1:
            num = 3
        chance = randrange(1, num)
        trunk_of_health = me.health
        if chance == 1 or chance == 2 or chance == 3:
            me.health = 1000
            me.health -= self.damage
            me.health = trunk_of_health
        else:
            me.health -= self.damage
            if me.health < 0:
                me.die()

    def die(self):
        print("Blahh!..kHaaa.Khaaa...KHaaaaaaaa.........")
