#!/usr/bin/env python3

# eldenRingOOP.py - Mini Elden Ring-based game that lets the user
# the tutorial boss Solder of Godrick and a majority of the field,
# mini, and main bosses from Elden Ring. Uses a random die roll of
# 1-20 to decide if the Tarnished was able to attack the boss and
# dodge/block the boss' attack.

# Allows class selection via pyinputplus module and a list of .json
# files stored in elden_ring/classes. The .json file contains the
# class name followed by each stat and their values for each Elden
# Ring starting class (e.g. Vig: 0).
# The stats are followed by the 6 equipment slots for the character
# including Right Hand, Left Hand, Helm, Torso, Wrists, and Legs.


import random
import sys
import os
import time
import json
import math
try:
    import pyinputplus as pyip
except ImportError:
    print("\nPlease install the missing module: pyinputplus")
    sys.exit(1)


def roll_d20(advantage=False, disadvantage=False):
    # Roll a number in the range 1-20 and return it. If the roller has
    # advantage, then roll twice and return the higher number. If the
    # roller has disadvantage, then roll twice and return the lower number.
    # Else, return a single roll of the 20-sided die.
    if advantage:
        return max(random.randrange(1,21), random.randrange(1,21))
    elif disadvantage:
        return min(random.randrange(1,21), random.randrange(1,21))
    else:
        return random.randrange(1,21)


def roll_d10():
    # Roll a number in the range 1-10 and return it.
    return random.randrange(1,11)


# The class for the the player character.
class Character:
    # Paths for the directory/file that contains the classes and
    # the starter weapons for each class.
    __classesPath = os.path.abspath(f'./classes/')
    __starterWeaponsPath = os.path.abspath(f'./weapons/starter-weapons.json')

    def __init__(self):
        self.__playerMaxHealth = 0
        self.__playerCurrentHealth = 0
        self.__playerAttack = 0
        self.__playerArmor = 11

        self.__stats = {
            'Vig:': 0,
            'Mnd:': 0,
            'End:': 0,
            'Str:': 0,
            'Dex:': 0,
            'Int:': 0,
            'Fth:': 0,
            'Arc:': 0
        }   # Dictionary to store the player's stats.

        self.__equipment = {
            'Right Hand:': "",
            'Left Hand:': "",
            'Helm:': "",
            'Torso:': "",
            'Wrists:': "",
            'Legs:': ""
        }   # Dictionary to store the player's currently equipped gear.

        # __self.inventory = {}    # TODO: Dictionary to track the player's inventory.

        # Clear the screen for the terminal.
        os.system('cls' if os.name == 'nt' else 'clear')

        # Create a menu of the classes for the player to choose from:
        self.__character = pyip.inputMenu(['Astrologer', 'Bandit','Confessor',
                                    'Hero', 'Prisoner', 'Prophet', 'Samurai',
                                    'Vagabond', 'Warrior', 'Wretch', 'Quit'],
                                   numbered=True)

        # Exit the program if the player chooses the 'Quit' option.
        if self.__character == 'Quit':
            sys.exit()

        # Get a name for the player.
        self.__playerName = pyip.inputStr(
                            prompt='\nEnter a name for your character: ')

        # "Load" the class and clear the screen.
        print('Loading class...')
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

        # Join the path to the classes .json files and the chosen class to get
        # the .json file for the chosen class and load the json file data into
        # classData.
        try:
            jsonFile = open(os.path.join(Character.__classesPath,
                                        self.__character.lower() + '.json'), 'r')
            self.__classData = json.load(jsonFile)
            jsonFile.close()
        except FileNotFoundError:
            print('\nFile {} not found! Exiting...'
                  .format(os.path.join(Character.__classesPath,
                                       self.__character.lower() + '.json')))
            sys.exit(1)

        for k, v in self.__classData['Stats'].items():
            # Store the player's stats in the __stats dict.
            self.__stats[k] = v

        for k, v in self.__classData['Equipment'].items():
            # Fill the slots for the player's equipment in the
            # __equipment dict.
            self.__equipment[k] = v

        # Search through the starter weapons file to find the weapon that is
        # in the player's right hand and give the player that weapon's attack
        # rating.
        try:
            with open(Character.__starterWeaponsPath, 'r') as jsonFile:
                self.__weaponReader = json.load(jsonFile)
        except FileNotFoundError:
            print('\nFile {} not found! Exiting...'
                  .format(Character.__starterWeaponsPath))
            sys.exit(1)

        for k, v in self.__weaponReader.items():
            if k == self.__equipment['Right Hand:']:
                self.__playerAttack = int(v)
            # If the player is holding another weapon in their left hand, then
            # increase the player's attack rating by half of the left-handed
            # weapon.
            if k == self.__equipment['Left Hand:']:
                self.__playerAttack += (int(v) // 2)

        # Get the player's max health and set their current health equal to
        # their max health.
        self.__playerMaxHealth = (self.__stats['Vig:'] * 10)
        self.__playerCurrentHealth = self.__playerMaxHealth

        # Determine if the player has a shielf in their left hand.
        if "shield" or "buckler" in self.__equipment['Left Hand:'].lower():
            self.__playerArmor = 13
        
    def print_stats(self):
        # Print the player's class and stats.
        print('Name: {}\n'.format(self.__playerName))
        print('Class: {}\n'.format(self.__character))
        for k, v in self.__stats.items():
            print(k.ljust(7, ' ') + str(v))
        print('\nHP: {}'.format(self.__playerMaxHealth))
        print('Attack: {}'.format(self.__playerAttack))
        print('-' * 30)

        # Print the player's currently equipped items.
        for k, v in self.__equipment.items():
            print(k.ljust(12, ' ') + v)
        print('-' * 30)

        # Let the player read the chosen class' stats.
        time.sleep(3)
        # Wait for the player to hit 'ENTER' to initiate the first battle.
        input("Press 'ENTER' to continue...")

    def print_health(self):
        # Print the player's current health.
        print('\n{}'.format(self.__playerName))
        print('HP: {}'.format(self.__playerCurrentHealth))

    def get_name(self):
        # Return the player's name.
        return self.__playerName

    def get_armor(self):
        # Return the player's armor rating for boss damage rolls.
        return self.__playerArmor

    def get_health(self):
        # Return the player's current health.
        return self.__playerCurrentHealth

    def grace(self):
        print('\nRest...') # Rest and prepare for the next battle.
        time.sleep(3)
        # Heal the player's current health to their max health.
        self.__playerCurrentHealth = self.__playerMaxHealth
        print('Fully healed and preparing for next battle...')
        time.sleep(2)
        print('-' * 30)

    def reduce_health(self, damage = 0):
        # Reduce the player's current health by the damage amount.
        self.__playerCurrentHealth -= damage

    def attack(self):
        # Perform a d10 die roll to determine the player's damage done to the
        # boss. The damage dealt is equal to a percentage of player's current
        # attack rating. The percentage is based off the results of the d10
        # die roll. For example, a roll of 4 will do 40% of the player's
        # attack rating in damage.
        # Round the damage number up to nearest whole number.
        return math.ceil(self.__playerAttack * (roll_d10() / 10))

    
# Class for the boss character.
class Boss():
    __bossesPath = os.path.abspath(f'./bosses/')

    def __init__(self):
        # Set the starter/tutorial boss name, health, attack, and armor.
        self.__bossName = 'Soldier of Godrick'
        self.__bossHealth = 300
        self.__bossAttack = 10
        self.__bossArmor = 7

    def set_field_boss(self):
        # Set the boss stats for a field boss.
        self.__bossHealth = 500
        self.__bossAttack = 15
        self.__bossArmor = 9

        # Read the field boss list file and create a list of field bosses.
        try:
            with open(os.path.join(Boss.__bossesPath,
                                   'field-boss-list.txt')) as bossFile:
                bossList = bossFile.readlines()
                # Use a random choice from the boss list for the boss name.
                self.__bossName = random.choice(bossList).rstrip()
        except FileNotFoundError:
            print('\nFile {} not found! Exiting...'
                  .format(os.path.join(Boss.__bossesPath,
                                       'field-boss-list.txt')))
            sys.exit(1)

    def set_mini_boss(self):
        # Set the boss stats for a mini boss.
        self.__bossHealth = 800
        self.__bossAttack = 20
        self.__bossArmor = 11

        # Read the mini boss list file and create a list of mini bosses.
        try:
            with open(os.path.join(Boss.__bossesPath,
                                   'mini-boss-list.txt')) as bossFile:
                bossList = bossFile.readlines()
                # Use a random choice from the boss list for the boss name.
                self.__bossName = random.choice(bossList).rstrip()
        except FileNotFoundError:
            print('\nFile {} not found! Exiting...'
                  .format(os.path.join(Boss.__bossesPath,
                                       'mini-boss-list.txt')))
            sys.exit(1)

    def set_main_boss(self):
        # Set the boss stats for the main boss.
        self.__bossHealth = 1200
        self.__bossAttack = 25
        self.__bossArmor = 13

        # Read the main boss list file and create a list of main bosses.
        try:
            with open(os.path.join(Boss.__bossesPath,
                                   'main-boss-list.txt')) as bossFile:
                bossList = bossFile.readlines()
                # Use a random choice from the boss list for the boss name.
                self.__bossName = random.choice(bossList).rstrip()
        except FileNotFoundError:
            print('\nFile {} not found! Exiting...'
                  .format(os.path.join(Boss.__bossesPath,
                                       'main-boss-list.txt')))
            sys.exit(1)

    def print_stats(self):
        # Print the boss' name and health.
        print('\n{}'.format(self.__bossName))
        print('HP: {}'.format(self.__bossHealth))

    def get_health(self):
        # Return the boss' health.
        return self.__bossHealth

    def get_armor(self):
        # Return the boss' armor for player damage rolls.
        return self.__bossArmor

    def get_name(self):
        # Return the boss' name.
        return self.__bossName

    def reduce_health(self, damage = 0):
        # Reduce the boss' health by the damage amount.
        self.__bossHealth -= damage

    def attack(self):
        # Perform a d10 die roll to determine the boss' damage done to the
        # player. The damage dealt is equal to a percentage of the boss'
        # current attack rating. The percentage is based off the results of
        # the d10 die roll. For example, a roll of 4 will do 40% of the boss'
        # attack rating in damage.
        # Round the damage number up to nearest whole number.
        return math.ceil(self.__bossAttack * (roll_d10() / 10))


def player_attack_phase(playerObj, bossObj):
    # Allows the player to perform an attack on the boss.
    # Use input() so the fight is interactive for the user.
    print('\n{} attack phase.'.format(playerObj.get_name()))
    input("Press 'ENTER' to roll for attack...")
    if roll_d20() < bossObj.get_armor():    # Attack roll fails if the boss'
        print('Attack roll failed!')        # armor is higher than the roll.
        time.sleep(1)   # Pause for the player to read the roll result.
    else:
        print('Attack roll success!')
        time.sleep(0.5)
        input("Press 'ENTER' to roll for damage...")
        time.sleep(0.5)
        # Get the damage done to the boss, reduce the boss' health, and let
        # the player know how much damage was done to the boss.
        dmg = playerObj.attack()
        bossObj.reduce_health(dmg)
        print('Hit {} for {} damage!'.format(bossObj.get_name(), dmg))
        time.sleep(1)


def boss_attack_phase(playerObj, bossObj):
    # Allows the boss to perform an attack on the player.
    print('\nBoss attack phase.')
    if roll_d20() < playerObj.get_armor():  # Attack roll fails if the
        print('Attack roll failed!')        # player's armor is higher than
        time.sleep(1)                       # the roll result.
    else:
        # Let the player know what steps are happening.
        print('Attack roll success!')
        time.sleep(0.5)
        print('Rolling for damage...')
        time.sleep(0.5)
        # Get the damage done to the player, reduce the player's health, and
        # let the player know how much damage was done to the player.
        dmg = bossObj.attack()
        playerObj.reduce_health(dmg)
        print('Hit {} for {} damage!'.format(playerObj.get_name(), dmg))
        # Allow the player to interactively proceed to the next phase.
        input("Press 'ENTER' to continue...")


# Function to fight the tutorial boss "Soldier of Godrick".
# This should be the first fight performed by the player and should only
# occur once in the program.
def tutorial_boss_fight(playerObj, bossObj):
    # Introduce the boss to the player and begin the boss fight.
    print('\nA CHALLENGER APPROACHES\n')
    print('Begin fight VS {}'.format(bossObj.get_name()))
    time.sleep(1)

    # Loop until either the player or the boss run out of health.
    while playerObj.get_health() > 0 and bossObj.get_health() > 0:
        # Separate the attack phases for easier readability.
        print('\n' + ('-' * 30))
        playerObj.print_health()    # Display the player's current hp.
        bossObj.print_stats()       # Display the boss' current hp.

        # Begin player attack phase.
        player_attack_phase(playerObj, bossObj)
        if bossObj.get_health() > 0:
            # Begin boss attack phase if the boss is still alive.
            boss_attack_phase(playerObj, bossObj)

    # If the player has no hp, then show a defeat screen and exit the program.
    if playerObj.get_health() <= 0:
        print('\nYOU DIED\n')
        time.sleep(1)
        sys.exit(0)
    
    # If the boss has no hp, then show a victory screen and proceed.
    print('\nENEMY FELLED\n')
    time.sleep(1)
    # Make the rest action interactive for the player.
    input("Press'ENTER' to rest...")
    
    
# Function to fight the tutorial boss "Soldier of Godrick".
# This should be the first fight performed by the player and should only
# occur once in the program.
# This version of the function is to be used for two players.
def two_player_tutorial_boss_fight(playerList, bossObj):
    # Set the players from the list to separate variables.
    hostObj = playerList[0]
    summonOne = playerList[1]
    
    # Introduce the boss to the player and begin the boss fight.
    print('\nA CHALLENGER APPROACHES\n')
    print('Begin fight VS {}'.format(bossObj.get_name()))
    time.sleep(1)

    # Loop until either the player or the boss run out of health.
    while hostObj.get_health() > 0 and bossObj.get_health() > 0:
        # Separate the attack phases for easier readability.
        print('\n' + ('-' * 30))
        hostObj.print_health()      # Display the player's current hp.
        summonOne.print_health()    # Display the first summon's hp.
        bossObj.print_stats()       # Display the boss' current hp.

        # Begin host attack phase.
        player_attack_phase(hostObj, bossObj)
        if bossObj.get_health() > 0:
            # Begin boss attack phase if the boss is still alive.
            boss_attack_phase(hostObj, bossObj)
        else:
            # Break from the loop if the boss dies from the host's attack.
            break
        
        # Begin first summon attack phase.
        player_attack_phase(summonOne, bossObj)
        if bossObj.get_health() > 0:
            # Begin boss attack phase if the boss is still alive.
            boss_attack_phase(summonOne, bossObj)

    # If the player has no hp, then show a defeat screen and exit the program.
    if hostObj.get_health() <= 0:
        print('\nYOU DIED\n')
        time.sleep(1)
        sys.exit(0)
    
    # If the boss has no hp, then show a victory screen and proceed.
    print('\nENEMY FELLED\n')
    time.sleep(1)
    # Make the rest action interactive for the player.
    input("Press'ENTER' to rest...")


def field_boss_fight(playerObj, bossObj):
    # Set the boss stats to the stats appropriate for a field boss.
    bossObj.set_field_boss()

    # Introduce the boss to the player and begin the boss fight.
    print('\nA CHALLENGER APPROACHES\n')
    print('Begin fight VS {}'.format(bossObj.get_name()))
    time.sleep(1)

    # Loop until either the player or the boss run out of health.
    while playerObj.get_health() > 0 and bossObj.get_health() > 0:
        # Separate the attack phases for easier readability.
        print('\n' + ('-' * 30))
        playerObj.print_health()    # Display the player's current hp.
        bossObj.print_stats()       # Display the boss' current hp.

        # Begin player attack phase.
        player_attack_phase(playerObj, bossObj)
        if bossObj.get_health() > 0:
            # Begin boss attack phase if the boss is still alive.
            boss_attack_phase(playerObj, bossObj)

    # If the player has no hp, then show a defeat screen and exit the program.
    if playerObj.get_health() <= 0:
        print('\nYOU DIED\n')
        time.sleep(1)
        sys.exit(0)

    # If the boss has no hp, then show a victory screen and proceed.
    print('\nENEMY FELLED\n')
    time.sleep(1)
    # Make the rest action interactive for the player.
    input("Press'ENTER' to rest...")
    
    
def two_player_field_boss_fight(playerList, bossObj):
    # Set the players from the list to separate variables.
    hostObj = playerList[0]
    summonOne = playerList[1]
    
    # Set the boss stats to the stats appropriate for a field boss.
    bossObj.set_field_boss()

    # Introduce the boss to the player and begin the boss fight.
    print('\nA CHALLENGER APPROACHES\n')
    print('Begin fight VS {}'.format(bossObj.get_name()))
    time.sleep(1)

    # Loop until either the player or the boss run out of health.
    while hostObj.get_health() > 0 and bossObj.get_health() > 0:
        # Separate the attack phases for easier readability.
        print('\n' + ('-' * 30))
        hostObj.print_health()      # Display the player's current hp.
        summonOne.print_health()    # Display the first summon's current hp.
        bossObj.print_stats()       # Display the boss' current hp.

        # Begin player attack phase.
        player_attack_phase(hostObj, bossObj)
        if bossObj.get_health() > 0:
            # Begin boss attack phase if the boss is still alive.
            boss_attack_phase(hostObj, bossObj)
        else:
            # Break out of the loop if the boss dies to the host's attack.
            break
        
        # Begin first summon attack phase.
        player_attack_phase(summonOne, bossObj)
        if bossObj.get_health() > 0:
            # Begin boss attack phase if the boss is still alive.
            boss_attack_phase(summonOne, bossObj)

    # If the player has no hp, then show a defeat screen and exit the program.
    if hostObj.get_health() <= 0:
        print('\nYOU DIED\n')
        time.sleep(1)
        sys.exit(0)

    # If the boss has no hp, then show a victory screen and proceed.
    print('\nENEMY FELLED\n')
    time.sleep(1)
    # Make the rest action interactive for the player.
    input("Press'ENTER' to rest...")


def mini_boss_fight(playerObj, bossObj):
    # Set the boss stats to the stats appropriate for a mini boss.
    bossObj.set_mini_boss()

    # Introduce the boss to the player and begin the boss fight.
    print('\nA CHALLENGER APPROACHES\n')
    print('Begin fight VS {}'.format(bossObj.get_name()))
    time.sleep(1)

    # Loop until either the player or the boss run out of health.
    while playerObj.get_health() > 0 and bossObj.get_health() > 0:
        # Separate the attack phases for easier readability.
        print('\n' + ('-' * 30))
        playerObj.print_health()    # Display the player's current hp.
        bossObj.print_stats()       # Display the boss' current hp.

        # Begin player attack phase.
        player_attack_phase(playerObj, bossObj)
        if bossObj.get_health() > 0:
            # Begin boss attack phase if the boss is still alive.
            boss_attack_phase(playerObj, bossObj)

    # If the player has no hp, then show a defeat screen and exit the program.
    if playerObj.get_health() <= 0:
        print('\nYOU DIED\n')
        time.sleep(1)
        sys.exit(0)

    # If the boss has no hp, then show a victory screen and proceed.
    print('\nENEMY FELLED\n')
    time.sleep(1)
    # Make the rest action interactive for the player.
    input("Press'ENTER' to rest...")
    
    
def two_player_mini_boss_fight(playerList, bossObj):
    # Set the players from the list to separate variables.
    hostObj = playerList[0]
    summonOne = playerList[1]
    
    # Set the boss stats to the stats appropriate for a mini boss.
    bossObj.set_mini_boss()

    # Introduce the boss to the player and begin the boss fight.
    print('\nA CHALLENGER APPROACHES\n')
    print('Begin fight VS {}'.format(bossObj.get_name()))
    time.sleep(1)

    # Loop until either the player or the boss run out of health.
    while hostObj.get_health() > 0 and bossObj.get_health() > 0:
        # Separate the attack phases for easier readability.
        print('\n' + ('-' * 30))
        hostObj.print_health()      # Display the player's current hp.
        summonOne.print_health()    # Display the first summon's current hp.
        bossObj.print_stats()       # Display the boss' current hp.

        # Begin player attack phase.
        player_attack_phase(hostObj, bossObj)
        if bossObj.get_health() > 0:
            # Begin boss attack phase if the boss is still alive.
            boss_attack_phase(hostObj, bossObj)
        else:
            # Break from the loop if the boss dies from the host's attack.
            break
        
        # Begin first summon attack phase.
        player_attack_phase(summonOne, bossObj)
        if bossObj.get_health() > 0:
            # Begin boss attack phase if the boss is still alive.
            boss_attack_phase(summonOne, bossObj)

    # If the player has no hp, then show a defeat screen and exit the program.
    if hostObj.get_health() <= 0:
        print('\nYOU DIED\n')
        time.sleep(1)
        sys.exit(0)

    # If the boss has no hp, then show a victory screen and proceed.
    print('\nENEMY FELLED\n')
    time.sleep(1)
    # Make the rest action interactive for the player.
    input("Press'ENTER' to rest...")


def main_boss_fight(playerObj, bossObj):
    # Set the boss stats to the stats appropriate for a main boss.
    bossObj.set_main_boss()

    # Introduce the boss to the player and begin the boss fight.
    print('\nA CHALLENGER APPROACHES\n')
    print('Begin fight VS {}'.format(bossObj.get_name()))
    time.sleep(1)

    # Loop until either the player or the boss run out of health.
    while playerObj.get_health() > 0 and bossObj.get_health() > 0:
        # Separate the attack phases for easier readability.
        print('\n' + ('-' * 30))
        playerObj.print_health()    # Display the player's current hp.
        bossObj.print_stats()       # Display the boss' current hp.

        # Begin player attack phase.
        player_attack_phase(playerObj, bossObj)
        if bossObj.get_health() > 0:
            # Begin boss attack phase if the boss is still alive.
            boss_attack_phase(playerObj, bossObj)

    # If the player has no hp, then show a defeat screen and exit the program.
    if playerObj.get_health() <= 0:
        print('\nYOU DIED\n')
        time.sleep(1)
        sys.exit(0)

    # If the boss has no hp, then show a victory screen and proceed.
    print('\nENEMY FELLED\n')
    time.sleep(1)
    # Make the exit action interactive for the player.
    input("Press'ENTER' to end journey...")
    
    
def two_player_main_boss_fight(playerList, bossObj):
    # Set the players from the list to separate variables.
    hostObj = playerList[0]
    summonOne = playerList[1]
    
    # Set the boss stats to the stats appropriate for a main boss.
    bossObj.set_main_boss()

    # Introduce the boss to the player and begin the boss fight.
    print('\nA CHALLENGER APPROACHES\n')
    print('Begin fight VS {}'.format(bossObj.get_name()))
    time.sleep(1)

    # Loop until either the player or the boss run out of health.
    while hostObj.get_health() > 0 and bossObj.get_health() > 0:
        # Separate the attack phases for easier readability.
        print('\n' + ('-' * 30))
        hostObj.print_health()      # Display the player's current hp.
        summonOne.print_health()    # Display the first summon's current hp.
        bossObj.print_stats()       # Display the boss' current hp.

        # Begin player attack phase.
        player_attack_phase(hostObj, bossObj)
        if bossObj.get_health() > 0:
            # Begin boss attack phase if the boss is still alive.
            boss_attack_phase(hostObj, bossObj)
        else:
            # Break from the loop if the boss dies from the host's attack.
            break
        
        # Begin first summon attack phase.
        player_attack_phase(summonOne, bossObj)
        if bossObj.get_health() > 0:
            # Begin boss attack phase if the boss is still alive.
            boss_attack_phase(summonOne, bossObj)

    # If the player has no hp, then show a defeat screen and exit the program.
    if hostObj.get_health() <= 0:
        print('\nYOU DIED\n')
        time.sleep(1)
        sys.exit(0)

    # If the boss has no hp, then show a victory screen and proceed.
    print('\nENEMY FELLED\n')
    time.sleep(1)
    # Make the rest action interactive for the player.
    input("Press'ENTER' to end journey...")


def single_player_game():
    playerOne = Character() # Create the player object.
    bossOne = Boss()        # Create the boss object.
    playerOne.print_stats() # Display the player's stats.

    tutorial_boss_fight(playerOne, bossOne) # Begin the tutorial boss fight.
    playerOne.grace()   # Rest and heal the player.

    field_boss_fight(playerOne, bossOne)    # Begin the field boss fight.
    playerOne.grace()

    mini_boss_fight(playerOne, bossOne) # Begin the mini boss fight.
    playerOne.grace()

    main_boss_fight(playerOne, bossOne) # Begin the main boss fight.
    
    
def two_player_game():
    host = Character()          # Create the host object.
    summonOne = Character()     # Create the first summon object.
    players = [host, summonOne] # Create the player list.
    bossOne = Boss()    # Create the boss object.

    host.print_stats()          # Display the host's stats.
    print()
    summonOne.print_stats()     # Display the first summon's stats.

    # Begin the tutorial boss fight.
    two_player_tutorial_boss_fight(players, bossOne)    
    host.grace()        # Rest and heal the host.
    summonOne.grace()   # Rest and heal the first summon.
    
    # Begin the field boss fight.
    two_player_field_boss_fight(players, bossOne)
    host.grace()        # Rest and heal the host.
    summonOne.grace()   # Rest and heal the first summon.
    
    # Begin the mini boss fight.
    two_player_mini_boss_fight(players, bossOne)
    host.grace()        # Rest and heal the host.
    summonOne.grace()   # Rest and heal the first summon.
    
    # Begin the main boss fight.
    two_player_main_boss_fight(players, bossOne)
    host.grace()        # Rest and heal the host.
    summonOne.grace()   # Rest and heal the first summon.


def main():
    numOfPlayers = pyip.inputInt(prompt="Enter the number of players. Max 3: ", min=1, max=3)
    
    if numOfPlayers == 1:
        single_player_game()
    elif numOfPlayers == 2:
        two_player_game()
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('\nTHANKS FOR PLAYING!')

