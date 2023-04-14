#!/usr/bin/env python3
playerOneLifePoints = 8000
playerTwoLifePoints = 8000
playerOne = ""
playerTwo = ""

playerOne = input("Enter the initial for player one's first name: ")
playerTwo = input("Enter the initial for player two's first name: ")

while playerTwo.lower() == playerOne.lower():
    print("Player two cannot have the same name as player one.")
    playerTwo = input("Enter the first initial for player two's last name instead: ")

while playerOneLifePoints > 0 and playerTwoLifePoints > 0:
    playerSelect = ""
    increaseDecrease = ""
    lifePoints = 0

    playerSelect = input("Which player is increasing/decreasing their life points? ")
    while (
            playerSelect.lower() != playerOne.lower()
            and playerSelect.lower() != playerTwo.lower()
    ):
        playerSelect = input(
            "Incorrect player initial entered. Please enter another player initial: "
        )
    if playerSelect.lower() == playerOne.lower():
        increaseDecrease = input(
            "Are you increasing or decreasing your life points? I/D: "
        )
        while increaseDecrease.lower() != "i" and increaseDecrease.lower() != "d":
            increaseDecrease = input(
                "Incorrect command. Please enter an 'i' for increasing or a 'd' for decreasing: "
            )
        if increaseDecrease.lower() == "i":
            lifePoints = int(input("How many life points are you gaining? "))
            playerOneLifePoints = playerOneLifePoints + lifePoints
        else:
            lifePoints = int(input("How many life points are you losing?"))
            playerOneLifePoints = playerOneLifePoints - lifePoints

    elif playerSelect.lower() == playerTwo.lower():
        increaseDecrease = input(
            "Are you increasing or decreasing your life points? I/D: "
        )
        while increaseDecrease.lower() != "i" and increaseDecrease.lower() != "d":
            increaseDecrease = input(
                "Incorrect command. Please enter an 'i' for increasing or a 'd' for decreasing: "
            )
        if increaseDecrease.lower() == "i":
            lifePoints = int(input("How many life points are you gaining? "))
            playerTwoLifePoints = playerTwoLifePoints + lifePoints
        else:
            lifePoints = int(input("How many life points are you losing? "))
            playerTwoLifePoints = playerTwoLifePoints - lifePoints

    print(playerOne, " remaining life points: ", playerOneLifePoints)
    print(playerTwo, " remaining life points: ", playerTwoLifePoints)
    if playerOneLifePoints <= 0 or playerTwoLifePoints <= 0:
        break

if playerOneLifePoints <= 0:
    print("Congratulations " + playerTwo + ", you win!")
else:
    print("Congratulations " + playerOne + ", you win!")
