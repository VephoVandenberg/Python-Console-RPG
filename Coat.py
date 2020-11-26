class Coat():
    def __init__(self, name, cunning):
        self.name = name
        self.cunning = cunning
        self.weight = cunning * 1.5
        self.flag = 0
        self.price = (cunning - self.weight) * 2.5

    def wear_the_coat(self, me):
        if self.flag == 0:
            me.health += self.cunning
            me.worn_armour = self.name
            self.flag += 1
        else:
            print("The", self.name, "is worn on")

    def take_off_the_coat(self, me):
        if self.flag == True:
            if self.cunning >= 0:
                self.cunning = 0
                me.health -= self.cunning
            me.inventory.remove(self)
            me.worn_armour = ""
            self.flag -= 1
        else:
            print("It's not worn on you.")

    def upgrade_the_coat(self, more_cunning):
        self.cunning += more_cunning
