'''
game_picker.py - Chooses a random game from a list of games for the user-specified
console. This is the updated version of the program that uses match-case statements
to check which console the user chose.
'''


import random
import pyinputplus as pyip


# Paths to game files.
PS5 = 'ps5-games.txt'
PS4 = 'ps4-games.txt'
PS3 = 'ps3-games.txt'
PS2 = 'ps2-games.txt'
SWITCH = 'SWITCH-games.txt'
GAMECUBE = 'GAMECUBE-games.txt'
N64 = 'n64-games.txt'
SNES = 'snes-games.txt'

def choose_game(console):
    """Chooses a random game from the game list for the specified value in console.

    Args:
        console (str): The console to choose a random game for.
    """
    match console:

        case 'PS5':
            with open(PS5, 'r', encoding='UTF-8') as file:
                game_list = file.readlines()
                print(f'\nYou should play: {random.choice(game_list).strip()} on {console}')
                file.close()

        case 'PS4':
            with open(PS4, 'r', encoding='UTF-8') as file:
                game_list = file.readlines()
                print(f'\nYou should play: {random.choice(game_list).strip()} on {console}')
                file.close()

        case 'PS3':
            with open(PS3, 'r', encoding='UTF-8') as file:
                game_list = file.readlines()
                print(f'\nYou should play: {random.choice(game_list).strip()} on {console}')
                file.close()

        case 'PS2':
            with open(PS2, 'r', encoding='UTF-8') as file:
                game_list = file.readlines()
                print(f'\nYou should play: {random.choice(game_list).strip()} on {console}')
                file.close()

        case 'Switch':
            with open(SWITCH, 'r', encoding='UTF-8') as file:
                game_list = file.readlines()
                print(f'\nYou should play: {random.choice(game_list).strip()} on {console}')
                file.close()

        case 'GameCube':
            with open(GAMECUBE, 'r', encoding='UTF-8') as file:
                game_list = file.readlines()
                print(f'\nYou should play: {random.choice(game_list).strip()} on {console}')
                file.close()

        case 'N64':
            with open(N64, 'r', encoding='UTF-8') as file:
                game_list = file.readlines()
                print(f'\nYou should play: {random.choice(game_list).strip()} on {console}')
                file.close()

        case 'SNES':
            with open(SNES, 'r', encoding='UTF-8') as file:
                game_list = file.readlines()
                print(f'\nYou should play: {random.choice(game_list).strip()} on {console}')
                file.close()


def main():
    """The main function to run for the program.
    """
    console_list = ['PS5', 'PS4', 'PS3', 'PS2', 'SWITCH', 'GAMECUBE', 'N64', 'SNES']

    answer = pyip.inputYesNo(prompt='\nWould you like to choose your console? (Y/N)\n')
    if answer == 'yes':
        game_system = pyip.inputMenu(console_list, prompt='\nChoose your console:\n',
                                     numbered=True)
    else:
        game_system = random.choice(console_list)

    choose_game(game_system)


if __name__ == "__main__":
    main()
