import random
import time
import sys


a = 0.01
b = 0.2
c = 0.08

character_health = 100
monster_health = 40
monster2_health = 100
monster_boss = 150
attack_punch = 5
attack_jajanken = 15
attack_liverblow = 10
monster_damage = 2
monster_damagetwo = 5
item = ""


def endAd():
    print()
    i2 ='>>>>>>>>> EXIT <<<<<<<<<<<'
    for character in i2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
    exit()
    

def attack_one():
    global character_health
    global monster_health
    global attack_punch
    global monster2_health
    global monster_boss
    monster_health=monster_health-attack_punch
    monster2_health=monster2_health-attack_punch
    monster_boss = monster_boss -attack_punch
    character_health = character_health-monster_damagetwo

def attack_two():
    global character_health
    global monster_health
    global attack_jajanken
    global monster2_health
    global monster_boss
    monster_health=monster_health-attack_jajanken
    monster2_health=monster2_health-attack_jajanken
    monster_boss = monster_boss -attack_jajanken
    character_health = character_health-monster_damage
    
def attack_three():
    global character_health
    global monster_health
    global attack_liverblow
    global monster2_health
    global monster_boss
    monster_health=monster_health-attack_liverblow
    monster2_health=monster2_health-attack_liverblow
    monster_boss = monster_boss -attack_liverblow
    character_health = character_health-monster_damage


 
def startAdventureIntro():
    print()
    i1 = 'You have enter the dungeon'
    for character in i1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    i2 = name + '! WELCOME TO THE FIRST FLOOR'
    for character in i2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)

    print()
    i3 = 'CERBERUS is the djinn that assigned in this area'
    for character in i3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    i4 = 'do you hear it? he is coming hurry up! kill him\n'
    for character in i4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    startAdventure()

def Adventure_secondIntro():
    print("Hello!" + name+ " your character's health "+ str(character_health))
    i2 ='WELCOME TO THE SECOND FLOOR'
    for character in i2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)

    print()
    i3 = 'KILL FORNEUS, THE SECOND DJINN AND GET THE HINT!'
    for character in i3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    Adventure_second()

def Adventure_bossIntro():
    print("Hello!" + name+ " your character's health "+ str(character_health))
    print()
    i2 ='THE FINAL STAGE'
    for character in i2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)

    print()
    i1 ='FINAL BATTLE BETWEEN '+ name + ' and AMON THE FLAME DJINN' 
    for character in i1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)

    print()
    i3 = 'TO KILL OR TO BE KILLED? hurry! you can do it'
    for character in i3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    Adventure_boss()
        

def startAdventure():
    if character_health <=0:
        Adventure_end()
    if monster_health <= 0:
        print("COMPLETED")
        print("\n~~~~~~~~~~~~~~")
        print("USE THIS LETTERS TO OPEN THE NEXT DOOR: PY")
        print("~~~~~~~~~~~~~~")
        print()
        i1 ='....................................'
        for character in i1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
        startGame = input("\nWould you like to continue your adventure? ENTER THE LETTERS: ")
        if startGame == "py" or startGame == "PY":
            Adventure_secondIntro()
        else:
            Adventure_end()
    
        
    
    attack = int(input("\nATTACKS:\n\n1.PUNCH\n2.JAJANKEN\n3.LIVER BLOW\nenter the no. of your attack:"))
    if attack == 1:
            attack_one()
            print("One hard punch; monster status " + str(monster_health))
            print("Cerberus Thunder")
            print("Character's health " + str(character_health))
            startAdventure()
    elif attack == 2:
            attack_two()
            print("jajanken with an overflowing nen; monster status " + str(monster_health))
            print("Cerberus double kick")
            print("Character's health " + str(character_health))
            startAdventure()
    elif attack == 3:
            attack_three()
            print ("Two consecutive liver blows: " + str(monster_health))
            print("Cerberus long array thunder")
            print("Character's health " + str(character_health))
            startAdventure()
    else:
        
        startAdventure()

        


def Adventure_second():
    if character_health <=0:
        Adventure_end()
    if monster2_health <= 0:
        print("COMPLETED")
        print("\n~~~~~~~~~~~~~~")
        print("ADD THIS LETTERS TO OPEN THE NEXT DOOR: TH")
        print("~~~~~~~~~~~~~~")
        print()
        i1 ='....................................'
        for character in i1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
        startGame = input("\n\nWould you like to continue your adventure? ADD THE COLLECTED LETTERS FROM FORNEUS PY")
        if startGame == "th" or startGame == "TH":
            Adventure_bossIntro()
        else:
            Adventure_end()


        
    attack = int(input("\nATTACKS:\n\n1.PUNCH\n2.JAJANKEN\n3.LIVER BLOW\nenter the no. of your attack:"))
    if attack == 1:
            attack_two()
            print("One hard punch; monster status " + str(monster2_health))
            print("FORNEUS ICE MAKE TIGER")
            print("Character's health " + str(character_health))
            Adventure_second()
    elif attack == 2:
            attack_three()
            print("jajanken with an overflowing nen; monster status " + str(monster2_health))
            print("FORNEUS ICE JAIL")
            print("Character's health " + str(character_health))
            Adventure_second()
    elif attack == 3:
            attack_one()
            print ("Two consecutive liver blows: " + str(monster2_health))
            print("FORNEUS ICE MAKE BOW AND ARROW")
            print("Character's health " + str(character_health))
            Adventure_second()
    else:
        startAdventure()

            
def Adventure_boss():
    if character_health <=0:
        Adventure_end()
    if monster_boss <= 0:
        print("\nCOMPLETED")
        print()
        i1 ='....................................'
        for character in i1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
        print("\n~~~~~~~~~~~~~~")
        print("ADD THESE LETTERS TO COMPLETE THE PASSWORD: ON")
        print("~~~~~~~~~~~~~~")
        startGame = input("\n\nCONGRATULATIONS! GET YOUR METAL VESSEL, ENTER THE PASSWORD: ")
        if startGame == "python" or startGame == "PYTHON":
            Adventure_vict()
        else:
            Adventure_end()

    attack = int(input("\nATTACKS:\n\n1.PUNCH\n2.JAJANKEN\n3.LIVER BLOW\nenter the no. of your attack:"))
    if attack == 1:
            attack_one()
            print("One hard punch; monster status " + str(monster_boss))
            print("AMON FIRE STYLE, FIRE BALL")
            print("Character's health" + str(character_health))
            Adventure_boss()
    elif attack == 2:
            attack_two()
            print("jajanken with an overflowing nen; monster status " + str(monster_boss))
            print("AMON FIRE STYLE, FIRE DRAGON FLAME")
            print("Character's health " + str(character_health))
            Adventure_boss()
    elif attack == 3:
            attack_three()
            print ("Two consecutive liver blows: " + str(monster_boss))
            print("AMON FIRE STYLE, FIRE OR A ROARING DRAGON")
            print("Character's health " + str(character_health))
            Adventure_boss()
    else:
        startAdventure()


def Adventure_end():
    print()
    i1 ='D E F E A T'
    for character in i1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
    endAd()
      
def Adventure_vict():
    print()
    i1 ='C O N G R A T U L A T I O N S'
    for character in i1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
    print()
    i2 ='DUNGEON COMPLETED'
    for character in i2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
    print()
    i3 ='AMON SWORD IS YOUR NEW METAL VESSEL, IT HAS FLAME POWER'
    for character in i3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
    print(",.                             ")
    print(" \%`.                          ")
    print("  `.%`.                        ")
    print("    `.%`.                      ")
    print("      `.%`.                   ")
    print("        `.%`.                 ")
    print("          `.%`.   __          ")
    print("           `.%`.  \ \         ")
    print("              `.%`./_/        ")
    print("                `./ /.        ")
    print("               __/\/:/;.      ")
    print("               \__/  `:/;.    ")
    print("                       `:/;., ")    
    print("         Amon Sword      `:/ ;  ")
    print("                           `'  ")
    print()
    i3 ='DUNGEON IS STARTING TO SHUTDOWN'
    for character in i3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
    endAd()




print()
print()
print("     ###############################")
print("     |                             |")
print("     | MAGI:THE LABYRINTH OF MAGIC |")
print("     |                             |")
print("     ###############################")
print()
print()
time.sleep(a)
print()
i1 = 'King Solomon created the world...'
for character in i1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
print()
i2 ='to be able to give powers to human, he made dungeon with djinns inside.'
for character in i2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
print()
i3 ='However, human needs a Magi to enter the dungeon.'
for character in i3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
print()
i4 = 'After defeating the djinns inside, \nhuman can have their metal vessels which can give them power.'
for character in i4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
print()
i5 = 'once you enter inside the border, list of choices will be shown'
for character in i5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
print()
i6 = 'choose from the list of choices or else it will close the dungeon'
for character in i6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
print("\nGOOD LUCK\n")
time.sleep(a)


name = input("Enter your name: ")
while character_health > 0:
    if character_health != 100 and item == "Fish":
        n = input("You have taken some damage to heal select [1 to heal/ 0 to ignore]")
        if n == "1":
            character_health += 10
            print("Your character's health is back to " + str(character_health))
        else :
             print("Your character's health is back to " + str(character_health))

    v = int(input("\nWELCOME TO THE LABYRINTH OF MAGIC.\n\nChoose 1 if you want to cross the river\nChoose 2 if you want to jump on the ravine\nChoose 3 if you want to fight monster in the dungeon \n\nINSERT YOUR CHOICE: "))
   
    #Start of Journey
    if v == 1:
        choice = input("If you want to go fishing select [1 for yes/ 0 for no]")
        if choice == "1":
            #Fishing minigame
            print("You have chosen Fishing! ")
            chance = random.randint(0,9)
            if chance > 6:
                item = "Fish"
                print("You have catch a Fish!")
            else:
                print("There is no fish to catch")

        elif choice == "0":
            print("You have crossed the river")


    elif v == 2:
        #damages the player
        print("You have jumped into the ravine")
        print("\nYour character has taken 10pt of damage")
        character_health = character_health - 10

    elif v == 3:
        print()
        i1 = 'Hello ' + name + ' I am Aladdin, your magi for this dungeon\nto be able to get powerful metal vessel,\nyou must defeat the three djinns inside the dungeon'
        for character in i1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
        startGame = input("\n\nWould you like to start your adventure? (Y/N): ")
        if startGame == "n" or startGame == "N":
            print("Rest for a second...")
        if startGame == "y" or startGame == "Y":
            startAdventureIntro()
        else:
            Adventure_end()

else:
        print("Invalid")

