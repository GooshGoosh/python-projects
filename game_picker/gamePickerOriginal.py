#!/usr/bin/env python3
# gamePicker.py - Asks the user to choose a console from a menu then randomly selects a game
# from that console for the user to play.


import pyinputplus as pyip
import random

# Variables to hold paths to game list files:
PS5 = '/home/alexg/Documents/txt-files/ps5-games.txt'
PS4 = '/home/alexg/Documents/txt-files/ps4-games.txt'
PS3 = '/home/alexg/Documents/txt-files/ps3-games.txt'
PS2 = '/home/alexg/Documents/txt-files/ps2-games.txt'
Switch = '/home/alexg/Documents/txt-files/switch-games.txt'
GameCube = '/home/alexg/Documents/txt-files/gamecube-games.txt'
N64 = '/home/alexg/Documents/txt-files/n64-games.txt'
SNES = '/home/alexg/Documents/txt-files/snes-games.txt'

# Menu for the user to select a console:
print('\n')
console = pyip.inputMenu(['PS5', 'PS4', 'PS3', 'PS2', 'Switch', 'GameCube', 'N64', 'SNES'], numbered=True)

if console == 'PS5':
    # Code to select a random game from PS5 list:
    gameFile = open(PS5, 'r')
    gameList = gameFile.readlines()
    gameFile.close()
    print(f'\nYou should play: {random.choice(gameList)}')

if console == 'PS4':
    # Code to select a random game from PS4 list:
    gameFile = open(PS4, 'r')
    gameList = gameFile.readlines()
    gameFile.close()
    print(f'\nYou should play: {random.choice(gameList)}')

if console == 'PS3':
    # Code to select a random game from PS3 list:
    gameFile = open(PS3, 'r')
    gameList = gameFile.readlines()
    gameFile.close()
    print(f'\nYou should play: {random.choice(gameList)}')

if console == 'PS2':
    # Code to select a random game from PS2 list:
    gameFile = open(PS2, 'r')
    gameList = gameFile.readlines()
    gameFile.close()
    print(f'\nYou should play: {random.choice(gameList)}')

if console == 'Switch':
    # Code to select a random game from Switch list:
    gameFile = open(Switch, 'r')
    gameList = gameFile.readlines()
    gameFile.close()
    print(f'\nYou should play: {random.choice(gameList)}')

if console == 'GameCube':
    # Code to select a random game from GameCube list:
    gameFile = open(GameCube, 'r')
    gameList = gameFile.readlines()
    gameFile.close()
    print(f'\nYou should play: {random.choice(gameList)}')

if console == 'N64':
    # Code to select a random game from N64 list:
    gameFile = open(N64, 'r')
    gameList = gameFile.readlines()
    gameFile.close()
    print(f'\nYou should play: {random.choice(gameList)}')

if console == 'SNES':
    # Code to select a random game from SNES list:
    gameFile = open(SNES, 'r')
    gameList = gameFile.readlines()
    gameFile.close()
    print(f'\nYou should play: {random.choice(gameList)}')
