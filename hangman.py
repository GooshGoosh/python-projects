#!/usr/bin/env python3
# hangman.py - Plays the classic game 'Hangman'.
# This will take a dictionary of words as a text file and grab a random line (word) from the file.
# The program will then ask the user for input and continue until the user has either (1) correctly guessed the word or
# (2) the user runs out of guesses.

import time
import random
import pyinputplus as pyip
import sys
import os


# Display a greeting message to the user that explains the rules of the game. Then, ask the user if they would like to play the game.
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
    print('\nSee you again!\nExiting...')       # Exit the program if the user does not want to play.
    time.sleep(1)
    sys.exit()


# Create the list of words from a dictionary file and remove the newline (\n) from each word.
with open('/home/dirtypi/Documents/words_alpha.txt') as dictFile:
    hangmanDict = [line.rstrip() for line in dictFile]

# Variables to track the chosen word, letters guessed (correct/incorrect).
hangmanWord = random.choice(hangmanDict).upper()        # Grab a random word from the list to use in the game.
availableLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
incorrectGuesses= []
correctGuesses = []
for i in range(len(hangmanWord)):       # Fill the that tracks correct guesses with "_" to give the user a visual representation of the word length.
    correctGuesses.append("_")
guessLetter = ""                            # Set the initial guess to empty.
wordCount = 0                               # Counter to ask the user if they would like to guess the word after every 3rd letter guess.

print('\nLoading game...\n')                # Load the game.
time.sleep(2)

# Loop to continually ask the user for alpha characters (letters) in the English alphabet.
while "_" in correctGuesses and len(incorrectGuesses) < 6:
    os.system('cls' if os.name == 'nt' else 'clear')                                            # Clear the screen before each guess.
    if wordCount == 3:                                                                          # Ask the user if they would like to solve the word
            wordCount = 0                                                                       # after every 3rd letter guess.
            print('\n\nCorrect letters:')
            for i in range(len(correctGuesses)):                                                # Print the letters that have been correctly guessed.
                print(correctGuesses[i], end=" | ")
            answer = pyip.inputYesNo('\nWould you like to guess the entire word? (Y/N): ')          
        
            if answer == 'yes':
                guessWord = pyip.inputStr('\nPlease type your guess: ')                         # Get the user's input if they would like to solve the word.
                break
            
    while guessLetter not in availableLetters:                                                  # Ensure user inputs a letter that is available to guess.
        print('\n\nAvailable letters:')
        for i in range(len(availableLetters)):                                                  # Print the available letters.
            print(availableLetters[i], end=" | ")
            
        print('\n\nIncorrect letters:')
        for i in range(len(incorrectGuesses)):                                                  # Print the incorrectly guessed letters.
            print(incorrectGuesses[i], end=" | ")
            
        print('\n\nCorrect letters:')
        for i in range(len(correctGuesses)):                                                    # Print the letters that have been correctly guessed.
            print(correctGuesses[i], end=" | ")
               
        guessLetter = input('\n\nPlease enter a letter from the available list: ').upper()      # Get input from the user.
        
    if guessLetter not in hangmanWord:                  # Check if the guessed letter is in the chosen word.
        incorrectGuesses.append(guessLetter)            # If not, add it to the list of incorrect guesses.
    else:
        for i in range(len(hangmanWord)):               # Check where the guessed letter is in the chosen word.
            if hangmanWord[i] == guessLetter:           # If so, add it to the correctGuesses list in the same
                correctGuesses[i] = guessLetter         # position as the chosen word.
        
    availableLetters.remove(guessLetter)                # Remove the guessed letter from the list of available letters.
    wordCount += 1
    time.sleep(1.5)


# Display a win or a loss screen.
os.system('cls' if os.name == 'nt' else 'clear')        # Clear the screen before printing results.
print('\nChecking results...')                          # Let the user know that the results are being printed.
time.sleep(2)
    
if len(incorrectGuesses) >= 6:                          # If the user had 6 incorrect guesses, they lose.
    print('\nYOU LOSE\n')
    time.sleep(1)
elif "_" not in correctGuesses:            # If the user guessed all letters of the word correctly, they win.
    print('\nYOU WIN\n')
    time.sleep(1)
elif guessWord.upper() == hangmanWord:                  # If the user guessed the word correctly, they win.
    print('\nYOU GUESSED THE WORD CORRECTLY\n')
    time.sleep(1)
elif guessWord.upper() != hangmanWord:                  # If the user guessed the word incorrectly, they lose.
    print('\nYOU GUESSED THE WORD INCORRECTLY\n')
    time.sleep(1)

print(f'Hangman word: {hangmanWord}')                   # Print the chosen word.

print('Correct guesses: ')
for i in range(len(correctGuesses)):                    # Print the correct guesses the user made.
    print(correctGuesses[i], end="")
    
print('\n\nIncorrect guesses: ')
for i in range(len(incorrectGuesses)):                  # Print the incorrect guesses the user made.
    print(incorrectGuesses[i], end="")
    
print('\n\nThanks for playing!\nExiting...\n')          # Print a goodbye message for the user.