import adventureclass
import MonsterClasses
import random
import math
import BossClasses
import sys



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
            print("                                              ,--.")
            print("                                             {    }")
            print("                                             K,   }")
            print("                                            /  `Y`")
            print("                                       _   /   / ")
            print("                                      {_'-K.__/")
            print("                                        `/-.__L._")
            print("                                        /  ' /`\_}")
            print("                                       /  ' /  ")
            print("                               ____   /  ' / ")
            print("                        ,-'~~~~    ~~/  ' /_")
            print("                      ,'             ``~~~  ',")
            print("                     (                     %  Y")
            print("                    {                       % I")
            print("                   {      -                 %  `.")
            print("                   |       ',                %  )")  
            print("                   |        |   ,..__      __. Y")
            print("                   |    .,_./  Y ' / ^Y   J   )|")
            print("                   \           |' /   |   |   ||")
            print("                    \          L_/    . _ (_,.'(")
            print("                     \,   ,      ^^""' / |      )")
            print("                       \_  \          /,L]     /")
            print("                         '-_`-,       ` `   ./`")
            print("                            `-(_            )")
            print("                                ^^\..___,.--`")
            sys.exit()
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

print("_______________________________________________________________________________________________________\n")
input("                   Your party has gotten stroger, your health stat has increased by 3")
input("_______________________________________________________________________________________________________\n")

Myclass.health = Myclass.health +3

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
input("JOJO: What say you " + playername + " do you wish to fight these Trolls or hear their challenges, the choice is yours my friend")
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
        input("UNO: THAT'S WHAT IM TALKING ABOUT, NO WAY WE'RE LETTING THESE MONSTERS STOP US, DOS! TRES! LETS HELP " + playername +" FIGHT THESE BASTARDS")
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
                    print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    print("                                            GAME OVER\n")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
                    print("                                              ,--.")
                    print("                                             {    }")
                    print("                                             K,   }")
                    print("                                            /  `Y`")
                    print("                                       _   /   / ")
                    print("                                      {_'-K.__/")
                    print("                                        `/-.__L._")
                    print("                                        /  ' /`\_}")
                    print("                                       /  ' /  ")
                    print("                               ____   /  ' / ")
                    print("                        ,-'~~~~    ~~/  ' /_")
                    print("                      ,'             ``~~~  ',")
                    print("                     (                     %  Y")
                    print("                    {                       % I")
                    print("                   {      -                 %  `.")
                    print("                   |       ',                %  )")  
                    print("                   |        |   ,..__      __. Y")
                    print("                   |    .,_./  Y ' / ^Y   J   )|")
                    print("                   \           |' /   |   |   ||")
                    print("                    \          L_/    . _ (_,.'(")
                    print("                     \,   ,      ^^""' / |      )")
                    print("                       \_  \          /,L]     /")
                    print("                         '-_`-,       ` `   ./`")
                    print("                            `-(_            )")
                    print("                                ^^\..___,.--`")
                    sys.exit()
                elif Myclass.health > 0:
                    Roll = random.randint(1,10)
                    input(" Press Enter to Roll Dice ")
                    input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
    elif userchoice2 == "2":
        Choice2 = Choice2 + 1
        input(playername + ": I chose, GAME!")
        input("TROLLS: MUHAHAHAHA, YOU CHOSE TO PLAYYY. PREPARE YOURSELF!")
        input(playername + ": Guys be carefull it could be anything!")
        input("TROLLS: THE GAME IS QUITE SIMPLEEEE.")
        input("UNO: SPIT IT OUT ALREADY YA BIG GOOFS!")
        input("TROLLS: THE GAME IS....")
        input("TROLLS: ROOOCKKKK!.....PAAPPEERRRRR!.....SCISSORSSS!")
        input("TROLLS: THERE WILL BE ONLY OONNEEEE ROUNDDD......")
        input("TROLLS: YOUR ONLY OPTIONS ARE....WIN......OR DIE!!!!!!")
        input("DOS: DARNN YOUU, I HATE COMPLICATED MATH OR SINCE OR WHATEVER THIS IS!! I CANT DO IT!")
        input(playername + ": I can do this!")
        input("JOJO: We belive in you " + playername + ", remember you are stronger than you think.")
        input("TROLLS: NOW LET THE GAME BEGINNNN!!!")
        input("TROLLS: YELL YOUR ANSWER ON SHOOT! UNDERSTAND!!")
        input(playername + ": Understood!\n")
        input("TROLLS: ROCK!!!\n")
        input("TROLLS: PAPER!!!\n")
        input("TROLLS: SICSSORS!!!\n")
        input("TROLLS: AND SHOOT!!!\n")

#Rock paper scissor
        s = 0

        while s == 0:

            game1 = ["Rock", "Paper", "Scissors"]
            choice3 = input("Enter either 'Rock' , 'Paper' or 'Scissors': ")
            trollschoice = random.choice(game1)

            if choice3 == "Rock" and trollschoice == "Scissors":
                s = s + 1
                print("TROLLS: NOOOOO, WE'VE BEEN DEFEATED!!!")

            elif choice3 =="Rock" and trollschoice == "Paper":
                    print("GAME OVER")
                
            elif choice3 == "Paper" and trollschoice == "Rock":
                s = s + 1
                print("TROLLS: NOOOOO, WE'VE BEEN DEFEATED!!!")

            elif choice3 == "Paper" and trollschoice == "Scissors":
                    print("GAME OVER")

            elif choice3 == "Scissors" and trollschoice == "Paper":
                s = s + 1
                print("TROLLS: NOOOOO, WE'VE BEEN DEFEATED!!!")

            elif choice3 == "Scissors" and trollschoice == "Rock":
                    print("GAME OVER")
                    print("                                              ,--.")
                    print("                                             {    }")
                    print("                                             K,   }")
                    print("                                            /  `Y`")
                    print("                                       _   /   / ")
                    print("                                      {_'-K.__/")
                    print("                                        `/-.__L._")
                    print("                                        /  ' /`\_}")
                    print("                                       /  ' /  ")
                    print("                               ____   /  ' / ")
                    print("                        ,-'~~~~    ~~/  ' /_")
                    print("                      ,'             ``~~~  ',")
                    print("                     (                     %  Y")
                    print("                    {                       % I")
                    print("                   {      -                 %  `.")
                    print("                   |       ',                %  )")  
                    print("                   |        |   ,..__      __. Y")
                    print("                   |    .,_./  Y ' / ^Y   J   )|")
                    print("                   \           |' /   |   |   ||")
                    print("                    \          L_/    . _ (_,.'(")
                    print("                     \,   ,      ^^""' / |      )")
                    print("                       \_  \          /,L]     /")
                    print("                         '-_`-,       ` `   ./`")
                    print("                            `-(_            )")
                    print("                                ^^\..___,.--`")
                    sys.exit()

            elif choice3 == trollschoice:
                input("TROLLS: A TIEEE!!!")
                input("AGAINNNN!!!!!!!")

            else:
                print("Invalid input, try again.")

#Going to the elfs
input("EVERYONE: HIP HIP HURRAYYYY!!!!!!")
input(playername + ": I was on edge for that, WHEWW!")
input("JOJO: Glad tha's over Huzzahhahaha!")
input("DOS: HAHAHA WELL JOJO, WHERE WE HEADED NOW?")
input("JOJO: HAHA...Haahaha....about that...")
input("JOJO: Our path leads to...The Elfs Kingdom.")
input("ALL THE DWARFS: WHHHAAAATTTTTT!!!!!")
input("TRES: I KNEW IT YOU SCHEMING SCUM!! YOU'RE WORKING WITH THEM FORSAKEN ELFS!!")
input("UNO: WIZZARD YOU BETTER EXPLAIN YOURSELF RIGHT NOW!!!\n")
input(playername + ": HEY! EVERYONE BE QUIET!!!!\n")
input(playername +": WHATS THE MATTER WITH ALL OF YOU!")
input(playername + ": * Deep breath * Jojo has been with all of us from the start, he's the one that brought us all together.")
input("DOS: THE BOYS RIGHT! I KNOW WHAT THIS MEANS FOR US, BUT WE'VE BEEN THROUGH SO MUCH!")
input("UNO: YE LADS HAVE A POINT...BUT I DON'T KNOW IF I HAVE IT IN ME TO GO FORWARD IN THIS DIRECTION!")
input("TRES: OI YE ARE NOT SERIOUS ARE YE!")
input("JOJO: Tres, I must appologise, I understand you feel this way but I solemly swear. I would never betray my comrads!")
input("UNO AND DOS: AYE! WELL SAID!")
input("TRES: IF MY BROTHERS SAY SO...THEN I HAVE NO SAY IN THE MATTER...")
input(playername + ": Don't worry guys, we have eachother no matter what. We can face it all!")
input("UNO: ALRIGHT THEN! IF YOU ARE WITH ME THEN WE ARE UNSTOPPABLE!")
input("EVERYONE: HUZZAAHH!!!")
input("JOJO: Alright then, lets rest for the night a little further down the path. And we move a sunrise.")
input("JOJO: * Whispers to " + playername + " * Hey thanks for helping me out back there. You're a natural leader too huh? Haha")
input(playername + ": Oh that, dont mention it of course my friend!")
input("JOJO: Also keep an eye out for Tres, I have a weird feeling about whats to come...")
input(playername + ": I understand, I dont think it's anything but ill keep an eye out since you mentioned it.")
input("EVERYONE: GOODNIGHT!")
print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("                                              THE NEXT MORNING\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
input("JOJO: Lets go everyone, it should be just past those trees.")
input(playername + ": OH! I can smell the food, and the music it's wonderfull!")
input("UNO: DONT FALL FOR IT BOY HAHAH, THOSE ELFS ARE ONE OF THE MOST FEIRCE FORCES OF NATURE!")
input("DOS: DONT SCARE THE BOY TOO MUCH AHAHAHAHAA!")
input("TRES:...")
input(playername + ": There's the gate lets gooo!")
input("JOJO: " + playername +"! WAIT DONT GET TOO CLOS-")

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
input("ELF GENERAL SVEN: I see, so you wish an audience with his lordship... His majesty will only meet with those of great strength, if you want to get him, you must go through me first, ELF GENERAL SVEN!")
input("JOJO: This is absurd! we are not here to start conflict!")
input("ELF GENERAL SVEN: ENOUGH IDILING! COME... TEST YOUR MIGHT!")
input(playername + ": So be it.")
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
            print("You have Defeated The Elf General!")
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
            print("You have defeated the Elf General!")
        elif ElfGeneral.health > 0:
            Roll = random.randint(1,10)
            input(" Press Enter to Roll Dice ")
            input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
     else:
        damage = ElfGeneral.attack
        print("Elf General Sven Attacks!")
        Myclass.health -= damage
        print(playername + " health:", Myclass.health)

        if Myclass.health <= 0:
            Myclass.health = 0
            print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("                                            GAME OVER\n")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
            print("                                              ,--.")
            print("                                             {    }")
            print("                                             K,   }")
            print("                                            /  `Y`")
            print("                                       _   /   / ")
            print("                                      {_'-K.__/")
            print("                                        `/-.__L._")
            print("                                        /  ' /`\_}")
            print("                                       /  ' /  ")
            print("                               ____   /  ' / ")
            print("                        ,-'~~~~    ~~/  ' /_")
            print("                      ,'             ``~~~  ',")
            print("                     (                     %  Y")
            print("                    {                       % I")
            print("                   {      -                 %  `.")
            print("                   |       ',                %  )")  
            print("                   |        |   ,..__      __. Y")
            print("                   |    .,_./  Y ' / ^Y   J   )|")
            print("                   \           |' /   |   |   ||")
            print("                    \          L_/    . _ (_,.'(")
            print("                     \,   ,      ^^""' / |      )")
            print("                       \_  \          /,L]     /")
            print("                         '-_`-,       ` `   ./`")
            print("                            `-(_            )")
            print("                                ^^\..___,.--`")
            sys.exit()
        elif Myclass.health > 0:
                Roll = random.randint(1,10)
                input(" Press Enter to Roll Dice ")
                input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)

print("_______________________________________________________________________________________________________\n")
print("                   Your Party has grown stronger from battle, there health has increased by 5")
input("_______________________________________________________________________________________________________\n")
Myclass.health = Myclass.health + 5
print("ELF GENERAL SVEN: GAAAHH..... You.... you and your band a lot stronger than I had thought")
input("UNO: DAMN STRAIGHT!")
input("JOJO: *He sure is strong, he could be just what we need for us to reclaim the Dwarven Kingdom...*")
input("ELF GENERAL SVEN: HOWEVER, I WILL NOT YEI-")
input("UNKOWN VOICE: Enough of this Sven...")
input("GENERAL SVEN: YOUR MAJESTY!")
print(",                                      ,")
print("|\                                      /|")
print(",   \'._ ,                           ,  _.'/   ,")
print("|\  {'. '-`\,      ,-._**_.-,      ,/`-' .'}  /|")
print(" \`'-'-.  '.`\      \*____*/      /`.'  .-'-'`/")
print(",'-'-._  '.  ) )    /`    `\     ( (  .'  _.-'-',")
print("|\'- _ '.   , /     /  /""\  \     \ ,  .'  _ -'/|")
print(" \'-.   .  ; (      \_|^  ^|_/      ) ;   .  .-'/")
print("  `'--, . ;  {`-.     \__/      .-'}  ; . ,--'`")
print("   '--`_. ;  { ^  \  _|  |_    /  ^ }  ; ._`--'")
print(" `,_.--  ;  { ^  `-'`      `'-`  ^ }  ;  --._,`")
print("   ,_.-    ; {^    /        \    ^} ;    -._, ")
print("    ,_.-`), /\{^,/\\_ _/\_ _//\,^}/\ ,(`-._,")
print("      _.'.-` /.'   \        /   `.\ `-.'._")
print("     `  _.' `       \      /       ` '._   `")
print("                   .-'.  .'-.")
print("                 .'    `` ^  '.")
print("                /  ^ ^   ^  ^  \ ")
print("                | ^    ^   ^   |")
print("               /^   ^/    \  ^  \ ")
print("               \,_^_/    ^ \_,^./")
print("                 /=/  \^   /  \=\  ")
print("                /=/_   | ^|   _\=\ ")
print("           <(=,'=(==,) |  | (,==)=',=)>")
print("             /_/|_\    /  \    /_|\_\ ")
print("             `V (=|  .'    '.  |=) V`")
print("                 V  / _/  \_ \  V")
print("                     ``\  / `    ")
print("                        \(")
print("\n\n\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| --------------------- |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
print("                                {-{-{-|     ELF KING ENCOUNTER   |-}-}-}\n")
input("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| --------------------- |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n\n")

print("ELF KING: My name is Algiar, I am king of the elves. Join me in the Great Hall....")
input("UNO: WELL HES A LIVELY ONE ISNT HE...")
input("JOJO: Best smarten up quick dwarf, for he is our ticket to saving your kingdom")
input("TRES:AH YES, THE ELVEN KING RESPONSIBLE FOR OUR DOWNFALL IS NOW THE ONLY ONE WHO CAN SAVE US WHAT A BUNCH OF SHITE")
input("DOS: WHATS GOTTEN INTO YOU TRES? CALM YOURSELF")
input(playername + ": Let's listen to JOJO for now, if you want your kingdom to be saved Tres, we must swallow this pill and have conversation with the king")
input("ELF GENERAL SVEN: I will guide you to the Great Hall")
print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("- - - - - - - - - - - - - - - - - - - - - - - - THE GREAT HALL - - - - - - - - - - - - - - - - - - - - -\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
input(playername + ": Woah, this place is beautiful!")
input("UNO: I MUST SAY FOR ELVES... THIS IS EASY ON THE EYES")
input("DOS: AGRRED! IT'S NICE TO SEE ELVEN ARCHITECTURE")
input("TRES: ....")
input("JOJO: YOUR MAJESTY, THANK YOU FOR WELCOMING US INTO YOUR HOME!")
input("ELF KING ALGIAR: No need to thank me")
input("ELF KING ALGIAR: I am very eager to hear what news would bring a " + Myclass.name + " A Wizard and most intriguing of all Dwarves to an Elvish Kingdom")
input("UNO: AIGHT WELL YOU SEE ME LORD-")
input("JOJO: best let me do the talking for now Uno, I promise you'll get your time later")
input("TRES:......")
print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("                                              2 HOURS LATER\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")

input("ELF KING ALGIAR: I SEE! so you need the aid of the elves to take back your long forgotten home!")
input("ELF KING ALGIAR: and of course I would assume the Elves would be generously conpencated for this deed, How Genuienly splendid")
input("TRES: splendid?...SPLENDID?")
print(playername + ": !!!")
print("UNO: !!!")
print("DOS: !!!")
input("JOJO: TRES WAIT NOW IS NOT THE TIME!")
input("TRES: SCREW THE TIME I NEVER KNEW HOW TO READ A CLOCK ANYWAY")
input(playername + ": huh?")
input("TRES: WHAT I DO KNOW, AND HAVE ALWAYS KNOWN SINCE I WAS A WEE LAD, IS THAT YOU ELVES ARE THE REASON WE LOST IT ALL, NOW LOOK AT YOU SITTING HIGH AND MIGHTY ON YOUR THRONE, WHILE WE THE... WE...")
input("TRES: WE THE DWARVES! RUN FOR OUR HOME SEEKING THE AID OF THOSE NOT OF OUR BLOOD LIKE BEGGARS AND NOW YOU TRY TO STEAL WHATS LEFT OF OUR WEALTH AS WELL!! HOW DARE YOU")
input("ELF KING ALGIAR: Is that how you truly feel?")
input("TRES: I'VE HAD ENOUGH OF THIS, I CANT STAND THESE ELVES")
input("TRES: " + playername + "YOU SAID YOU UNDERSTOOD MY PAIN, IF YOU REALLY DO THEN YOU'LL HELP ME DETHRONE THIS FALSE KING AND TAKE THEIR WEAPONS FOR OUR OWN, WE CAN DO THIS WITHOUT THESE DAMN ELVES")
input(playername + ": Tres...")
print("_______________________________________________________________________________________________________\n")
print("                            (1) - Stop Tres")
print("                            (2) - Fight the King.")
print("_______________________________________________________________________________________________________\n")

King = BossClasses.ElfKing()

Choice3 = 0

while Choice3 == 0:
    userchoice3 = input("Enter a number for the corresponding options: ")

    if userchoice3 == "1":
        Choice3 = Choice3 + 1
        print(playername + ": Im sorry Tres... I can't do this, it isnt right")
        input("TRES: I KNEW I SHOULDNT HAVE TRUSTED YOU...")
        input("UNO: STOP IT TRES, YER GOING TO FAR")
        input("DOS: THINK TRES IF WE JUST SIDE WITH THE ELF KING NOW WE CAN GET OUR HOME BACK!")
        input("TRES: IF YOU ALL WILL COWARD FROM THIS, THEN LEAVE IT TO ME TO CLEAN THIS MESS UP ONCE AND FOR-")
        print("_______________________________________________________________________________________________________\n")
        print("                                 Tres has been put to sleep")
        input("_______________________________________________________________________________________________________\n")
        print("JOJO: That took a lot out of me...")
        input("UNO: WHAT DID YOU DO?")
        input("DOS: IS HE GONNA BE OKAY?")
        input("JOJO: He's fine-")
        input(playername + ": He's just asleep, looks like hes out cold too")
        input("JOJO: I apologize for Tres your higness-")
        input("ELF KING ALGIAR: I worry not of such *little* matters, this matter has changed from a poltical one, to a personal once, as I would very much like to see what will happen to your company once you set foot in the Dwarf Kingdom")
        input("ELF KING ALGIAR: Especially since that Monsterous Stunna still resides there... My soldiers and I actually tried many times to take back your land Dwarves, sadly our efforts where in vein")
        input("ELF KING ALGIAR: You bunch seem different than the rest, no one has made it this far before, especially beating my Elf General Sven, of which will be joining you in battle")
        input("but your weapons and armour as it stands is abysmal, GUARDS! bless these fine warriors in my name")
        input("\n\n<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-| ARMOUR AND WEAPONS AQUIRED |-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n\n")
        print("_______________________________________________________________________________________________________\n")
        print("                   Your Attack Stat Has Increased by 3 and Your health stat Has increased by 6")
        input("_______________________________________________________________________________________________________\n")
        Myclass.attack = Myclass.attack + 3
        Myclass.health = Myclass.health + 6
        input("JOJO: Thank you Lord Algiar, with this we can surely take back the Dwarves home")
        input("UNO: CARRY TRES DOS")
        input(playername + ": It's okay I got it")
        print("_______________________________________________________________________________________________________\n")
        print("                   Elf General Sven Has Joined your party and increased you overall damage by 5")
        input("_______________________________________________________________________________________________________\n")
        print("_______________________________________________________________________________________________________\n")
        print("            With the help of the Elve's, The hero's make their way to the Lost Kingdom of The Dwarves")
        input("_______________________________________________________________________________________________________\n")
        input("JOJO: THERE IT IS... THE LOST CITY OF THE DWARVES")
        print("               /~\         .-:::-.     ")
        print("             /` , \      ,:::::::::, ")
        print("            /. `  .\_   ;:::::::::::;")
        print("           / , ~ . ^ `~`\:::::::::::<")
        print("          /~~ . `  . ~  , .`~~\::::")
        print("    /`\  /~,  . ~ , '  `  ,  .` \: ")
        print("  /` .`\ /` .  ^  ,  ~  ,  . ` . ~\~  ")
        print(" / ` , ,`\.  ` ~  ,  ^ ,  `  ~ . . ``~~~`,   ")
        print(" / , ~ . ~ \ , ` .  ^  `  , . ^   .   , ` .`-,___,---,__")
        print(" /` ` . ~ . ` `\ `  ~  ,  .  ,  `  ,  . ~  ^  ,  .  ~  , .`~---,___")
        print(" /` . `  ,  . ~ , \  `  ~  ,  .  ^  ,  ~  .  `  ,  ~  .  ^  ,  ~  .  `-,")
        print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("- - - - - - - - - - - - - - - - - - - - - - - - THE DWARVEN KINGDOM - - - - - - - - - - - - - - - - - - - - -\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
        input("ELF GENERAL SVEN: Alas I have returned to the forsaken remains of this kingdom.")
        input(playername + ": How was you last visit, I was wondering if you're experience could teach us a few things.")
        input("ELF GENERAL SVEN: At my last visit, not only did we have to face the beast, we had to face ourselvs.")
        input("DOS: WHAT DO YE MEAN LAD? FIGHT AMONG US?")
        input("JOJO: Could you be talking about the Devil's Greed?")
        input("ELF GENERAL SVEN: Thats right! How'd you-? Nevermind. The main mission is to focus on staying as ourselfs until we get to the real fight.")
        input(playername + ": Hahaha, luckily for us our determination which brought us this far, this should be easy.")
        input("DOS: HAHAHA NOW THATS WHAT WE LIKE TO HEAR!")
        input("ELF GENERAL SVEN: Alright then, with our spirits up now's the perfect time to push forwards.\n")
        input("ELF GENERAL SVEN: Ah the armory room...")
        input("TRES: * Starts waking up *")
        input("UNKNOWN: * Whispers to Tres * Wake up oh dwarf, you are a fool oh dwarf.")
        input("TRES: * Still admist waking up *")
        input("UNKNOWN: They will betray youuu, you dont need them, wake up Tres, WAKE UP TRES!")
        print("_______________________________________________________________________________________________________\n")
        print("          Tres jumps off your back and grabs a nearby spear from the armoury ready to attack.")
        input("_______________________________________________________________________________________________________\n")
        input("TRES: ALL OF YE, SNAKES! DAMN SNAKES!")
        input("ELF GENERAL SVEN: NO, THE DEVILS CURSE.")
        input("JOJO: Everyone back away from Tres.")
        input(playername + ": TRES SNAP OUT OF IT.")
        input("UNO AND DOS: NO BROTHER PLEASE DONT DO THIS.")
        input("TRES: BACK OFF ALL OF YE, ALL OF YALL DISHONOR ME IN FRONT OF THE SCUM KING AND BETRAYED ME!")
        input("DOS: BROTHER LISTEN TO US ITS NOT LIKE THAT, WE AINT DO NOTHIN BUT PROTECT EACHOTHER")
        input("UNO: ITS TRUe LAD WE ONLY WANT WHATS BESt FOR OUR KINGDOM AND ITS PEOPLE!")
        input("ELF GENERAL SVEN: It's too late everyone please be carefull, theres only one outcome of this. Kombat!")
        input("JOJO: The general is right we have no choice left, the devil has taken over him.")
        input(playername + ": Please Tres don't let it come to this...I dont wanna have to!")
        input("TRES: RAAAAHHHGHGHGH BRING IT ON COWARDS!!!")
        print("\n\n⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠")
        print("⠀⠀⠀⠀⠀⠀⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣾⣧⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⢸⣿⣿⣷⡀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⢀⣾⣿⣿⡇⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣷⠀⣠⣾⣿⣿⣷⣄⠀⣾⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠈⠛⠿⠁⣼⣿⣿⣿⣿⣿⣿⣧⠈⠿⠛⠁⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠘⠛⠛⠛⠛⠛⠛⠛⠛⠃⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀⠿⣿⣶⣶⣶⣶⣿⠿⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⢰⡟⠀⣴⡄⠀⣈⣹⣏⣁⡀⢠⣦⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠈⠀⠐⢿⣿⠿⠿⠿⠿⠿⠿⣿⡿⠂⠀⠙⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢀⣴⣿⣷⣄⠉⢠⣶⠒⠒⣶⡄⠉⣠⣾⣿⣦⡀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠚⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠓⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

        print("\n\n\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| --------------------- |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        print("                                {-{-{-| TRES BATTLE ENCOUNTER |-}-}-}\n")
        input("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| --------------------- |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n\n")

    elif userchoice3 == "2":
        Choice3 = Choice3 + 1
        print(playername + ": I will fight with you tres")
        input("TRES: I KNEW I COULD TRUST YOU")
        input("JOJO: What's the menaing of this" + playername + " !")
        input("UNO: IF " + playername + " THINKS THIS IS THE PATH WE SHOULD TAKE I WILL FOLLOW YOU BROTHER")
        input("DOS: I WONT LEAVE YOU TO FIGHT ALONE")
        input("JOJO: Fools...")
        print("_______________________________________________________________________________________________________\n")
        print("                                 JOJO suddenly vanishes")
        input("_______________________________________________________________________________________________________\n")
        input("ELF KING ALGIAR: FOOLS INDEED!")
        input("ELF GENERAL SVEN: I WILL JOIN YOU MY LORD, LETS SMITE THESE IMPOSTERS!")
        input("ELF KING ALGIAR: NO SVEN THIS FIGHT IS MINE ALONE! You Fools defy a GOD of Elves!")
        input(playername + ": Whats a God to a Non-believer!")

        Roll = random.randint(1,10)

        input(" Press Enter to Roll Dice ")

        print("The Dice lands on... " + color.BOLD + str(Roll) + color.END)

        while Myclass.health > 0 and King.health > 0:
            if Roll in [1,7]:
                damage = 0.7 * King.health
                formatted_damage = "{:.2f}".format(damage)
                print(playername + " and party uses RADIANT SPARK")
                King.health -= damage
                print("ELF KING ALGIAR's health:", King.health)

                if King.health <= 0:
                    print("You have Defeated The King of Elves")
                elif King.health > 0:
                    Roll = random.randint(1,10)
                    input(" Press Enter to Roll Dice ")
                    input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
            elif Roll <= Myclass.speed:
                damage = Myclass.attack + LostDwarves.attack
                print(playername + " and party Attacks!")
                King.health -= damage
                print("ELF KING ALGIAR'S health:", King.health)
                if King.health <= 0:
                    print("You have defeated The King of Elves")
                elif King.health > 0:
                    Roll = random.randint(1,10)
                    input(" Press Enter to Roll Dice ")
                    input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
            else:
                damage = King.attack
                print("ELF KING ALIGAR Attacks!")
                Myclass.health -= damage
                print(playername + " health:", Myclass.health)

                if Myclass.health <= 0:
                    Myclass.health = 0
                    print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    print("                                            GAME OVER\n")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
                    print("                                              ,--.")
                    print("                                             {    }")
                    print("                                             K,   }")
                    print("                                            /  `Y`")
                    print("                                       _   /   / ")
                    print("                                      {_'-K.__/")
                    print("                                        `/-.__L._")
                    print("                                        /  ' /`\_}")
                    print("                                       /  ' /  ")
                    print("                               ____   /  ' / ")
                    print("                        ,-'~~~~    ~~/  ' /_")
                    print("                      ,'             ``~~~  ',")
                    print("                     (                     %  Y")
                    print("                    {                       % I")
                    print("                   {      -                 %  `.")
                    print("                   |       ',                %  )")  
                    print("                   |        |   ,..__      __. Y")
                    print("                   |    .,_./  Y ' / ^Y   J   )|")
                    print("                   \           |' /   |   |   ||")
                    print("                    \          L_/    . _ (_,.'(")
                    print("                     \,   ,      ^^""' / |      )")
                    print("                       \_  \          /,L]     /")
                    print("                         '-_`-,       ` `   ./`")
                    print("                            `-(_            )")
                    print("                                ^^\..___,.--`")
                    sys.exit()

                elif Myclass.health > 0:
                    Roll = random.randint(1,10)
                    input(" Press Enter to Roll Dice ")
                    input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)

        print("ELF GENERAL SVEN: MY LORD NOOOOO!")
        input("ELF KING ALGIAR: how could I lose to such heinous animals... I will not... accept thi-")
        print("_______________________________________________________________________________________________________\n")
        print("                               Lightning strikes the King Killing him")
        print("                           JOJO apears from the lightning with a new aura")
        input("_______________________________________________________________________________________________________\n")
        input(playername + ": JOJO YOUR BACK!")
        input("JOJO: I never entended to leave you all, I knew at some point this fight was inevitable so I had prepared a special potion just for this situation, My magics returned and im ready to fight!")
        input("ELF GENERAL SVEN: YOU'VE SLAIN MY KING, ILL KILL YOU ALL!")
        print("_______________________________________________________________________________________________________\n")
        print("                                  JOJO joins your party!")
        print("          Your party now gets additional Speed and a higher chance for you SUPER POWER to activate")
        input("_______________________________________________________________________________________________________\n")
        Myclass.speed = Myclass.speed + 3

        Roll = random.randint(1,10)

        ElfGeneral2 = BossClasses.ElfGeneralMad()

        input(" Press Enter to Roll Dice ")

        print("The Dice lands on... " + color.BOLD + str(Roll) + color.END)

        while Myclass.health > 0 and ElfGeneral2.health > 0:
            if Roll in [1,7,10]:
                damage = 0.7 * ElfGeneral2.health
                formatted_damage = "{:.2f}".format(damage)
                print(playername + " and party uses RADIANT SPARK")
                ElfGeneral2.health -= damage
                print("ELF GENERAL SVEN'S health:", ElfGeneral2.health)

                if ElfGeneral2.health <= 0:
                    print("You have Defeated The Enraged Elf general")
                elif ElfGeneral2.health > 0:
                    Roll = random.randint(1,10)
                    input(" Press Enter to Roll Dice ")
                    input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
            elif Roll <= Myclass.speed:
                damage = Myclass.attack + LostDwarves.attack
                print(playername + " and party Attacks!")
                ElfGeneral2.health -= damage
                print("ELF GENERAL SVEN's health:", ElfGeneral2.health)
                if ElfGeneral2.health <= 0:
                    print("You have defeated The Enraged Elf general")
                elif ElfGeneral2.health > 0:
                    Roll = random.randint(1,10)
                    input(" Press Enter to Roll Dice ")
                    input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)
            else:
                damage = ElfGeneral2.attack
                print("ELF GENERAL SVEN Attacks!")
                Myclass.health -= damage
                print(playername + " health:", Myclass.health)

                if Myclass.health <= 0:
                    Myclass.health = 0
                    print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                    print("                                            GAME OVER\n")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
                    print("                                              ,--.")
                    print("                                             {    }")
                    print("                                             K,   }")
                    print("                                            /  `Y`")
                    print("                                       _   /   / ")
                    print("                                      {_'-K.__/")
                    print("                                        `/-.__L._")
                    print("                                        /  ' /`\_}")
                    print("                                       /  ' /  ")
                    print("                               ____   /  ' / ")
                    print("                        ,-'~~~~    ~~/  ' /_")
                    print("                      ,'             ``~~~  ',")
                    print("                     (                     %  Y")
                    print("                    {                       % I")
                    print("                   {      -                 %  `.")
                    print("                   |       ',                %  )")  
                    print("                   |        |   ,..__      __. Y")
                    print("                   |    .,_./  Y ' / ^Y   J   )|")
                    print("                   \           |' /   |   |   ||")
                    print("                    \          L_/    . _ (_,.'(")
                    print("                     \,   ,      ^^""' / |      )")
                    print("                       \_  \          /,L]     /")
                    print("                         '-_`-,       ` `   ./`")
                    print("                            `-(_            )")
                    print("                                ^^\..___,.--`")
                    sys.exit()
                elif Myclass.health > 0:
                    Roll = random.randint(1,10)
                    input(" Press Enter to Roll Dice ")
                    input("The Dice lands on... " + color.BOLD + str(Roll) + color.END)

        print("ELF GENERAL SVEN: You fools... have waged war with the elves...")
        input("TRES: WE WILL BE READY")
        input("DOS: LOOK OVER HERE YALL I WAS ABLE TO FIND SOME LOOT!")
        input("\n\n<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-| ARMOUR AND WEAPONS AQUIRED |-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>-<>\n\n")
        print("_______________________________________________________________________________________________________\n")
        print("                       Your party now gets additional 2 attack and 1 health")
        input("_______________________________________________________________________________________________________\n")
        Myclass.attack = Myclass.attack + 2
        Myclass.health = Myclass.health + 1
        input("DOS: THANK YOU FOR HELPING US JOJO!")
        input("JOJO: you dwarves tasked me with helping you reclaim you lost kingdom...I cant accomplish that if you're dead... I do hope you understand what you have done Tres...")
        input(playername + ": *I am sorry JOJO you warned me about tres but I could not help my self")
        input("JOJO: Now is not the time to linger, we must journey to our journey's end")
        input("TRES: THE DWARF KINGDOM!")
        print("_______________________________________________________________________________________________________\n")
        print("                  The party make their way to the Lost Kingdom of The Dwarves")
        input("_______________________________________________________________________________________________________\n")
        input("JOJO: THERE IT IS... THE LOST CITY OF THE ELVES")
        input("UNO: SHES AS BEAUTIFUL AS THE DAY WE LEFT HER")
        print("               /~\         .-:::-.     ")
        print("             /` , \      ,:::::::::, ")
        print("            /. `  .\_   ;:::::::::::;")
        print("           / , ~ . ^ `~`\:::::::::::<")
        print("          /~~ . `  . ~  , .`~~\::::")
        print("    /`\  /~,  . ~ , '  `  ,  .` \: ")
        print("  /` .`\ /` .  ^  ,  ~  ,  . ` . ~\~  ")
        print(" / ` , ,`\.  ` ~  ,  ^ ,  `  ~ . . ``~~~`,   ")
        print(" / , ~ . ~ \ , ` .  ^  `  , . ^   .   , ` .`-,___,---,__")
        print(" /` ` . ~ . ` `\ `  ~  ,  .  ,  `  ,  . ~  ^  ,  .  ~  , .`~---,___")
        print(" /` . `  ,  . ~ , \  `  ~  ,  .  ^  ,  ~  .  `  ,  ~  .  ^  ,  ~  .  `-,")
        print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("- - - - - - - - - - - - - - - - - - - - - - - - THE DWARVEN KINGDOM - - - - - - - - - - - - - - - - - - - - -\n")
        input("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
        input(playername + ": It's- It's incredible I never thought Ive only ever heard of it in stories")
        input("TRES: TAKE A GOOD LOOK " + playername + " THIS IS OUR HOME")
        input("DOS: I MISSED IT SO MUCH... WE HAVE TO GO TO THE THRONE ROOM BROTHERS!")
        input("UNO: YER RIGHT DOS, " + playername + " JOJO, LET US SHOW YOU THE MAGNIFICENT THRONE ROOM OF THE DWARVES")
        print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("- - - - - - - - - - - - - - - - - - - - - - - - THE THRONE ROOM- - - - - - - - - - - - - - - - - - - - -\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
        input("UNO: THIS WHERE OUR FATHERS AND THEIR FATHERS SAT AND RULED THE KINGDOM, WITH THE RICHES AND WEALTH SURROUND THEIR THRONE")
        print("_______________________________________________________________________________________________________\n")
        print("                                        The Gold Entrances Tres")
        input("_______________________________________________________________________________________________________\n")
        input("TRES: *picks up gold coin* THIS... IS BEAUTY")
        input("DOS: IM SO HAPPY TO FINALLY BE BACK HOME!")
        input(playername + ": what about Stunna! Where is the Dragon?")
        input("JOJO: he lives in the Treasury Chamber, The Gold took a curious hold of Stunna...")
        input("DOS: THAT REMINDS ME SINCE WE'RE HEAR WE CAN GO TO THE ARMORY AND GRAB SOME AMAZING GEAR CRAFTED BY OUR FOREFATHERS")
        input("UNO: GREAT IDEA DOS, LET ME TAKE YOU TO THE ARMY")
        input("TRES:....")
        input("JOJO: HUZAAAA, good idea Dwarves")
        input(playername + ": Ill follow your lead JOJO!")
        print("\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        print("- - - - - - - - - - - - - - - - - - - - - - - - THE ARMORY- - - - - - - - - - - - - - - - - - - - -\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n")
        input("UNO: HERE IS THE ARMORY THE FINEST OF DWARF CRAFTSMANSHIP CAN BE SEEN HERE")
        input("JOJO: This place truly is impressive")
        input("DOS: HA COULD YOU IMAGINE IF WE WORKED WITH THE ELV-")
        input("DOS: SORRY.. I DONT KNOW WHAT CAME OVER ME.. IT SEEMS MY MIND IS FOGGY")
        input("JOJO: Its not just you Dos, its this place... Something doesnt seem right here...")
        input("TRES: ARE YOU QUESTIONING THE DWARVEN KINGDOMS POWER?")
        input("JOJO: ?")
        input("JOJO: Tres you know I would do no such thing")
        print("_______________________________________________________________________________________________________\n")
        print("      Tres looks off into a pile of shiny weaponary on the floor almost as if someone was speaking to him")
        input("_______________________________________________________________________________________________________\n")
        input("TRES: How... How Do I know....")
        input("DOS: TRES ARE YOU OKAY? YOU'RE NOT ACTING RIGHT")
        input("TRES: SHUT IT DOS, IM TIRED OF YOUR ACT OF INNOCENCE, YOU KNOW EXACTLY WHAT YOUR DOING, YOU'RE TRYING TO AGITATE ME")
        input("UNO: BROTHER HE WOULD NEVER DO SUCH A THING")
        input("DOS: BROTHER PLEASE... YOU KNOW ME...")
        input("TRES: *They're lying to you... why else would they have listened to you to kill the elf king, its because they're using you* ")
        print("_______________________________________________________________________________________________________\n")
        print("                           Tres picks up a sword from the floor ")
        input("_______________________________________________________________________________________________________\n")
        input("Tres: NONE OF YOU WILL TAKE THIS AWAY FROM ME, I WILL NEVER LOSE MY HOME AGAIN!")
        print("\n\n⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠")
        print("⠀⠀⠀⠀⠀⠀⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣾⣧⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⢸⣿⣿⣷⡀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⢀⣾⣿⣿⡇⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣷⠀⣠⣾⣿⣿⣷⣄⠀⣾⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠈⠛⠿⠁⣼⣿⣿⣿⣿⣿⣿⣧⠈⠿⠛⠁⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠘⠛⠛⠛⠛⠛⠛⠛⠛⠃⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⠀⠿⣿⣶⣶⣶⣶⣿⠿⠀⠹⣷⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⢰⡟⠀⣴⡄⠀⣈⣹⣏⣁⡀⢠⣦⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠈⠀⠐⢿⣿⠿⠿⠿⠿⠿⠿⣿⡿⠂⠀⠙⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢀⣴⣿⣷⣄⠉⢠⣶⠒⠒⣶⡄⠉⣠⣾⣿⣦⡀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠚⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠓⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")

        print("\n\n\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| --------------------- |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        print("                                {-{-{-| TRES BATTLE ENCOUNTER |-}-}-}\n")
        input("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<| --------------------- |>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n\n\n")

        input("JOJO: ITS THE GOLD, IT'S INFECTED HIS MIND I CANT BELIVE IT I THOUGHT It WAS ONLY A MYTH, THATS WHY THE ELF KING COULDNT TAKE BACK THE DWARF KINGDOM, BECAUSE OF THE DEVILS GREED")
        input("UNO: WHAT ARE YOU TALKING ABOUT JOJO")
        input(playername + ": so you're saying that his emotions are being manipulated by the gold?")
        input("JOJO: more specifically by the curse known as the Devils Greed, we know little about it other than the fact that it came in with the abominable Stunna when he conquered the kingdom")
        input("JOJO: Now however is no time to chat, we have to think of a way to stop tres")
        if isinstance(Myclass, adventureclass.Human):
            print(playername + ": Ill Distract him while you all figure out a cure!")
            print(playername + ": TRES STOP, IF YOU REALLY WANNA STOP US THEN WE MUST PLAY A GAME OF ROCK PAPER SCISSORS *Good thing the trolls played it with us*")
            print("TRES: I WILL DESTROY YOU.... IN ROCK PAPER SCISSORS!")
            rockpaper = 0

            while rockpaper == 0:

                game1 = ["Rock", "Paper", "Scissors"]
                choice3 = input("Enter either 'Rock' , 'Paper' or 'Scissors': ")
                trollschoice = random.choice(game1)

                if choice3 == "Rock" and trollschoice == "Scissors":
                    s = s + 1
                    print("TRES: NOOOOO, I CAN'T BELIEVE IT!!!")

                elif choice3 =="Rock" and trollschoice == "Paper":
                    print("GAME OVER")
                    print("                                              ,--.")
                    print("                                             {    }")
                    print("                                             K,   }")
                    print("                                            /  `Y`")
                    print("                                       _   /   / ")
                    print("                                      {_'-K.__/")
                    print("                                        `/-.__L._")
                    print("                                        /  ' /`\_}")
                    print("                                       /  ' /  ")
                    print("                               ____   /  ' / ")
                    print("                        ,-'~~~~    ~~/  ' /_")
                    print("                      ,'             ``~~~  ',")
                    print("                     (                     %  Y")
                    print("                    {                       % I")
                    print("                   {      -                 %  `.")
                    print("                   |       ',                %  )")  
                    print("                   |        |   ,..__      __. Y")
                    print("                   |    .,_./  Y ' / ^Y   J   )|")
                    print("                   \           |' /   |   |   ||")
                    print("                    \          L_/    . _ (_,.'(")
                    print("                     \,   ,      ^^""' / |      )")
                    print("                       \_  \          /,L]     /")
                    print("                         '-_`-,       ` `   ./`")
                    print("                            `-(_            )")
                    print("                                ^^\..___,.--`")
                    sys.exit()
                
                elif choice3 == "Paper" and trollschoice == "Rock":
                    s = s + 1
                    print("TRES: NOOOOO, I CAN'T BELIEVE IT!!!")

                elif choice3 == "Paper" and trollschoice == "Scissors":
                    print("GAME OVER")
                    print("                                              ,--.")
                    print("                                             {    }")
                    print("                                             K,   }")
                    print("                                            /  `Y`")
                    print("                                       _   /   / ")
                    print("                                      {_'-K.__/")
                    print("                                        `/-.__L._")
                    print("                                        /  ' /`\_}")
                    print("                                       /  ' /  ")
                    print("                               ____   /  ' / ")
                    print("                        ,-'~~~~    ~~/  ' /_")
                    print("                      ,'             ``~~~  ',")
                    print("                     (                     %  Y")
                    print("                    {                       % I")
                    print("                   {      -                 %  `.")
                    print("                   |       ',                %  )")  
                    print("                   |        |   ,..__      __. Y")
                    print("                   |    .,_./  Y ' / ^Y   J   )|")
                    print("                   \           |' /   |   |   ||")
                    print("                    \          L_/    . _ (_,.'(")
                    print("                     \,   ,      ^^""' / |      )")
                    print("                       \_  \          /,L]     /")
                    print("                         '-_`-,       ` `   ./`")
                    print("                            `-(_            )")
                    print("                                ^^\..___,.--`")
                    sys.exit()

                elif choice3 == "Scissors" and trollschoice == "Paper":
                    s = s + 1
                    print("TRES: NOOOOO, I CAN'T BELIEVE IT!!!")

                elif choice3 == "Scissors" and trollschoice == "Rock":
                    print("GAME OVER")
                    print("                                              ,--.")
                    print("                                             {    }")
                    print("                                             K,   }")
                    print("                                            /  `Y`")
                    print("                                       _   /   / ")
                    print("                                      {_'-K.__/")
                    print("                                        `/-.__L._")
                    print("                                        /  ' /`\_}")
                    print("                                       /  ' /  ")
                    print("                               ____   /  ' / ")
                    print("                        ,-'~~~~    ~~/  ' /_")
                    print("                      ,'             ``~~~  ',")
                    print("                     (                     %  Y")
                    print("                    {                       % I")
                    print("                   {      -                 %  `.")
                    print("                   |       ',                %  )")  
                    print("                   |        |   ,..__      __. Y")
                    print("                   |    .,_./  Y ' / ^Y   J   )|")
                    print("                   \           |' /   |   |   ||")
                    print("                    \          L_/    . _ (_,.'(")
                    print("                     \,   ,      ^^""' / |      )")
                    print("                       \_  \          /,L]     /")
                    print("                         '-_`-,       ` `   ./`")
                    print("                            `-(_            )")
                    print("                                ^^\..___,.--`")
                    sys.exit()
                elif choice3 == trollschoice:
                    input("TROLLS: A TIEEE!!!")
                    input("AGAINNNN!!!!!!!")

                else:
                    print("Invalid input, try again.")

            print("_______________________________________________________________________________________________________\n")
            print("                           Tres is suddenly hit with a potion ")
            input("_______________________________________________________________________________________________________\n")

            print("TRES: I... CANT MOVE... NOT.... AGAIN...")
            print("_______________________________________________________________________________________________________\n")
            print("                            Tres falls to the floor ")
            input("_______________________________________________________________________________________________________\n")
            

            



        elif isinstance(Myclass, adventureclass.Hobbit):
            print(playername + ": Ill try to snap him out of it, I know hell come back, Im a hobbit, Its my thing :D")
        elif isinstance(Myclass, adventureclass.Dwarf):
            print(playername + ": Although I am a nomad of the dwarves, I must respect Tres's whish to battle it is the Dwarf thing to do!")
        elif isinstance(Myclass, adventureclass.Elf):
            print(playername + ": Although I am an elf I harbor no ill entent to Tres or any of you... I never did, lets trap Tres until we can figure out how to snap him out of it")
        
                  





        


        
        
        



        



        

    
        





            
        








 






    

