import random
from Weapon001 import Weapon
from Artefact import Artefact
from Coat import Coat

class City():
    number_of_cities = 0
    def __init__(self, name):
        self.name = name
        self.blacksmith_inventory = []
        self.doctor_inventory = []
        City.number_of_cities += 1
        self.mission_flag = 0
        self.my_number = City.number_of_cities
        self.blacksmith_mission = ""

    def forge_of_blacksmith(self,me):

        choice = None
        while choice != 4:
            print("""Hello my dear friend what do you want to do in forge:
                1 - To sell any weaponry from your bag
                2 - To create a weapon
                3 - To take a mission
                4 - To upgrade the weapon
                5 - To create a coat
                6 - To upgrade the coat
                7 - To complete the mission
                8 - Exit
                            """)
            choice = input("Print here your choice:")
            if choice == "1":
                n = 0
                print("Weaponry")
                for thing in me.inventory:
                    if type(thing) == Weapon or type(thing) == Coat:
                        n += 1
                        print("\t%s - %s"%(n, thing.name))
                another_choice = input("Print here your choice")
                for num in range(len(me.inventory)):
                    if int(another_choice) - 1 == num:
                        me.throw_out_of_inventory(me.inventory[num - 1].name)
                        me.money += me.inventory[num].price


            elif choice == "2":
                name = input("Print here the name of your weapon")
                damage = int(input("What damage you would like to have in your weapon:"))
                cunning = int(input("How firm you want to do it"))
                price = (damage + cunning) * 3 * 0.75
                if price > me.money:
                    print("Sorry I can't buy it.")
                else:
                    print("Here is your weapon",me.name)
                    new_weapon = Weapon(name,damage,cunning,price,random.randrange(3,6))
                    me.add_to_inventory(new_weapon)
                    me.money -= price

            elif choice == "3":
                if self.my_number == 1:
                    for row in open("Blacksmith_mission_with_metal.txt"):
                        print(row, end="")
                    me.missions.append("Blacksmith_mission_with_metal")
                    self.blacksmith_mission = "Blacksmith_mission_with_metal"
                elif self.my_number == 2:
                    for row in open("Blacksmith_mission_with_tools.txt"):
                        print(row, end="")
                    me.missions.append("Blacksmith_mission_with_tools")
                    self.blacksmith_mission = "Blacksmith_mission_with_tools"
                else:
                    print("I haven't got any mission for you")

            elif choice == "4":
                print("Which of your weapon you want to upgrade:")
                n = 1
                for thing in range(len(me.inventory)):
                    if type(me.inventory[thing]) == Weapon:
                        print(n, "-", me.inventory[thing].name,
                              ":\n\tdamage - ", me.inventory[thing].damage,
                              "\n\tcunning - ", me.inventory[thing].cunning)
                        n += 1
                another_choice = input("Print here your choice:")
                if int(another_choice) - 1 in range(len(me.inventory)):
                    price = int(me.inventory[int(another_choice) - 1].price / 2.5)
                    if price <= me.money:
                        me.inventory[int(another_choice)].upgrade_the_weapon(15,10)
                    else:
                        print("Sorry I can't buy it")

            elif choice == "5":
                name_of_the_coat = input("Print here the name of your coat")
                cunning_of_your_coat = input("Print here the cunning of your coat:")
                price = int(float(cunning_of_your_coat*3)*0.75)
                if price > me.money:
                    print("Sorry I can't buy it.")
                else:
                    new_coat = Coat(name_of_the_coat, cunning_of_your_coat, price, int(cunning_of_your_coat / 3.5))
                    me.add_to_inventory(new_coat)
                    me.money -= price

            elif choice == "6":
                print("Which of your coat you want to upgrade:")
                n = 1
                for thing in range(len(me.inventory)):
                    if type(me.inventory[thing]) == Coat:
                        print(n, "-", me.inventory[thing].name,
                              ":\n\tcunning - ", me.inventory[thing].cunning)
                    n += 1
                another_choice = input("Print here your choice:")
                if int(another_choice) - 1 in range(len(me.inventory)):
                    price = int(me.inventory[int(another_choice) - 1].price / 2.5)
                    if price <= me.money:
                        me.inventory[int(another_choice)].upgrade_the_coat(20)
                    else:
                        print("Sorry I can't buy it.")

            elif choice == "7":
                for object in me.inventory:
                    if self.number_of_cities == 1:
                        if object.name == "Black metal":
                            if self.mission_flag == 1:
                                print("Thank you", me.name)
                            else:
                                me.inventory.throw_out_of_the_inventory(object)
                                me.money += 500
                                me.inventory.add_to_inventory(Weapon("Elvish sword", 150, 180, 250, 3))
                        else:
                            print("You didn't complete your mission"
                                  )
                    elif self.number_of_cities == 2:
                        if object.name == "Tools":
                            if self.mission_flag == 1:
                                print("Thank you", me.name)
                            else:
                                me.inventory.throw_out_of_the_inventory(object)
                                me.money += 1000
                                me.inventory.add_to_inventory(Coat("Elvish black coats",300))
                        else:
                            print("You didn't complete your mission")

            elif choice == "8":
                break

            else:
                print("There is no such command")
                continue

    def doctor(self, me):
        choice = None
        while choice != 4:
            print("""
                1 - To heal yourself
                2 - To sell artefacts
                3 - To exit
             """)
            choice = input("Print here your choice:")
            if choice == "1":
                print("The price of healing is 45.C.")
                a = input("Do you have so much Y/N:")
                if a == "y" or a == "y".upper():
                    me.health = me.limitation_of_health
                    me.money -= 45
                else:
                    n = int(input("So how much can you give for your healing:"))
                    if n > me.money:
                        print("Sorry,but you haven't got so much.")
                    else:
                        me.health += n * 0.55

            elif choice == "2":
                n = 1
                for thing in me.inventory:
                    if type(thing) == Artefact:
                        print(n,"-",thing.name)
                    n += 1
                another_choice = input("Print here your choice:")
                if int(another_choice) in range(len(me.inventory)):
                    me.inventory.remove(me.inventory[int(another_choice)])
                    me.money += me.inventory[int(another_choice)].price
                else:
                    print("Sorry I can't buy it")

            elif choice == "3":
                break

            else:
                print("There is no such command")