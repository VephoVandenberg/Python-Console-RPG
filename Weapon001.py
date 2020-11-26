class Weapon():
    def __init__(self, name, damage, cunning, price, weight):
        self.damage = damage
        self.cunning = cunning
        self.name = name
        self.price = price
        self.weight = weight
        self.__limitation_of_cunning = self.weight

    def __str__(self):
        rep = "\t",self.name + "\nDamage:", self.damage + "\nCunning:", self.cunning
        return rep

    def fix_the_weapon(self, cunning):
        self.cunning = cunning

    def upgrade_the_weapon(self, more_cunning, more_damage):
        self.cunning += more_cunning
        self.damage += more_damage