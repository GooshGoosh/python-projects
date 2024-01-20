'''
high_low_game.py - Selects a random number from 1 to 10 and asks the user to guess
the selected number. Gives hints to the user if they are too high or too low with
their guessed number.
'''
from random import randint
import pyinputplus as pyip

play_again = "y"

while play_again.lower() == "y":
    num = randint(1, 10)
    guess = 0
    tries = 0
    while guess != num:
        guess = pyip.inputInt(prompt="Guess a number between 1 and 10: ")
        tries += 1
        if guess < num:
            print(f'\n {guess} is too low. Try again.')
        elif guess > num:
            print(f'\n {guess} is too high. Try again.')
        else:
            print(f'\n {guess} is correct! You win!')
    if tries == 1:
        print("Amazing! You guessed the secret number on the first try!")
        play_again = pyip.inputYesNo(prompt="Would you like to play again? y/n: ")
    else:
        print(f'Congratulations! It only took you {tries} tries!')
        play_again = pyip.inputYesNo(prompt="Would you like to play again? y/n: ")

print("Thank you for playing. Goodbye!")
