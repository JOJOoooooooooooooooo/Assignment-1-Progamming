import adventureclass
import MonsterClasses
import random



class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   



#Game title
print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| --------------------- |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("><><><><><>><><><><><><><><><><><><| WELCOME TO THE HOPPIT |><><><><><><><><><><><><><><><><><><")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| --------------------- |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
print("                                            ,'\   |\\")
print("                                           / /.:  ;;")
print("                                          / :'|| //")
print("                                         (| | ||;'")
print("                                         / ||,;'-.._")
print("                                        : ,;,`';:.--`")
print("                                        |:|'`-(\\")
print("                                        ::: \-'\`'")
print("                                         \\\ \,-`.")
print("                                          `'\ `.,-`-._      ,-._")
print("                                   ,-.       \  `.,-' `-.  / ,..`.")
print("                                  / ,.`.      `.  \ _.-' \',: ``\ \ ")
print("                                 / / :..`-'''``-)  `.   _.:''  ''\ \ ")
print("                                : :  '' `-..''`/    |-''  |''  '' \ \ ")
print("                                | |  ''   ''  :     |__..-;''  ''  : :")
print("                                | |  ''   ''  |     ;    / ''  ''  | |")
print("                                | |  ''   ''  ;    /--../_ ''_ '' _| |")
print("                                | |  ''  _;:_/    :._  /-.'',-.'',-. |")
print("                                : :  '',;'`;/     |_ ,(   `'   `'   \|")
print("                                 \ \  \(   /\     :,'  \ ")
print("                                  \ \.'/  : /    ,)    /")
print("                                   \ ':   ':    / \   :")
print("                                    `.\    :   :\  \  |")
print("                                            \  | `. \ |..-_")
print("                                             ) |.  `/___-.-`")
print("                                               ,'  -.'.  `. `'        _,)")
print("                                               \'\(`.\ `._ `-..___..-',')")
print("                                                  `'      ``-..___..-'")
print("")
print("")

input("--------------------------------Press (enter) to enter the world--------------------------------\n\n\n")
input("                            After a dailogue press enter to move on.\n\n\n")

#Asking user for player name
input("Unknown Voice: Hey you down there, you alright?")
input("You: Huh?.....What.....?")
input("Unknown Voice: Yooo-hooo, whats your name buddy?\n")

playername = input("(Enter a username):")

#Asking user for their selected class
input("\nYou: I'm " + playername + "...Who are you?")
input("Unknown Voice: Ohh well well well, Iv'e been looking for you my friend. You can call me JOJO!")
input(playername +": Ah I see, well JOJO how can I help you?")
input("JOJO: Straight to the point I see hahaha, no matter. I was just wondering, what clan do you hail from by the way?")
print("\n\n")



x = 0

while x == 0 :

    MyclassShell = input("Select a class to play as by entering the number correspon ding with the class.\n(1) - Human\n(2) - Hobbit\n(3) - Dwarf\n(4) - Elf\n:")

    if MyclassShell == "1":
        x = x + 1
        input("JOJO: ahh yes... The will of humans are strong, just as I had hoped!")
        Myclass = adventureclass.Human()


    elif MyclassShell == "2":
        x = x + 1
        input("JOJO: Splendid! the Hobbits unwavering spirit makes for the perfect companion, just as I had hoped!")
        Myclass = adventureclass.Hobbit()

    elif MyclassShell == "3":
        x = x + 1
        input("JOJO: Splendid! The strength of dwarves are unrivaled, In that case im sure this journey will serve you well!")
        Myclass = adventureclass.Dwarf()
    
    elif MyclassShell == "4":
        x = x + 1
        input("JOJO: The nobility and inteligence of the Elves are exactly what I'm looking for!")
        Myclass = adventureclass.Elf()

    else:
        x = 0
        print("\n\nInvalid input, try again.\n\n")



input(playername + ": I dont understand, what's going on?")
input("JOJO: Dwarves from a long forgotten culture have come seeking my aid, and I have thought of no one better but you " + playername + " to join me on this quest!")
input(playername + ": but why me? and what would I be helping with?")
input("JOJO: Hahaha....All in due time my friend")
input(playername + ": ...")
input("JOJO: Your mind should first be trying to piece together what you're doing in a cave on your lonesome")
input(playername + ": *now that he meantions it... what am I doing here? all I remember is being called from my home then hitting my head...*")
input("JOJO: Yooo-hooo, dont get too lost in thought. Take this and make your way back to your house, you will have some surprise visitors waiting to explain it all, I will meet you there")
input("                 ><><><><><>><><><><><><><><><><><><| DAGGER AQUIRED |><><><><><><><><><><><><><><><><><><")
input(playername + ": ...")
print("")
print("")
print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| --------------------- |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" ><><><><><>><><><><><><><><><><><><| TWO HOURS LATER |><><><><><><><><><><><><><><><><><><            ")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| --------------------- |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
input(playername + ": ...I wonder why JOJO handed me a dagger to get back home, its not like him to be overprotective in such a peaceful place...")
input("Unkown Voice: Lost are you.... how about handing me all your shillings and maybe I can find a place for you to sleep here...")
input(playername + ": A GOBLIN!. And this far from their home too!?")

print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| --------------------- |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("><><><><><>><><><><><><><><><><><><| GOBLIN ENCOUNTER!!!!!! |><><><><><><><><><><><><><><><><><><")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| --------------------- |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
print("                                              ,      , ")
print("                                             /(.-""-.)\ ")
print("                                         |\  \/      \/  /| ")
print("                                         | \ / =.  .= \ / | ")
print("                                         \( \   o\/o   / )/ ")
print("                                          \_, '-/  \-' ,_/ ")
print("                                            /   \__/   \ ")
print("                                            \ \__/\__/ / ")
print("                                          ___\ \|--|/ /___ ")
print("                                        /`    \      /    `\ ")
print("                                       /       '----'       \ ")
print("")
print("")

Goblin = MonsterClasses.Goblin()

input("God: You have now entered combat with a GOBLIN, depending on the class you have chosen, your attack, health and speed stats will differ. Since you have chosen " + color.BOLD + str(Myclass.name) + color.END + " your attack stat is, " + color.BOLD + str(Myclass.attack) + color.END)
input("your health stat is, " + color.BOLD + str(Myclass.health) + color.END + " and your speed stat is, " + color.BOLD + str(Myclass.speed) + color.END)

print("")
print("                                                  STATS                ")
print("                                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                                     |      " + color.BOLD + str(playername) + color.END + " Versus " + color.BOLD + str(Goblin.name) + color.END + "      |")
print("                                     ---------------|---------------")
print("                              Health: " + color.BOLD + str(Myclass.health) + color.END +   "             |           " + color.BOLD + str(Goblin.health) + color.END)
print("                                      --------------|--------------")
print("                              Attack: " + color.BOLD + str(Myclass.attack) + color.END +  "             |           " + color.BOLD + str(Goblin.attack) + color.END)
print("                                      --------------|------------ ")
print("                              Speed:  "  + color.BOLD + str(Myclass.speed) + color.END +   "             |           " + color.BOLD + str(Goblin.speed) + color.END)

print("")

input("God: to engage in combat you must roll the dice, as you can see, since your speed is greater than the goblins that means you get to roll the dice first! If the dice rolls any number between 1 to your speed, you will then get to attack")
input("The first combatant to reach health that is 0 or less will lose")
input("God: Try it out!")

Roll = random.randint(1,10)

input(" Press Enter to Roll Dice ")

print("The Dice lands on... " + color.BOLD + str(Roll) + color.END)

while Myclass.health > 0 and Goblin.health > 0: 
    if Roll <= Myclass.speed:
        print("Good job! in this case you would take the turn and attack")
        damage = Myclass.attack
        print(playername + " Attacks!")
        Goblin.health -= damage
        print("Goblin health:", Goblin.health)
        if Goblin.health <= 0:
            input("You have slain the enemy")
        elif Goblin.health > 0:
            Roll = random.randint(1,10)
            input(" Press Enter to Roll Dice ")
            input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
    else:
        print("uh oh it seems the odds where not in your favor, in this case the enemy would attack you")
        damage = Goblin.attack
        print("The Goblin Attacks!")
        Myclass.health -= damage
        print(playername + " health:", Myclass.health)
        if Myclass.health <= 0:
            Myclass.health = 0
            print("You have lost the fight")
            print("GAME OVER")
        elif Myclass.health > 0:
            print("God: Dont lose faith! continue the attack!")
            Roll = random.randint(1,10)
            input(" Press Enter to Roll Dice ")
            input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
    

print("God: You now understand the rules of combat")










