import adventureclass
import MonsterClasses
import random

#since the speed stat is the only one that directly effects combat we need to integrate it into the random generation
#since 7 is the max speed, we neeed to find the percentage, round it so that it becomes an int number and implement it into the dice
#example hobbits speed is 6/7= 85.... percent, when putting this in the dice we round down to 8/10 to keep int's
Roll = random.randint(1,10)

class HobbitCombat():
    def __init__(hobbitcombat):
        hobbitcombat.speed = 1-8
        


