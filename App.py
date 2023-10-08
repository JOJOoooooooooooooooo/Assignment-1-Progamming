import adventureclass
import MonsterClasses
import random
import math
import BossClasses



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
input("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| --------------------- |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n\n")

Goblin = MonsterClasses.Goblin()
# Introduction to combat
print("_______________________________________________________________________________________________________\n")
input("                                  YOU HAVE ENTERED COMBAT WITH A GOBLIN:\n\n")
print("                           In this game combat is won by lowering the enemys health to 0.")
print("                                  You do so by rolling a dice with numbers 1-10,")
print("                If the dice rolls a number that is less than or equal to your speed stat you attack first.\n")
print("                           However, if the dice roll is above your speed stat, the enemy will attack.")
print("                                  If you're health goes to 0 you lose the game")
print("                    Depending on the class you chose, Your Attack, Health, and Speed stats will differ")
input("_______________________________________________________________________________________________________\n")


print("")
print("                                                  STATS                ")
print("                                     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("                                     |      " + color.BOLD + str(playername) + color.END + " Versus " + color.BOLD + str(Goblin.name) + color.END + "      |")
print("                                     -------------------------------")
print("                              Health: " + color.BOLD + str(Myclass.health) + color.END +   "                         " + color.BOLD + str(Goblin.health) + color.END)
print("                                      ------------------------------")
print("                              Attack: " + color.BOLD + str(Myclass.attack) + color.END +  "                         " + color.BOLD + str(Goblin.attack) + color.END)
print("                                      ------------------------------ ")
print("                              Speed:  "  + color.BOLD + str(Myclass.speed) + color.END +   "                         " + color.BOLD + str(Goblin.speed) + color.END)

print("")
print("_______________________________________________________________________________________________________\n")
input("                                      As you can see your speed is " + str(Myclass.speed))
input("                           Meaning that if its equal to or lower than " + str(Myclass.speed) + " You will attack first")
print("                                             Try it out!")
input("_______________________________________________________________________________________________________\n")

Roll = random.randint(1,10)

input(" Press Enter to Roll Dice ")

print("The Dice lands on... " + color.BOLD + str(Roll) + color.END)

while Myclass.health > 0 and Goblin.health > 0: 
    if Roll <= Myclass.speed:
        print("_______________________________________________________________________________________________________\n")
        print("                       Good job! in this case you would take the turn and attack")
        input("_______________________________________________________________________________________________________\n")
        damage = Myclass.attack
        print(playername + " Attacks!")
        Goblin.health -= damage
        input("Goblin health:"+ str(Goblin.health))
        if Goblin.health <= 0:
            print("_______________________________________________________________________________________________________\n")
            print("                                 You have slain the enemy")
            input("_______________________________________________________________________________________________________\n")
        elif Goblin.health > 0:
            Roll = random.randint(1,10)
            input(" Press Enter to Roll Dice ")
            input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
    else:
        print("_______________________________________________________________________________________________________\n")
        print("           Uh oh it seems the odds where not in your favor, in this case the enemy would attack you")
        input("_______________________________________________________________________________________________________\n")
        damage = Goblin.attack
        print("The Goblin Attacks!")
        Myclass.health -= damage
        input(playername + " health:" + str(Myclass.health))
        if Myclass.health <= 0:
            Myclass.health = 0
            print("_______________________________________________________________________________________________________\n")
            print("                            You have lost the fight")
            input("_______________________________________________________________________________________________________\n")
            print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("                                            GAME OVER\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
        elif Myclass.health > 0:
            print("_______________________________________________________________________________________________________\n")
            print("                            Dont lose faith! continue the attack!")
            input("_______________________________________________________________________________________________________\n")
            Roll = random.randint(1,10)
            input(" Press Enter to Roll Dice ")
            input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
    

print("_______________________________________________________________________________________________________\n")
input("                               You now understand the rules of combat")
input("                             As the story progresses combat will evolve")
input("                                   And new challenges will apear.") 
print("                         Be prepared to fight with both your brawn and bains!")
input("_______________________________________________________________________________________________________\n")

#Getting to JOJO's house
input(playername +": Oh wow, that went a lot better than I hoped.")
input("JOJO: Yoooo Hooooo, Good morning " + playername + "! I was wondering how much longer you were gonna take, Hahahaha.")
input(playername + ": By the heavens, JOJO!")
input("JOJO: Oh my! Are we that excited to see me again?")
input("JOJO: Is everything alright by the way? I heard a bunch or ruckus in this area.")
input(playername + ": Im okay now that you're here, and about that ruckus you heard!")
input(playername + ": I defeated a goblin! He went after me as I was coming closer to your home.")
input("JOJO: Oh my, we have a warrior at our hands! Amazing work " + playername + ".")
input("JOJO: Follow me we're almost there, we can patch you up in my medicine bay")

print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("- - - - - - - - - - - - - - - - - - - - - - - - AT JOJO'S HUT - - - - - - - - - - - - - - - - - - - - -\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")

input("JOJO: Well you're all set from here, good as new.")
input(playername + ": Thanks, JOJO. By the way how do you now all the things you do.")
input(playername + ": Like how did you know I was meant to acompny you, or how to heal me like that, or-or-o-")
input("JOJO: My friend, you must rest. You are fresh from battle. Be at ease, as I promised it will all make sense.")
input("JOJO: You just rest in bed for a little longer, and here take this. It should prove to be usefull in the future.")
input("\n\n<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-| NECKLACE AQUIRED |-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n\n")
print("_______________________________________________________________________________________________________\n")
input("                             Your health stat has now doubled since battle!")
print("_______________________________________________________________________________________________________\n")
Myclass.health = Myclass.health * 2
input(playername + ": Phew I feel a lot better, Okay, I trust you, I'm gonna get some shut eye...")

#Intorucing the dwarfs
print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("                                            AFTER THE NAP\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
input(playername + ": * What's all that noises, and who are all those voices?")
print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("- - - - - - - - - - - - - - - - - - - - YOU GO CLOSER TO THE SOUNDS - - - - - - - - - - - - - - - - - -\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
input("Unkown: HAHAHAHAH-OH! IS THIS HIM?")
input("JOJO: Alas, " + playername + ". You are finally awake, I want you to meet the people I mentioned.")
input("Unkown: GREETINGS FELLOW BRAVEHEART! HOPE YER FEELIN BETTER, HAPPY TO MAKE YOUR AQUAINTANCE!")
input(playername + ": Hello everyone! I am " + playername +".")
input("UNO: PLESURE TO MEET'CHA, THE NAMES UNO.")
input("DOS: THE'NAMES DOS HOWDY!")
input("TRES: ......")
input("JOJO: Aaaaand that's Tres, dont worry he's not a talker. But these are the 'Lost Dwarves', you remeber them?")
input(playername + ": Ahhhhh, It's you guys! Hi everyone.")
input("UNO: " + playername + " , SO JOJO MUST'VE GAVE'YA THE RUN DOWN EH?")
input(playername + ": Heh!? Sort of?")
input(playername + ": I'm supposed to...help you guys find a lost key to your house?")
input("DOS: AAAAGHAHAHGHA, YOU'RA FUNNY ONE LADDY!")
input("JOJO: Almost there, but not quite.")
input(playername + ": Huh...?")
input("JOJO: " + playername + ", using your own analogy. YOU are the key we need.")
input(playername + ": And how am I supposed to open a door...?")
input("UNO: WELL YA SEE BOY, THE DOOR IS A LITTLE DIFFRENT THAN WHATS IN YER HEAD.")
input("JOJO: Jokes aside.....you and I are here to help them overthrow a feirce monster to set their home free...")
input("JOJO: I'm sorry I didn't fully explain before and I understand if you want to turn back and-")
input(playername + ": I'm in.")
input("JOJO: ?")
input(playername + ": This has always been my dream growing up, and after fighting the goblin I feel like I'm meant for this!")
input("EVERYONE: HUZZAAHHHHH!!!!")
input("DOS: ALRIGHTY THEN, WE SET OFF AT NOON! PREPARE YOURSELF BEAST WE ARE COMING FOR YE!!")

#GOING TO THE DWARVES
print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("                                                AT NOON\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
input(playername + ": Which direction are we headed by the way?")
input("JOJO: We're headed directly west, my only concern is that the fastest route involves going through the...")
input("JOJO: * Whispers * the elf kingdom, alos you should probably not mention to the dwarfs")
input(playername + ": Hmmm I think I understand what's going on, It's a SURPRIZE PARTY!!")
input("JOJO: SHHHHH, HEY! Don't be so loud. We have to keep our path a secret because of the long and hard conflicts the Elfs have with the Dwarfs.")
input(playername + ": OH! Hahaha, sorry Jojo. I didn't know.")
input("JOJO: Worry not my friend, luckily Uno, Dos, and Tres are waliking ahead of us. This gives us time to catch up.")
input("JOJO: If you want to ask me a question nows the time my friend.")

#Questions from user
print("_______________________________________________________________________________________________________\n")
print("                            (1) - Ask about JOJO.")
print("                            (2) - Ask about the monster.")
print("_______________________________________________________________________________________________________\n")

a = 0

while a == 0:
    userchoice1 = input("Enter a number for the corresponding options: ")

    if userchoice1 == "1":
        a = a + 1
        input("\n\n" + playername + ": Alright then, tell me about yourself, who really are you and what do you do?")
        input("JOJO: Hahaha, well I knew this would happen sooner or later, no point in fighting it hahahah!")
        input(playername + ": ...")
        input("JOJO: You know me as Jojo...BUT my proper name, bestowed onto me by the S.W.M.G! is Jonathan the All Knower!!!")
        input(playername + ": * speachless* ")
        input("JOJO: Hahaha, what a mouthfull am I right.")
        input(playername + ": IT ALL MAKES SENSE NOW! I UNDERSTAND FINALLY!")
        input(playername + ": So that's how you knew where to find me, and that's why u gave me the dagger, AND ALSO THAT'S HOW YOU HEALED ME, AND ALSO-")
        input("JOJO: Whoahhh, slow down there my friend. Hahah you're making me blush.")
        input(playername + ": So you really are something huh? Hahaha.")
        input("JOJO: Hey what's that supposed to mean, Hahaha.")
        input(playername + ": By the way what and who is the S.W.M.G?")
        input("JOJO: Ah you see, the S.W.M.G stands for-")
        input("DOS: HEY YOU LAZYBONES ALMOST DONE BACK THERE! WE CAN ALMOST SEE THE BRIDGE, CMON HURRY UP! HAHAHAHA!")
    
    elif userchoice1 == "2":
        a = a + 1
        input("\n\n" + playername +": Alright then, tell me about this monster we're going to face off.")
        input("JOJO: Making good use of you time I see, Hahaha.")
        input("JOJO: Well this monster is more than JUST a monster, it is feirce unlike any other, it is mightier than all, and it is the most beautiful creature in all the lands.")
        input("JOJO: The sheer size of it is enough to scar all men who aproach it to soil their garments Hahaha.")
        input(playername + ": Well what kind of monster is it then, more specifically this time?")
        input("JOJO: Fair enough, the monster is a Dragon!")
        input(playername + ": IT'S A-A-A D-D-DRAGO-")
        input("DOS: HEY YOU LAZYBONES ALMOST DONE BACK THERE! WE CAN ALMOST SEE THE BRIDGE, CMON HURRY UP! HAHAHAHA!")

    else:
        print("Invalid input, try again.\n")

input("JOJO: Oh well, there goes our time limit for that!")
input("UNO: CMON YA HEAFTY LADS, LETS GET A MOVE ON.")
input(playername + ": COMINGGG!")
input("JOJO: Our next stop should be right over this bridge, ONWARDS!")

#INTRODUCING THE TROLLS

print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("- - - - - - - - - - - - - - - - - - - - THE BAND APPROACHES THE BRIDGE - - - - - - - - - - - - - - - - -\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
input("")
print("_______________________________________________________________________________________________________\n")
print("                                 You feel a tremble in the earth")
print("_______________________________________________________________________________________________________\n")
input("\nUNKOWN: FII FII FOO FUMMMM")
input("UNO: OI WHATS GOIN ON HER")
input("UNKOWN: WHOOOO DAAARES COMEE NEEEAARRR!!!")
input("JOJO: Everyone be ready for anything!\n\n\n")

print("           _......._")
print("       .-'.'.'.'.'.'.`-.")
print("     .'.'.'.'.'.'.'.'.'.`.")
print("    /.'.'               '.\ ")
print("    |.'    _.--...--._     |")
print("    \    `._.-.....-._.'   /")
print("    |     _..- .-. -.._   |")
print(" .-.'    `.   ((@))  .'   '.-.")
print("( ^ \      `--.   .-'     / ^ )")
print(" \  /         .   .       \  /")
print(" /          .'     '.  .-    \ ")
print("( _.\    \ (_`-._.-'_)    /._\)")
print(" `-' \   ' .--.          / `-'")
print("     |  / /|_| `-._.'\   |")
print("     |   |       |_| |   /-.._")
print(" _..-\   `.--.______.'  |")
print("      \       .....     |")
print("       `.  .'      `.  /")
print("         \           .'")
print("          `-..___..-`")
print("\n\n\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| --------------------- |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
print("                                {-{-{-|     TROLL ENCOUNTER   |-}-}-}\n")
input("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| --------------------- |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n\n")
input("Trolls: IF YOU WISHH TO PASS THIS BRIDGE EITHER FIGHT US WHERE WE STAND OR PASS OUR CHALLENGES!")
print("_______________________________________________________________________________________________________\n")
input("                            You have now gained the strength of the Lost Dwarves!")
print("             in Battle Your attack stats will now combine with the attack stats of the dwarves to deal even more power")
input("        You also now have a SUPER POWER; if your dice lands on the numbers 1 or 7 you do 70 percent of your enemies health as damage")
print("                            use your powerful new allies to deal with these Bridge Trolls!")
input("_______________________________________________________________________________________________________\n")
input("JOJO: If we do plan on fighting I will not be able to join...as of now my magic is to weak to help...")
input("JOJO: What say you " + playername + "do you wish to fight these Trolls or hear their challenges, the choice is yours my friend")
print("_______________________________________________________________________________________________________\n")
print("                            (1) - Fight The Trolls!")
print("                            (2) - Attempt their Challenges.")
print("_______________________________________________________________________________________________________\n")

Troll = MonsterClasses.Trolls()

LostDwarves = adventureclass.BandofDwarves()
Choice2 = 0

while Choice2 == 0:
    userchoice2 = input("Enter a number for the corresponding options: ")

    if userchoice2 == "1":
        Choice2 = Choice2 + 1
        print("I Chose to FIGHT!")
        input("UNO: THAT'S WHAT IM TALKING ABOUT, NO WAY WE'RE LETTING THESE MONSTERS STOP US, DOS! TRES! LETS HELP " + playername +"FIGHT THESE BASTARDS")
        Roll = random.randint(1,10)
        input(" Press Enter to Roll Dice ")
        print("The Dice lands on... " + color.BOLD + str(Roll) + color.END)

        while Myclass.health > 0 and Troll.health > 0:
            if Roll in [1,7]:
                damage = 0.7 * Troll.health
                formatted_damage = "{:.2f}".format(damage)
                print(playername + " and party uses RADIANT SPARK")
                Troll.health -= damage
                print("Bridge Trolls health:", Troll.health)

                if Troll.health <= 0:
                    print("You have slain the enemy")
                elif Troll.health > 0:
                    Roll = random.randint(1,10)
                    input(" Press Enter to Roll Dice ")
                    input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
            elif Roll <= Myclass.speed:
                damage = Myclass.attack + LostDwarves.attack
                print(playername + " and party Attacks!")
                Troll.health -= damage
                print("Bridge Trolls health:", Troll.health)
                if Troll.health <= 0:
                    print("You have slain the enemy")
                elif Troll.health > 0:
                    Roll = random.randint(1,10)
                    input(" Press Enter to Roll Dice ")
                    input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
            else:
                damage = Troll.attack
                print("The Trolls Attacks!")
                Myclass.health -= damage
                print(playername + " health:", Myclass.health)

                if Myclass.health <= 0:
                    Myclass.health = 0
                    print("GAME OVER")
                elif Myclass.health > 0:
                    Roll = random.randint(1,10)
                    input(" Press Enter to Roll Dice ")
                    input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
    elif userchoice2 == "2":
        Choice2 = Choice2 + 1
        print("")


input("UNKOWN VOICE: HEY STOP RIGHT THERE!")
input("UNKOWN VOICE: WHERE DO YOU THINK YOU'RE GOING")
print("                      _)\.-.")
print("     .-.__,___,_.-=-. )\`  a`\_")
print(" .-.__\__,__,__.-=-. `/  \     `\ ")
print(" {~,-~-,-~.-~,-,;;;;\ |   '--;`)/") 
print("  \-,~_-~_-,~-,(_(_(;\/   ,;/")   
print(    ",-.~_,-~,-~,)_)_)'.  ;;( ")
print("     `~-,_-~,-~(_(_(_(_\  `;\ ") 
print("  ,        `'~~--,)_)_)_)\_   \ ")
print("  |\              (_(_/_(_,   \  ;")
print("  \ '-.       _.--'  /_/_/_)   | |")
print("   '--.\    .'          /_/    | |")
print("       ))  /       \      |   /.'")
print("      //  /,        | __.'|  |")
print("     //   ||        /`    (  ||")
print("    ||    ||      .'       \ \\")
print("    ||    ||    .'_         \ \\")
print("     \\   //   / _ `\        \ \\_")
print("      \'-'/(   _  `\,;        \ '--:,")
print("        `'`  `'` `-,,;         `" ",,; ")
print("\n\n\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| --------------------- |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
print("                                {-{-{-|     ELF GENERAL ENCOUNTER   |-}-}-}\n")
input("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| --------------------- |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n\n")

input("TRES: I KNEW THEY WOULDNT LET US IN WITHOUT A FIGHT")
input("UNO: WAIT TRES LETS HEAR THEM OUT FIRST, THIS ISNT WISE")
input("JOJO: Yes I agree with UNO, its not right to go into the Elven Kingdom waging conflict, we are here to seek the aid of the Elven King after all")
input("Elf General Sven: I see, so you wish an audience with his lordship... His majesty will only meet with those of great strength, if you want to get him, you must go through me first, ELF GENERAL SVEN!")
input("JOJO: This is absurd! we are not here to start conflict!")
input("Elf General Sven: ENOUGH IDILING! COME... TEST YOUR MIGHT!")
print("_______________________________________________________________________________________________________\n")
print("                            Deafeat General Sven to get an audience with the king")
input("_______________________________________________________________________________________________________\n")

ElfGeneral = BossClasses.ElfGeneral()

Roll = random.randint(1,10)

input(" Press Enter to Roll Dice ")

print("The Dice lands on... " + color.BOLD + str(Roll) + color.END)

while Myclass.health > 0 and ElfGeneral.health > 0:
     if Roll in [1,7]:
        damage = 0.7 * ElfGeneral.health
        formatted_damage = "{:.2f}".format(damage)
        print(playername + " and party uses RADIANT SPARK")
        ElfGeneral.health -= damage
        print("Elf General Sven health:", ElfGeneral.health)
        if ElfGeneral.health <= 0:
            print("You have slain the enemy")
        elif ElfGeneral.health > 0:
            Roll = random.randint(1,10)
            input(" Press Enter to Roll Dice ")
            input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
     elif Roll <= Myclass.speed:
        damage = Myclass.attack + LostDwarves.attack
        print(playername + " and party Attacks!")
        ElfGeneral.health -= damage
        print("Elf General Sven:", ElfGeneral.health)
        if ElfGeneral.health <= 0:
            print("You have slain the enemy")
        elif ElfGeneral.health > 0:
            Roll = random.randint(1,10)
            input(" Press Enter to Roll Dice ")
            input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
     else:
        damage = ElfGeneral.attack
        print("ELf General Sven Attacks!")
        Myclass.health -= damage
        print(playername + " health:", Myclass.health)

        if Myclass.health <= 0:
            Myclass.health = 0
            print("GAME OVER")
        elif Myclass.health > 0:
                Roll = random.randint(1,10)
                input(" Press Enter to Roll Dice ")
                input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)






 






    

