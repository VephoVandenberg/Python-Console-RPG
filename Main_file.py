import Hero, Enemy001, Weapon001, City, Artefact, Coat, random
from Place import Place, fight, create_the_artefact, create_the_weapon
MAIN_HERO = None
CITIES = []
PLACES = [[], [], [], [], []]
INNER_MAPS = {}
MAP_OF_PALCES = None

def random_fight(me):
    names_of_enemys = [["Orc", "Goblin", "Ogre", "Throll"], ["Bandit"],
                       ["Uaeig", "Donbetr"], ["Demon", "Devil's slave"],
                       ["Skeleton", "Undead Knight", "Zombie"]]
    num = random.randrange(1, 5)
    enemys = []

    for i in range(random.randrange(1, 5)):
        name = random.choice(names_of_enemys[num])
        damage = None
        health = None
        if name == "Orc" or name == "Goblin":
            damage = random.randrange(15, 40)
            health = random.randrange(70, 110)
        elif name == "Ogre" or name == "Throll":
            damage = random.randrange(35, 60)
            health = random.randrange(90, 150)
        elif name == "Bandit":
            damage = random.randrange(10, 30)
            health = random.randrange(70, 90)
        elif name == "Uaeig":
            damage = random.randrange(120, 180)
            health = random.randrange(150, 250)
        elif name == "Donbetr" or name == "Demon" or name == "Devil's slave":
            damage = random.randrange(80, 120)
            health = random.randrange(90, 110)
        elif name == "Undead Knight":
            damage = random.randrange(110, 140)
            health = random.randrange(120, 180)
        else:
            health = random.randrange(25, 50)
            damage = random.randrange(10, 30)
        enemys.append(Enemy001.Enemy(name, damage, health))

    fight(me, enemys)

def making_cities():
    names = ["Vargen", "Ahsergan", "Regnos", "Venguir", "Levinor"]
    for name in names:
        CITIES.append(City.City(name))

def making_places():
    for city in range(len(CITIES)):
        for num in range(4):
           PLACES[city].append(Place(random.choice(["Cave", "Lost castle",
                                                    "Camp of Burglars and Slayers",
                                                    "Dungeon",
                                                    "Mountains"])))

        INNER_MAPS[CITIES[city].name] = PLACES[city]

def main_function():
    while True:
        print("\t\tRPG")
        name = input("Please print here your name:")
        MAIN_HERO = Hero.Hero(name)
        print("You find yourself in a cave.\n"
              "You see dead and hardly injured people around.\n"
              "You don't know how did you get there,and who are these people around.\n"
              "Then you see the weapon behind the huge closed trunk.\n\n")
        weapon1 = create_the_weapon()
        print("That is a", weapon1.name, ",and of course you take it.")
        MAIN_HERO.add_to_inventory(weapon1)
        MAIN_HERO.add_to_inventory(create_the_artefact())
        print("You hear the steps and grouling.You realize that you need to get out of this place.")
        print("There are two goblins on your way.\nYou need to kill them.\n")
        fight(MAIN_HERO, [Enemy001.Enemy("Goblin", random.randint(15, 40), random.randint(25, 60)) for num in range(2)])
        while True:
            if MAIN_HERO.health <= 0:
                break
            print("\n\nIn which of this cities you want to go.\n")
            for city in range(len(CITIES)):
                print("\t\t", city + 1, "-", CITIES[city].name)
            choice = input("Print here your choice:")
            if not 0 < int(choice) < 5:
                continue
            if random.randint(1, 3) == 1:
                random_fight(MAIN_HERO)
                if MAIN_HERO.health < 1:
                    continue
            num = 1
            print("\t\t", num, "- ", CITIES[int(choice) - 1].name)
            for n in range(len(INNER_MAPS[CITIES[int(choice) - 1].name])):
                num += 1
                print("\t\t", num, "- ", INNER_MAPS[CITIES[int(choice) - 1].name][n].name)
            another_choice = input("Where do you want to go:")
            if another_choice == "1":
                print("""
            1 - Go to the blacksmith's forge
            2 - Go to the doctor
                    """)
                choice = input("Where do you want to go:")
                if choice == "1":
                    CITIES[0].forge_of_blacksmith(MAIN_HERO)
                elif choice == "2":
                    CITIES[0].doctor(MAIN_HERO)
                else:
                    print("There is no such command")
            elif type(INNER_MAPS[CITIES[int(choice) - 1].name][int(another_choice) - 2]) == Place:
                INNER_MAPS[CITIES[int(choice) - 1].name][int(another_choice) - 2].walk_in_the_place(MAIN_HERO)
                if MAIN_HERO.health < 1:
                    continue
            else:
                print("There is no such ")

        choice = input("Do you want to start again Y/N:").upper()
        while True:
            if choice == "Y" or choice == "N":
                break
            else:
                choice = input("Do you want to start again Y/N:").upper()
        if choice == "Y":
            continue
        else:
            break

making_cities()
making_places()
main_function()
