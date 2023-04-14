from random import randint

playAgain = "y"

while playAgain.lower() == "y":
    theNumber = randint(1, 1000000)
    guess = 0
    tries = 0
    while guess != theNumber:
        guess = int(input("Guess a number between 1 and 1,000,000: "))
        tries = tries + 1
        if guess < theNumber:
            print("\n", guess, " is too low. Try again.")
        elif guess > theNumber:
            print("\n", guess, " is too high. Try again.")
        else:
            print("\n", guess, " is correct! You win!")
    if tries == 1:
        print("Wow! It only took you ", tries, " guess!? Incredible!")
        playAgain = input("Would you like to play again? (y/n)")
    else:
        print("Congratulations! It only took you ", tries, " tries!")
        playAgain = input("Would you like to play again? (y/n)")
        """while(playAgain != 'y' or playAgain != 'n'):
			print("Please type 'y' to play again or 'n' to exit")
			playAgain = input("Would you like to play again? (y/n)")"""
    if playAgain.lower() != "y":
        break
        print("Thank you for playing. Goodbye!")
