#!/usr/bin/env python3


import sys
try:
    import pyinputplus as pyip
except ImportError:
    print("\nPlease install the missing module: pyinputplus.")
    sys.exit(1)


class Player():
    def __init__(self):
        self.__name = pyip.inputStr(prompt="Enter the player's first name: ")
        self.__lifePoints = 8000
        
    def get_name(self):
        return self.__name
        
    def get_lp(self):
        return self.__lifePoints
    
    def damage_lp(self, damage):
        self.__lifepoints -= damage
        
    def recover_lp(self, healing):
        self__lifepoints += healing
        
        
def player_take_damage(player, damage):
    player.damage_lp(damage)
    
    
def player_recover_lp(player, healing):
    player.recover_lp(healing)
    
    
def main():
    playerOne = Player()
    playerTwo = Player()
    playerOneLP = playerOne.get_lp()
    playerTwoLP = playerTwo.get_lp()
    
    while playerOneLP > 0 and playerTwoLP > 0:
        print('\n' + '-' * 30)
        choice = pyip.inputMenu(['Damage LP', 'Recover LP', 'Surrender'],
                                prompt="\nChoose an action:\n",
                                numbered=True)
        
        match choice:
            case 'Surrender':
                loser = pyip.inputMenu(prompt="\nWho is surrendering?\n",
                                   numbered=True)
            
                if loser == playerOne.get_name():
                    print('\n{} wins!'.format(playerTwo.get_name()))
                else:
                    print('\n{} wins!'.format(playerOne.get_name()))
                    
                sys.exit(0)

            case 'Damage LP':
                player = pyip.inputMenu([playerOne.get_name(),
                                         playerTwo.get_name()],
                                        prompt="\nWhich player is taking damage:\n",
                                        numbered=True)
                damage = pyip.inputInt(prompt="\nEnter the damage amount: ")
                player.damage_lp(damage)
                playerOneLP = playerOne.get_lp()
                playerTwoLP = playerTwo.get_lp()
                
            case 'Recover LP':
                player = pyip.inputMenu([playerOne.get_name(),
                                         playerTwo.get_name()],
                                        prompt="\nWhich player is recovering LP:\n",
                                        numbered=True)
                damage = pyip.inputInt(prompt="\nEnter the healing amount: ")
                player.recover_lp(healing)
                playerOneLP = playerOne.get_lp()
                playerTwoLP = playerTwo.get_lp()
            
    if playerOne.get_lp() > 0:
        print('\n{} wins!'.format(playerOne.get_name()))
    else:
        print('\n{} wins!'.format(playerTwo.get_name()))
        

if __name__ == "__main__":
    main()
