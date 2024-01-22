'''
life_point_calculator_oop.py - A simple CLI life point calculator for keeping track
of life point values for two players in a Yu-Gi-Oh duel. Similar function as the
life_point_calculator.py programs but uses object-oriented programming (OOP) concepts.
'''


import sys
try:
    import pyinputplus as pyip
except ImportError:
    print("\nPlease install the missing module: pyinputplus.")
    sys.exit(1)


class Player():
    """A class used to represent a player in a Yu-Gi-Oh duel.
    
    Attributes
    ----------
    _name: str
        The name of the player.
    _life_points: int
        The amount of life points the player has.
        
    Methods
    -------
    get_name()
        Returns the name of the player.
    get_lp()
        Returns the life points of the player.
    damage_lp(damage=0)
        Reduces the player's life points based on the given damage value.
    recover_lp(healing=0)
        Increases the player's life points based on the given healing value.
    """

    def __init__(self):
        # Get the player's name and set their life point starting value.
        self._name = pyip.inputStr(prompt="Enter the player's first name: ")
        self._life_points = 8000

    def get_name(self):
        """Returns the player's name.

        Returns:
            str: The player's name.
        """
        return self._name

    def get_lp(self):
        """Returns the player's life point value.

        Returns:
            int: The player's current life point value.
        """
        return self._life_points

    def damage_lp(self, damage = 0):
        """Reduces the player's life points based on the given damage value.

        Args:
            damage (int, optional): The number of life points to take away from
            the player's current life point value. Defaults to 0.
        """
        self._life_points -= damage

    def recover_lp(self, healing = 0):
        """Increases the player's life points based on the given healing value.

        Args:
            healing (int, optional): The number of life points to add to the player's
            current life point value. Defaults to 0.
        """
        self._life_points += healing


def player_take_damage(player, damage = 0):
    """Reduce the life point value of the chosen player by the damage value given.

    Args:
        player (Player): Player object to take life points from.
        damage (int, optional): The number of life points to take away from
        the player's current life point value. Defaults to 0.
    """
    player.damage_lp(damage)


def player_recover_lp(player, healing = 0):
    """Increase the life point value of the chosen player by the damage value given.

    Args:
        player (Player): Player object to add life points to.
        healing (int, optional): The number of life points to add to the player's
        current life point value. Defaults to 0.
    """
    player.recover_lp(healing)


def main():
    """Main function to run the program.
    """
    PLAYER_ONE = Player()
    PLAYER_TWO = Player()

    PLAYER_ONE_NAME = PLAYER_ONE.get_name()
    PLAYER_TWO_NAME = PLAYER_TWO.get_name()
    player_one_lp = PLAYER_ONE.get_lp()
    player_two_lp = PLAYER_TWO.get_lp()

    while player_one_lp > 0 and player_two_lp > 0:
        print('\n' + '-' * 30)
        choice = pyip.inputMenu(['Damage LP', 'Recover LP', 'Surrender'],
                                prompt="\nChoose an action:\n",
                                numbered=True)

        match choice:
            case 'Surrender':
                loser = pyip.inputMenu([PLAYER_ONE_NAME, PLAYER_TWO_NAME],
                                       prompt="\nWho is surrendering?\n",
                                       numbered=True)

                if loser == PLAYER_ONE_NAME:
                    print(f'\n{PLAYER_TWO_NAME} wins!')
                else:
                    print(f'\n{PLAYER_ONE_NAME} wins!')

                sys.exit(0)

            case 'Damage LP':
                player = pyip.inputMenu([PLAYER_ONE.get_name(),
                                         PLAYER_TWO.get_name()],
                                        prompt="\nWhich player is taking damage:\n",
                                        numbered=True)
                damage = pyip.inputInt(prompt="\nEnter the damage amount: ")
                player.damage_lp(damage)
                player_one_lp = PLAYER_ONE.get_lp()
                player_two_lp = PLAYER_TWO.get_lp()

            case 'Recover LP':
                player = pyip.inputMenu([PLAYER_ONE.get_name(),
                                         PLAYER_TWO.get_name()],
                                        prompt="\nWhich player is recovering LP:\n",
                                        numbered=True)
                healing = pyip.inputInt(prompt="\nEnter the healing amount: ")
                player.recover_lp(healing)
                player_one_lp = PLAYER_ONE.get_lp()
                player_two_lp = PLAYER_TWO.get_lp()

    if player_one_lp > 0:
        print(f'\n{PLAYER_ONE_NAME} wins!')
    else:
        print(f'\n{PLAYER_TWO_NAME} wins!')


if __name__ == "__main__":
    main()
