'''
life_point_calculator.py - A simple CLI life point calculator for keeping track
of life point values for two players in a Yu-Gi-Oh duel.
'''


player_one_life_points = 8000
player_two_life_points = 8000

# Get player names.
PLAYER_ONE = input("Enter the initial for player one's first name: ")
PLAYER_TWO = input("Enter the initial for player two's first name: ")

while PLAYER_TWO.lower() == PLAYER_ONE.lower():
    print("\nPlayer two cannot have the same name as player one.")
    PLAYER_TWO = input("Enter the first initial for player two's last name instead: ")

# Continue loop until one player runs out of life points.
while player_one_life_points > 0 and player_two_life_points > 0:
    player_select = input(
        "\nWhich player is increasing/decreasing their life points? "
        )

    while (
            player_select.lower() != PLAYER_ONE.lower()
            and player_select.lower() != PLAYER_TWO.lower()
    ):
        player_select = input(
            "Incorrect player initial entered. Please enter another player initial: "
        )

    # Increase or decrease player one's life points.
    if player_select.lower() == PLAYER_ONE.lower():
        action = input(
            "Are you increasing or decreasing your life points? I/D: "
        )
        while action.lower() != "i" and action.lower() != "d":
            action = input(
                "Incorrect command. " \
                "Please enter an 'i' for increasing or a 'd' for decreasing: "
            )
        if action.lower() == "i":
            life_points = int(input("How many life points are you gaining? "))
            player_one_life_points = player_one_life_points + life_points
        else:
            life_points = int(input("How many life points are you losing?"))
            player_one_life_points = player_one_life_points - life_points

    # Increase or decrease player two's life points.
    elif player_select.lower() == PLAYER_TWO.lower():
        action = input(
            "Are you increasing or decreasing your life points? I/D: "
        )
        while action.lower() != "i" and action.lower() != "d":
            action = input(
                "Incorrect command. " \
                "Please enter an 'i' for increasing or a 'd' for decreasing: "
            )
        if action.lower() == "i":
            life_points = int(input("How many life points are you gaining? "))
            player_two_life_points = player_two_life_points + life_points
        else:
            life_points = int(input("How many life points are you losing? "))
            player_two_life_points = player_two_life_points - life_points

    print(f'{PLAYER_ONE} remaining life points: {player_one_life_points}')
    print(f'{PLAYER_TWO} remaining life points: {player_two_life_points}')

    if player_one_life_points <= 0 or player_two_life_points <= 0:
        break

if player_one_life_points <= 0:
    print(f'Congratulations {PLAYER_TWO}, you win!')
else:
    print(f'Congratulations {PLAYER_ONE}, you win!')
