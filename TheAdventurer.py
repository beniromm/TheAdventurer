import random
character = ""
xp = 0 #xp starts at 0 and will change throughout the game
gp = 0 #money starts at 0 and will change throughout the game

def character_info():
    print "\nUNDER CONSTRUCTION\n"

def character_builder():
    print ("\nIn this game there are 7 different types of characters: Fighters, Clerics, Mages, Thieves, Elves, Dwarves, and Halflings (Hobbit-like folk), each with their own strengths and weaknesses.\n\nFighters have no special abilities, but their high hitpoints and great strength help them survive in dungeons. They are of average intellegence and their common sense leaves what to be desired. As such, they have an additional 10% chance to hit a monster, only speak the common tongue, are 5% less likely to resist the effects of magic spells, and start with 9 hp, gaining 5 hp every level. They may wear any type of armour, may use a shield, and use any weapon. (starts with a normal sword, heavy leather armor, and a sheild.)\n\nClerics have two special abilities: casting cleric spells(which are usually benefitial, like a healing spell), and turning (forcing away) undead monsters. Clerics have a very sound mind, thus it is 10% easier for them to resist the effects of magic spells. Their intellegence is above average, so they can calm and suggest things to animals. They are not as nimble as other characters, causing them to be 5% less acurate with a missile weapon, and making it 5% easier for monsters to hit them. Their kind disposition makes people and monsters react 5% more favorably. They begin with 6 hp, gaining 3 hp every level. They may only wear light or medium armour, may use a shield, and may not use a weapon with a sharp edge. (starts with a war hammar, leather armour, and a shield.) \n\n")

def rules(): #game rules, directed from the home page
    print("\nIn the game, your character will explore a \'dungeon,\' a place where monsters can be found, in search of treasure and experiance.")
    print("\nEach character has different strengths and weaknesses that help that character survive in the \'dungeon.\'")
    print("\nThe rules to this game are very simple: you will be promted with a scenario, and you will choose your action from a list of choices. Each choice will yield a different outcome.")
    print("\nAlthough letter case does not matter, correct spelling does.")
    print("\nXP stands for experiance points. There are five different types of coins that can be found in dungeons: gold pieces (gp), platinum pieces (pp), worth 5gp, electrum pieces (ep), worth .5gp, silver pieces (sp), worth .1gp, and copper pieces (cp), worth .01gp.\n")

def home_else():
    print("\nThis is not an option.\n")
    go_home = raw_input("Write \'home\' to go to the home page: ").lower()
    if go_home == 'home':
        home_page()
    else:
        home_else()

def home_page(): #the home page
    print("\nHello, " + name + ". Welcome to the Adventurer.")
    print("\nFrom here you may play Tutorial or Adventure mode, you may visit the Shop or the Apothecary, you may read the Rules, and you may view your character's info, or if you are new, build a character.")
    print("\nXP = " + str(xp) + " GP = " + str(gp)) + "\n" #shows current gp and xp values
    from_home = raw_input("Simply type \'tutorial\' or \'adventure\' or \'shop\' or \'apothecary\' or \'rules\' or \'character\': ").lower()
    if from_home == 'tutorial': #these will all eventually direct to their respective pages
        print("\nUNDER CONSTRUCTION\n")
        go_home = raw_input("Write \'home\' to go to the home page: ").lower()
        if go_home == 'home':
           home_page() #how to get back to the home page
        else:
            home_else()
    elif from_home == 'adventure':
        print("\nUNDER CONSTRUCTION\n")
        go_home = raw_input("Write \'home\' to go to the home page: ").lower()
        if go_home == 'home':
            home_page()
        else:
            home_else()
    elif from_home == 'shop':
        print("\nUNDER CONSTRUCTION\n")
        go_home = raw_input("Write \'home\' to go to the home page: ").lower()
        if go_home == 'home':
            home_page()
        else:
            home_else()
    elif from_home == 'apothecary':
        print("\nUNDER CONSTRUCTION\n")
        go_home = raw_input("Write \'home\' to go to the home page: ").lower()
        if go_home == 'home':
            home_page()
        else:
            home_else()
    elif from_home == 'rules':
        rules()
        go_home = raw_input("Write \'home\' to go to the home page: ").lower()
        if go_home == 'home':
            home_page()
        else:
            home_else()
    elif from_home == 'character':
        if character == 'fighter' or character == 'cleric' or character == 'thief' or character == 'mage' or character == 'elf' or character == 'dwarf' or character == 'halfling':
            character_info()
        else:
            character_builder()
        go_home = raw_input("Write \'home\' to go to the home page: ").lower()
        if go_home == 'home':
            home_page()
        else:
            home_else()
    else:
        home_else()
print("\nHello. Welcome to Beni Romm's dungeon crawler game, the Adventurer.") #game introduction
print("\nYou will learn more soon, but for now all you need to know is that for this game all you need is something that can run Python, a keyboard, and an imagination.")

name = ""
while (len(name) < 2):
    name = raw_input("First, what is your name? ") #finds players name
name = name[0].upper() + name[1:].lower() #the first letter is always upper case, the rest is always lower case
home_page() #directs to homepage
