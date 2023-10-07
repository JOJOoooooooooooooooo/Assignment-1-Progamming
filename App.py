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
print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| --------------------- |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("><><><><><>><><><><><><><><><><><><<><><><| WELCOME TO THE HOPPIT |<><><><><><><><><><><><><><><><><><><><><\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~| --------------------- |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
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

input("--------------------------------------Press (enter) to enter the world--------------------------------------\n\n\n")
input("                                  After a dailogue press enter to move on.\n\n\n")

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

    MyclassShell = input("Select a class to play as by entering the number corresponding with the class.\n(1) - Human\n(2) - Hobbit\n(3) - Dwarf\n(4) - Elf\n:")

    if MyclassShell == "1":
        x = x + 1
        input("JOJO: Ahh yes... The will of humans are strong, just as I had hoped!")
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


#Dialogue: Introducing JOJO the Wizard
input(playername + ": I dont understand, why are you looking for me?")
input("JOJO: Well, dwarves from a long forgoten culture have come to me to seek help, and the task is to grave for me to do it alone.")
input("JOJO: You see, I am in need of a companion, someone with a pure heart to help me on this quest. That is why I needed to find you!")
input(playername + ": This is all so confusiong, how do you even know that I'm the one with the pure heart?")
input(playername + ": And how did you know where to find me?")
input("JOJO: Worry not my friend, it will all be clear in due time!")
input("JOJO: Instead you should focus on getting home and getting well rested, you have a big day tomorrow. HAHAHAA!")
input(playername + ": It is getting dark soon...wait a minute, what do you mean big day tomorrow?")
input("JOJO: You see that hill in the south?")
input(playername + ": Yeah...?")
input("JOJO: Well, my humble abode resides at the summit, come meet me there at sunrise and our tale of great adventure shall begin!!!")
input(playername + ": All the way there????")
input(playername + ": ...")
input(playername + ": ....")
input(playername + ": .....")
input(playername + ": Fine lets do it!")
input("JOJO: HUZZAH!!, then its set!. I shall see you tomorrow bright and early!")
input("JOJO: Oh! I had almost forgoten, here this is for you. Safe travels my friend.")
input(playername + ": Huh? Whats this?")
input("\n\n<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-| DAGGER AQUIRED |-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n\n")
input(playername + ": Ah I see, I dont see why I would need this but alright. Well I better get some rest for tomorrow.")
print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("                                            THE NEXT MORNING\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
input(playername + ": * Yaaawnnn * Whew, I better start hedding out I dont wanna be late for my new friend.")
print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("- - - - - - - - - - - - - - - - - - - - PATH TO THE TOP OF THE HILL - - - - - - - - - - - - - - - - - -\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
input(playername  + ": Just a little further and I should be able to start seeing some smoke from JOJO's chimney atleast.\n\n")

#Goblin encounter
print("_______________________________________________________________________________________________________\n")
print("                               * The bushes infront of you seems suspisious *")
print("_______________________________________________________________________________________________________\n")
input(playername + ": Huh? Why is that bush moving like that, it's not even windy?")
input("Unkown: Hehehehe, hey you there! Give me all your dabloons now Hehehehe!!!!")
input(playername + ": AHHHH!!!\n\n\n")
print("                                              ,      , ")
print("                                             / (.-""-.) \ ")
print("                                         |\  \/      \/  /| ")
print("                                         | \ / =.  .= \ / | ")
print("                                         \( \   o\/o   / )/ ")
print("                                          \_, '-/  \-' ,_/ ")
print("                                            /   \__/   \ ")
print("                                            \ \__/\__/ / ")
print("                                          ___\ \|--|/ /___ ")
print("                                        /`    \      /    `\ ")
print("                                       /       '----'       \ ")
print("\n\n\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| --------------------- |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
print("                                {-{-{-|    GOBLIN ENCOUNTER   |-}-}-}\n")
print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| --------------------- |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n\n")

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

# introduction to combat
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










