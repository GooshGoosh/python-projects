'''
tic_tac_toe.py - A simple program to allow the user and the computer to play a game
of Tic-Tac-Toe together. The computers plays as 'X' and the user plays as 'O'. The
computer always gets the first move and places it's first 'X' in the center of the
board.
'''


from random import randrange
import pyinputplus as pyip


# A list of lists of spaces for the Tic-Tac-Toe board.
game_board = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

# A dictionary of the free spaces available on the board as well as the coordinates
# of those spaces to access from the game_board variable.
free_spaces = {1: (0, 0), 2: (0, 1), 3: (0, 2),
               4: (1, 0), 5: (1, 1), 6: (1, 2),
               7: (2, 0), 8: (2, 1), 9: (2, 2)}


def display_board(board):
    """Outputs the game board's current status.

    Args:
        board (list): A list of lists containing the 3x3 spaces for the game board.
    """
    print()
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print(f'|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


def enter_move(board, spaces):
    """Gets the user's move, ensures it is valid, then updates the board according
    to the user's decision.

    Args:
        board (list): A list of lists containing the 3x3 spaces for the game board.
        spaces (dict): A dictionary of available spaces on the game board along
        with the coordinates of those spaces.
    """
    global game_board

    valid_move = False

    # Get a space from the user and ensure it is valid.
    while not valid_move:
        move = pyip.inputInt(prompt="Enter your move: ",min=1,max=9)

        # Get the coords for the available space and set the player's letter.
        if move in spaces.keys():
            move = spaces[move]
            board[move[0]][move[1]] = 'O'
            valid_move = True
        else:
            print('Invalid move. Please select an open space.\n')
            continue

    display_board(board)
    make_list_of_free_fields(board)
    game_board = board


def make_list_of_free_fields(board):
    """Builds a list of all the available free spaces on the board.

    Args:
        board (list): A list of lists containing the 3x3 spaces for the game board.
    """
    global free_spaces

    # Empty dictionary to hold the updated free spaces temporarily.
    free = {}

    # Loop through each list in the board and find any spaces that do not contain
    # 'X' or 'O'.
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] == 'X' or board[i][j] == 'O':
                continue
            else:
                free[board[i][j]] = (i, j)  # Add the coordinates to the free spaces.

    free_spaces = free


def draw_move(board, spaces):
    """Draws the computer's move and updates the game board.

    Args:
        board (list): A list of lists containing the 3x3 spaces for the game board.
        spaces (dict): A dictionary of available spaces on the game board along
        with the coordinates of those spaces.
    """
    global game_board

    valid_move = False

    # Start the computer's first move in the middle of the game board.
    if 5 in spaces.keys():
        move = spaces[5]
        board[move[0]][move[1]] = 'X'
    else:
        while not valid_move:
            move = randrange(1, 10)

            # Check if the space on the board is available and, if so, put the
            # computer's next move there.
            if move in spaces.keys():
                move = spaces[move]
                board[move[0]][move[1]] = 'X'
                valid_move = True
            else:
                continue

    display_board(board)
    make_list_of_free_fields(board)
    game_board = board


def victory_for(board, sign):
    """Checks the board's status to see if the player (O) or the computer (X) has
    won the game.

    Args:
        board (list): A list of lists containing the 3x3 spaces for the game board.
        sign (str): The symbol that either the player or the computer is using for
        the game.

    Returns:
        bool: Tells the program that there is a winner and that the game should end.
    """
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
    """The main function to run the program.
    """
    display_board(game_board)
    player_turn = False  # Allow the computer to go first.

    # Continue the loop until there are no more free spaces.
    while len(free_spaces):
        # The player's turn.
        if player_turn:
            enter_move(game_board, free_spaces)
            if victory_for(game_board, 'O'):
                # Exit the loop if there is a winner.
                break
            player_turn = False  # End the player's turn.
        # The computer's turn.
        else:
            draw_move(game_board, free_spaces)
            if victory_for(game_board, 'X'):
                break
            player_turn = True   # End the computer's turn.


if __name__ == "__main__":
    main()
