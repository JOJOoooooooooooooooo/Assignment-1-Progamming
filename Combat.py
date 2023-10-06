import adventureclass
import MonsterClasses
import random


#since the speed stat is the only one that directly effects combat we need to integrate it into the random generation
#since 7 is the max speed, we neeed to find the percentage, round it so that it becomes an int number and implement it into the dice
#example hobbits speed is 6/7= 85.... percent, when putting this in the dice we round down to 8/10 to keep int's


mc1 = MonsterClasses.Goblin()

ch2 = adventureclass.Hobbit()

ch1 = adventureclass.Human()

ch3 = adventureclass.Dwarf()

ch4 = adventureclass.Elf()

Roll = random.randint(1,10)

print(Roll)

def HobbitCombat():
    Hobbitspeed = [1,2,3,4,5,6,7,8]
    if Roll in Hobbitspeed:
        print("Goblin is attacked by Hobbit, Goblin has " , mc1.health - ch2.attack )
    else:
        print(ch2.health - mc1.attack)

if mc1.health <= 0:
    break


HobbitCombat()

def HumanCombat():
    Humanspeed = [1,2,3,4,5,6]
    if Roll in Humanspeed:
        print("Goblin is attacked by Human", mc1.health - ch1.attack)
    else:
        print(ch1.health - mc1.health)

HumanCombat()

def DwarfCombat():
    Dwarfspeed = [1,2,3,4]
    if Roll in Dwarfspeed:
        print("Goblin is attacked by Dwarf", mc1.health - ch3.attack)
    else:
        print(ch3.health - mc1.attack)

DwarfCombat()


def ElfCombat():
    Elfspeed = [1,2,3,4,5,6,7]
    if Roll in Elfspeed:
        print("Goblin is attacked by Elf", mc1.health - ch4.attack)
    else:
        print(ch4.health - mc1.attack)

ElfCombat()






