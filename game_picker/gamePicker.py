#!/usr/bin/env python3

# gamePicker.py - Selects a game from a list for a specific console that is either
# randomly chosen or chosen by the user.


import pyinputplus as pyip
import random


def choose_game(console):
    # Variables to hold paths to game list files.
    ps5 = 'ps5-games.txt'
    ps4 = 'ps4-games.txt'
    ps3 = 'ps3-games.txt'
    ps2 = 'ps2-games.txt'
    switch = 'switch-games.txt'
    gamecube = 'gamecube-games.txt'
    n64 = 'n64-games.txt'
    snes = 'snes-games.txt'

    match console:

        case 'PS5':
            with open(ps5) as file:
                gameList = file.readlines()
                print('\nYou should play: {} on {}'.format(random.choice(gameList).strip(), console))
                file.close()

        case 'PS4':
            with open(ps4) as file:
                gameList = file.readlines()
                print('\nYou should play: {} on {}'.format(random.choice(gameList).strip(), console))
                file.close()

        case 'PS3':
            with open(ps3) as file:
                gameList = file.readlines()
                print('\nYou should play: {} on {}'.format(random.choice(gameList).strip(), console))
                file.close()

        case 'PS2':
            with open(ps2) as file:
                gameList = file.readlines()
                print('\nYou should play: {} on {}'.format(random.choice(gameList).strip(), console))
                file.close()

        case 'Switch':
            with open(switch) as file:
                gameList = file.readlines()
                print('\nYou should play: {} on {}'.format(random.choice(gameList).strip(), console))
                file.close()

        case 'GameCube':
            with open(gamecube) as file:
                gameList = file.readlines()
                print('\nYou should play: {} on {}'.format(random.choice(gameList).strip(), console))
                file.close()

        case 'N64':
            with open(n64) as file:
                gameList = file.readlines()
                print('\nYou should play: {} on {}'.format(random.choice(gameList).strip(), console))
                file.close()

        case 'SNES':
            with open(snes) as file:
                gameList = file.readlines()
                print('\nYou should play: {} on {}'.format(random.choice(gameList).strip(), console))
                file.close()


def main():
    consoleList = ['PS5', 'PS4', 'PS3', 'PS2', 'Switch', 'GameCube', 'N64', 'SNES']

    answer = pyip.inputYesNo(prompt='\nWould you like to choose your console? (Y/N)\n')
    if answer == 'yes':
        gameSystem = pyip.inputMenu(consoleList, prompt='\nChoose your console:\n', numbered=True)
    else:
        gameSystem = random.choice(consoleList)
    
    choose_game(gameSystem)


if __name__ == "__main__":
    main()

