'''
hangman.py - Plays the classic game 'Hangman'.
This will take a list of words as a text file and grab a random line (word)
from the file. The program will then ask the user for input and continue until
the user has either (1) correctly guessed the word or (2) the user runs out of guesses.
'''


import time
import random
import sys
import os
import pyinputplus as pyip


PATH_TO_WORD_FILE = ""


# Display a greeting message to the user that explains the rules of the game.
# Then, ask the user if they would like to play the game.
print('''\n\n
HELLO AND WELCOME TO HANGMAN!!!
The rules of the game are as follows:
  (1) A random word will be chosen from an English dictionary.
  (2) Your goal is to guess the word one letter at a time.
  (3) You can choose to solve the entire word at once if you choose, however, you only get 1 chance to do so.
  (4) You have a maximum of 6 incorrect guesses.
  (5) If you run out of incorrect guesses or you fail to solve to entire word, you lose.      
      \n\n''')

answer = pyip.inputYesNo('Would you like to play the game? (Y/N): ')
if answer == 'no':
    print('\nSee you again!\nExiting...')
    time.sleep(1)
    sys.exit()


# Create the list of words from a dictionary file.
with open(PATH_TO_WORD_FILE, 'r', encoding='UTF-8') as file:
    hangman_dict = [line.rstrip() for line in file]

# Variables to track the chosen word, letters guessed (correct/incorrect).
hangman_word = random.choice(hangman_dict).upper()
available_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                     'Y', 'Z']
incorrect_guesses= []
correct_guesses = []

# Give the user a visual representation of the word length.
for i in range(len(hangman_word)):
    correct_guesses.append("_")
guess_letter = ""
word_count = 0

print('\nLoading game...\n')
time.sleep(2)

# Loop to continually ask the user for alpha characters (letters) in the English alphabet.
while "_" in correct_guesses and len(incorrect_guesses) < 6:
    os.system('cls' if os.name == 'nt' else 'clear')    # Clear the screen before each guess.

    # Ask the user if they would like to guess the word after every 3rd guess.
    if word_count == 3:
        word_count = 0
        print('\n\nCorrect letters:')
        for letter in correct_guesses:
            print(letter, end=" | ")
        answer = pyip.inputYesNo('\nWould you like to guess the entire word? (Y/N): ')          

        if answer == 'yes':
            guess_word = pyip.inputStr('\nPlease type your guess: ')
            break

    # Ensure the user enters a letter that is available.
    while guess_letter not in available_letters:
        print('\n\nAvailable letters:')
        for letter in available_letters:
            print(letter, end=" | ")

        print('\n\nIncorrect letters:')
        for letter in incorrect_guesses:
            print(letter, end=" | ")

        print('\n\nCorrect letters:')
        for letter in correct_guesses:
            print(letter, end=" | ")

        guess_letter = input('\n\nPlease enter a letter from the available list: ').upper()

    # Check if the guessed letter is in the chosen word.
    if guess_letter not in hangman_word:
        incorrect_guesses.append(guess_letter)
    else:
        # Add the letter to the correct_guesses list at the same position(s)
        # as it appears in the chosen word.
        for i, letter in enumerate(hangman_word):
            if letter == guess_letter:
                correct_guesses[i] = guess_letter

    available_letters.remove(guess_letter)
    word_count += 1
    time.sleep(1.5)


# Display a win or a loss screen.
os.system('cls' if os.name == 'nt' else 'clear')
print('\nChecking results...')
time.sleep(2)

if len(incorrect_guesses) >= 6:
    print('\nYOU LOSE\n')
    time.sleep(1)
elif "_" not in correct_guesses:
    print('\nYOU WIN\n')
    time.sleep(1)
elif guess_word.upper() == hangman_word:
    print('\nYOU GUESSED THE WORD CORRECTLY\n')
    time.sleep(1)
elif guess_word.upper() != hangman_word:
    print('\nYOU GUESSED THE WORD INCORRECTLY\n')
    time.sleep(1)

print(f'Hangman word: {hangman_word}')

print('Correct guesses: ')
for letter in correct_guesses:
    print(letter, end="")

print('\n\nIncorrect guesses: ')
for letter in incorrect_guesses:
    print(letter, end="")

print('\n\nThanks for playing!\nExiting...\n')
