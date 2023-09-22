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

        # "Load" the class and clear the screen.
        print('Loading class...')
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

        # Join the path to the classes .json files and the chosen class to get
        # the .json file for the chosen class and load the json file data into
        # classData.
        jsonFile = open(os.path.join(Character.__classesPath,
                                    self.__character.lower() + '.json'))
        self.__classData = json.load(jsonFile)
        jsonFile.close()

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
        with open(Character.__starterWeaponsPath) as jsonFile:
            self.__weaponReader = json.load(jsonFile)

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
        print('\nTarnished')
        print('HP: {}'.format(self.__playerCurrentHealth))

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
        with open(os.path.join(Boss.__bossesPath,
                               'field-boss-list.txt')) as bossFile:
            bossList = bossFile.readlines()
            # Use a random choice from the boss list for the boss name.
            self.__bossName = random.choice(bossList).rstrip()

    def set_mini_boss(self):
        # Set the boss stats for a mini boss.
        self.__bossHealth = 800
        self.__bossAttack = 20
        self.__bossArmor = 11

        # Read the mini boss list file and create a list of mini bosses.
        with open(os.path.join(Boss.__bossesPath,
                               'mini-boss-list.txt')) as bossFile:
            bossList = bossFile.readlines()
            # Use a random choice from the boss list for the boss name.
            self.__bossName = random.choice(bossList).rstrip()

    def set_main_boss(self):
        # Set the boss stats for the main boss.
        self.__bossHealth = 1200
        self.__bossAttack = 25
        self.__bossArmor = 13

        # Read the main boss list file and create a list of main bosses.
        with open(os.path.join(Boss.__bossesPath,
                               'main-boss-list.txt')) as bossFile:
            bossList = bossFile.readlines()
            # Use a random choice from the boss list for the boss name.
            self.__bossName = random.choice(bossList).rstrip()

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



def main():
    # TEST DATA #
    playerOne = Character()
    playerOne.print_stats()
    print(playerOne.get_armor())
    print(playerOne.get_health())
    #playerOne.grace()
    #print(playerOne.attack(69))
    #playerOne.reduce_health(20)
    #print(playerOne.get_health())
    playerOne.print_health()

    bossOne = Boss()
    bossOne.print_stats()
    #print(bossOne.get_armor())
    #print(bossOne.attack(69))
    #bossOne.reduce_health(20)
    bossOne.set_field_boss()
    bossOne.print_stats()
    bossOne.set_mini_boss()
    bossOne.print_stats()
    bossOne.set_main_boss()
    bossOne.print_stats()
    # TEST DATA #


main()
