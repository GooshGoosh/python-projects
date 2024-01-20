'''
game_picker_original.py - Chooses a random game from a list of games for the
user-specified console. This is the original version of the program that uses
if statements to check which console the user chose.
'''


import random
import pyinputplus as pyip


# Paths to game list files:
PS5 = 'ps5-games.txt'
PS4 = 'ps4-games.txt'
PS3 = 'ps3-games.txt'
PS2 = 'ps2-games.txt'
SWITCH = 'SWITCH-games.txt'
GAMECUBE = 'GAMECUBE-games.txt'
N64 = 'n64-games.txt'
SNES = 'snes-games.txt'

# Menu for the user to select a console:
print('\n')
console = pyip.inputMenu(['PS5', 'PS4', 'PS3', 'PS2',
                          'SWITCH', 'GAMECUBE', 'N64', 'SNES'],
                         numbered=True)


try:
    if console == 'PS5':
        # Select a random game from PS5 list:
        with open(PS5, 'r', encoding='UTF-8') as file:
            game_list = file.readlines()
        print(f'\nYou should play: {random.choice(game_list)}')

    if console == 'PS4':
        # Select a random game from PS5 list:
        with open(PS4, 'r', encoding='UTF-8') as file:
            game_list = file.readlines()
        print(f'\nYou should play: {random.choice(game_list)}')

    if console == 'PS3':
        # Select a random game from PS5 list:
        with open(PS3, 'r', encoding='UTF-8') as file:
            game_list = file.readlines()
        print(f'\nYou should play: {random.choice(game_list)}')

    if console == 'PS2':
        # Select a random game from PS5 list:
        with open(PS2, 'r', encoding='UTF-8') as file:
            game_list = file.readlines()
        print(f'\nYou should play: {random.choice(game_list)}')

    if console == 'Switch':
        # Select a random game from PS5 list:
        with open(SWITCH, 'r', encoding='UTF-8') as file:
            game_list = file.readlines()
        print(f'\nYou should play: {random.choice(game_list)}')

    if console == 'GameCube':
        # Select a random game from PS5 list:
        with open(GAMECUBE, 'r', encoding='UTF-8') as file:
            game_list = file.readlines()
        print(f'\nYou should play: {random.choice(game_list)}')

    if console == 'N64':
        # Select a random game from PS5 list:
        with open(N64, 'r', encoding='UTF-8') as file:
            game_list = file.readlines()
        print(f'\nYou should play: {random.choice(game_list)}')

    if console == 'SNES':
        # Select a random game from PS5 list:
        with open(SNES, 'r', encoding='UTF-8') as file:
            game_list = file.readlines()
        print(f'\nYou should play: {random.choice(game_list)}')
except FileNotFoundError:
    print(f'\nGame file for {console} not found!\n')
