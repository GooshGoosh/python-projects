#!/usr/bin/env python3

# ticTacToe.py - A simple program to allow the user and the computer to play a game
# of Tic-Tac-Toe together. The computer plays as 'X' and the user plays as 'O'. The
# computer always gets the first move and places it's first 'X' in the center of the 
# board. 


import pyinputplus as pyip
from random import randrange


# A list of lists of spaces for the Tic-Tac-Toe board.
gameBoard = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
# A dictionary of the free spaces available on the board as well as the coordinates
# those spaces to access from the gameBoard variable.
freeSpaces = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2)}


def display_board(board):
    # Take the board's current status and print it out to the console.
    print()
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   {}   |   {}   |   {}   |'.format(board[0][0], board[0][1], board[0][2]))
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   {}   |   {}   |   {}   |'.format(board[1][0], board[1][1], board[1][2]))
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   {}   |   {}   |   {}   |'.format(board[2][0], board[2][1], board[2][2]))
    print('|       |       |       |')
    print('+-------+-------+-------+')


def enter_move(board, spaces):
    # Asks the user for their move, checks the input, and updates the board according to
    # the user's decision.
    global gameBoard

    # Ensure the user performs a valid move.
    validMove = False

    while validMove == False:
        move = pyip.inputInt(prompt="Enter your move: ",min=1,max=9)    # Get a space from user.
        if move in spaces.keys():   # Ensure that the space is available on the board.
            move = spaces[move]     # Grab the coordinates for the available space.
            board[move[0]][move[1]] = 'O'   # Set the letter for the player in the chosen space.
            validMove = True    # Exit the loop.
        else:
            print('Invalid move. Please select an open space.\n')
            continue

    display_board(board)                # Display the updated board.
    make_list_of_free_fields(board)     # Update the free spaces.
    gameBoard = board                   # Update the game board.


def make_list_of_free_fields(board):
    # Builds a list of all the available free squares on the board.
    global freeSpaces
    
    # Empty dictionary to hold the updated free spaces temporarily.
    free = {}

    # Loop through each list in the board and find any spaces that do not contain 'X' or 'O'.
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'X' or board[row][col] == 'O':
                continue
            else:
                free[board[row][col]] = (row, col)  # Add the coordinates to the free spaces.

    freeSpaces = free   # Update the freeSpaces dictionary.


def draw_move(board, spaces):
    # Draw's the computer's move and updates the board.
    global gameBoard

    # ENsure the computer performs a valid move.
    validMove = False

    # Start the computer's first move in the middle of the game board.
    if 5 in spaces.keys():
        move = spaces[5]
        board[move[0]][move[1]] = 'X'
    else:
        while validMove == False:
            move = randrange(1, 10)     # Get a random number from 1-9.
            if move in spaces.keys():   # Check if that space on the board is available and,
                move = spaces[move]     # if so, put the computer's next move there.
                board[move[0]][move[1]] = 'X'
                validMove = True    # Exit the loop.
            else:
                continue

    display_board(board)                # Display the updated board.
    make_list_of_free_fields(board)     # Update the free spaces.
    gameBoard = board                   # Update the game board.


def victory_for(board, sign):
    # Checks the board's status to see if the player using 'O's or 'X's has won the game.
    # Loop through the list of lists 3 times.
    for rc in range(3):
        # Check the rows for 3 'O's or 3 'X's.
        if board[rc][0] == sign and board[rc][1] == sign and board[rc][2] == sign:
            if sign == 'O':
                print('\nThe player wins!')
            else:
                print('\nThe computer wins!')
            return True  # End the game.
        # Check the columns for 3 'O's or 3 'X's.
        if board [0][rc] == sign and board[1][rc] == sign and board[2][rc] == sign:
            if sign == 'O':
                print('\nThe player wins!')
            else:
                print('\nThe computer wins!')
            return True
        # Check the first cross-section (diagonal) for 3 'O's or 3 'X's.
        if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            if sign == 'O':
                print('\nThe player wins!')
            else:
                print('\nThe computer wins!')
            return True
        # Check the second cross-section (diagonal) fro 3 'O's or 3 'X's.
        if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            if sign == 'O':
                print('\nThe player wins!')
            else:
                print('\nThe computer wins!')
            return True
    return False  # Do not end the game if there are no 3-in-a-row matches.


def main():
    display_board(gameBoard)
    playerTurn = False  # Allow the computer to go first.

    # Continue the loop until there are no more free spaces.
    while len(freeSpaces):
        # The player's turn.
        if playerTurn == True:
            enter_move(gameBoard, freeSpaces)   # Player makes a move.
            if victory_for(gameBoard, 'O'):     # Check if the player has won.
                break   # Exit the loop if there is a winner.
            playerTurn = False  # End the player's turn.
        # The computer's turn.
        else:
            draw_move(gameBoard, freeSpaces)    # Computer makes a move.
            if victory_for(gameBoard, 'X'):     # Check if the computer has won.
                break   # Exit the loop if there is a winner.
            playerTurn = True   # End the computer's turn.


if __name__ == "__main__":
    main()

