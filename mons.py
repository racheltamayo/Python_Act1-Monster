import random
import time
import sys


a = 0.01
b = 0.2
c = 0.08

character_health = 100
monster_health = 10 
monster2_health = 10
attack_punch = 10
attack_jajanken = 20
attack_liverblow = 15
monster_damage = 10
monster_damagetwo = 15
item = ""
item_one = "PYTHON"



def Adventure_end():
    print()
    i1 ='D E F E A T'
    for character in i1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
    endAd()
    
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
    monster_health=monster_health-attack_punch
    monster2_health=monster2_health-attack_punch
    character_health = character_health-monster_damagetwo

def attack_two():
    global character_health
    global monster_health
    global attack_jajanken
    global monster2_health
    monster_health=monster_health-attack_jajanken
    monster2_health=monster2_health-attack_jajanken
    character_health = character_health-monster_damage
    
def attack_three():
    global character_health
    global monster_health
    global attack_liverblow
    global monster2_health
    monster_health=monster_health-attack_liverblow
    monster2_health=monster2_health-attack_liverblow
    character_health = character_health-monster_damage
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

        print("You have jumped into the ravine")
        print("\nYour character has taken 10pt of damage")
        character_health = character_health - 10

    elif v == 3:
        print()
        i1 = 'Hello ' + name + ' I am Aladdin, your magi for this dungeon\nto be able to get powerful metal vessel,\nyou must defeat the two djinns inside the dungeon'
        for character in i1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
        startGame = input("\n\nWould you like to start your adventure? (Y/N): ")
        if startGame == "n" or startGame == "N":
            endAd()
        if startGame == "y" or startGame == "Y":
            monster = int(input("CHOOSE MONSTER [1]. CERBERUS [2]. FERNEUS"))
            if monster == 1:
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
                    time.sleep(b)
                print()
                i3 = 'CERBERUS is the djinn that assigned in this area'
                for character in i3:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(b)
                print()
                i4 = 'do you hear it? he is coming hurry up! kill him\n'
                for character in i4:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(b)
        print ("FORNEUS is preparing to attack")
        time.sleep(3)
        attack = int(input("\nATTACKS:\n\n1.PUNCH\n2.JAJANKEN\n3.LIVER BLOW\nenter the no. of your attack:"))
        if attack == 1:
            attack_one()
            print("One hard punch; monster status " + str(monster_health))
            print("Cerberus Thunder")
            print("Character's health " + str(character_health))
        elif attack == 2:
            attack_two()
            print("jajanken with an overflowing nen; monster status " + str(monster_health))
            print("Cerberus double kick")
            print("Character's health " + str(character_health))
        elif attack == 3:
            attack_three()
            print ("Two consecutive liver blows: " + str(monster_health))
            print("Cerberus long array thunder")
            print("Character's health " + str(character_health))
        print("COMPLETED")
        print("\n~~~~~~~~~~~~~~")
        print("YOUR PASSWORD TO GET THE METAL VESSEL:" + item_one )
        print("~~~~~~~~~~~~~~")
        print()
        i1 ='....................................'
        for character in i1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
        startGame = input("\nWould you like to get yout new metal vessel?? INSERT THE ITEM: ")
        if startGame == "python" or startGame == "PYTHON":
           Adventure_vict()
        else:
            endAd()
        if monster == 2:
            print("Hello!" + name+ " your character's health "+ str(character_health))
    i2 ='WELCOME TO THE SECOND FLOOR'
    for character in i2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)

    print()
    i3 = 'KILL FORNEUS, THE SECOND DJINN AND GET THE PASSWORD TO GET THE METAL VESSEL !'
    for character in i3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print("FORNEUS IS PREPARING TO ATTACK")
    time.sleep(3)
    attack = int(input("\nATTACKS:\n\n1.PUNCH\n2.JAJANKEN\n3.LIVER BLOW\nenter the no. of your attack:"))
    if attack == 1:
            attack_two()
            print("One hard punch; monster status " + str(monster2_health))
            print("FORNEUS ICE MAKE TIGER")
            print("Character's health " + str(character_health))
    elif attack == 2:
            attack_three()
            print("jajanken with an overflowing nen; monster status " + str(monster2_health))
            print("FORNEUS ICE JAIL")
            print("Character's health " + str(character_health))
    elif attack == 3:
            attack_one()
            print ("Two consecutive liver blows: " + str(monster2_health))
            print("FORNEUS ICE MAKE BOW AND ARROW")
            print("Character's health " + str(character_health))
    print("COMPLETED")
    print("\n~~~~~~~~~~~~~~")
    print("YOUR PASSWORD TO GET THE METAL VESSEL:" + item_one )
    print("~~~~~~~~~~~~~~")
    print()
    i1 ='....................................'
    for character in i1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
        startGame = input("\nWould you like to get yout new metal vessel?? INSERT THE PASSWORD: ")
        if startGame == "python" or startGame == "PYTHON":
           Adventure_vict()
        else:
            endAd()
    
            
            
        
    else:
        endAd()

else:
        print("Invalid")
