'''
play_chess.py - A program that takes a chess board (pieces and spaces) and writes
them to a file. The file will be a json file and will be named after both players
followed by the date (mm-dd-yy) that the file was saved. The two player are given
the option to either start a new game or load a game that was previously saved.

If the players decide to load from a previously saved game, they will be given a list
of files in the 'chess-games' directory in the user home directory that will allow
them to type in the file that they would like to load. If the 'chess-games' directory
is not found within the user's home directory, the directory will be created.

The players will take turns and on each turn they will be given two options: move a
piece on a specified space or save and exit the game. If the player chooses to move
a piece on a specified space, they will then be given a prompt to select a space
(piece) that they would like to move and then to choose a space that they would like
to move their piece to. Players will have to select the space that they would like
to interact with that contains the piece that they would like to move. e.g. if the
white queen is on space h3, the player would type in 'h3' and then type in the space
that they would like to move it to such as 'h6'.

If the player chooses the option to save and quit, the program will save the current
board configuration and number of moves for each player to a json file. The current
configuration of the chess board will be printed out to the screen after each player's turn.

WARNING: This program assumes that the player's know how to play chess and intend to
play it fairly without exploiting the program. This program does not check if any
moves made by either player are legal or if the correct player is moving their
intended piece (i.e. the black player moving the white pieces). The program only
ensures that the players interact with legal spaces on the chess board and do not
try to move pieces to and from invalid board spaces such as z7 or r23.
'''

import json
import os
import time
import sys
import datetime
try:
    import pyinputplus as pyip
except ImportError:
    print("\nPlease install the missing module: pyinputplus.")
    sys.exit(1)


def load_board():
    """Loads a default chess board or a previously saved chess board from a file.

    Returns:
        dict, dict, dict: Three dicts that hold the game board spaces/pieces,
        the number of moves each player has taken, and the pieces removed from play
        for each player.
    """
    # Set the path to look for saved chess games.
    user_home = os.path.expanduser('~')
    chess_dir = os.path.abspath(os.path.join(user_home, 'chess-games'))
    board = {}
    moves = {}
    removed_from_play = {}

    # Check if the chess directory already exists and, if not, create it.
    if not os.path.isdir(chess_dir):
        os.makedirs(chess_dir)

    # Check if the players have a saved game file.
    time.sleep(0.5)
    if len(os.listdir(chess_dir)) == 0:
        answer = 'no'
        print('No saved games found.')
        time.sleep(0.25)
    else:
        answer = ''

    while answer != 'yes' and answer != 'no':
        answer = input(
            'Do you have a saved game that you would like to load? (yes/no) > '
            ).lower()

    if answer == 'no':
        print('Loading default chess board...\n')
        time.sleep(1)

        board = {
            'a1': 'wr', 'b1': 'wk', 'c1': 'wb', 'd1': 'WK',
            'e1': 'wq', 'f1': 'wb', 'g1': 'wk', 'h1': 'wr',
            'a2': 'wp', 'b2': 'wp', 'c2': 'wp', 'd2': 'wp',
            'e2': 'wp', 'f2': 'wp', 'g2': 'wp', 'h2': 'wp',
            'a3': '  ', 'b3': '  ', 'c3': '  ', 'd3': '  ',
            'e3': '  ', 'f3': '  ', 'g3': '  ', 'h3': '  ',
            'a4': '  ', 'b4': '  ', 'c4': '  ', 'd4': '  ',
            'e4': '  ', 'f4': '  ', 'g4': '  ', 'h4': '  ',
            'a5': '  ', 'b5': '  ', 'c5': '  ', 'd5': '  ',
            'e5': '  ', 'f5': '  ', 'g5': '  ', 'h5': '  ',
            'a6': '  ', 'b6': '  ', 'c6': '  ', 'd6': '  ',
            'e6': '  ', 'f6': '  ', 'g6': '  ', 'h6': '  ',
            'a7': 'bp', 'b7': 'bp', 'c7': 'bp', 'd7': 'bp',
            'e7': 'bp', 'f7': 'bp', 'g7': 'bp', 'h7': 'bp',
            'a8': 'br', 'b8': 'bk', 'c8': 'bb', 'd8': 'BK',
            'e8': 'bq', 'f8': 'bb', 'g8': 'bk', 'h8': 'br'
        }   # Dictionary for a new, freshly set up chess board.

        moves = {'playerWhite': 0, 'playerBlack': 0}

        removed_from_play = {'removedWhite': [], 'removedBlack': []}

    elif answer == 'yes':
        try:
            print()
            # Output a list of saved games in the chess directory.
            chess_file = pyip.inputMenu(os.listdir(chess_dir), numbered=True,
                                        blank=True,
                                        prompt="Which of these games " \
                                            "would you like to load? " \
                                            "Type in the number that corresponds " \
                                            "to your saved game: \n")

            print('Loading chess board from file...\n')
            with open(os.path.join(chess_dir, chess_file), 'r', encoding='UTF-8') as file:
                chess_dicts = json.load(file)

            for k, v in chess_dicts[0].items():
                board[k] = v

            for k, v in chess_dicts[1].items():
                moves[k] = v

            for k, v in chess_dicts[2].items():
                removed_from_play[k] = v

            time.sleep(1)
        except FileNotFoundError:
            print('A file for the given name was not found.\n')
            sys.exit(1)

    return board, moves, removed_from_play


def save_board(board, moves, removed_pieces, player1, player2):
    """Saves the current game board, the current number of moves for each player
    and the number of moves each player has taken in a file named after the two
    players followed by the date.

    Args:
        board (dict): Dictionary of the game board's spaces and pieces.
        moves (dict): Current number of moves each player has taken.
        removed_pieces (dict): Pieces removed from play for each player.
        player1 (str): The first player's name.
        player2 (str): The second player's name.
    """
    # Set the variables to save the chess game.
    user_home = os.path.expanduser('~')
    chess_dir = os.path.abspath(os.path.join(user_home, 'chess-games'))
    today = datetime.datetime.now()
    format_time = today.strftime("%m-%d-%y")
    file_name = f'{player1.lower()}-{player2.lower()}-chess-{format_time}.json'
    dicts_to_json = [board, moves, removed_pieces]


    print('Saving chess game to file...\n')
    time.sleep(1)

    json_data = json.dumps(dicts_to_json, indent=4)
    with open(os.path.join(chess_dir, file_name), 'w', encoding='UTF-8') as file:
        file.write(json_data)

    print(f'Chess game saved in {chess_dir} as {file_name}')


def print_board(board, removed_pieces, player1, player2):
    """Prints the current status of the game board to the screen.

    Args:
        board (dict): Dictionary of the game board's spaces and pieces.
        removed_pieces (dict): Pieces removed from play for each player.
        player1 (str): The first player's name.
        player2 (str): The second player's name.
    """
    row_num = 8
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'White: {player1}')
    print(f'Black: {player2}')
    print('\n')

    # Create a list of dictionaries for each row of chess board spaces.
    list_of_spaces = [
        {   'a8': board['a8'], 'b8': board['b8'], 'c8': board['c8'], 'd8': board['d8'],
            'e8': board['e8'], 'f8': board['f8'], 'g8': board['g8'], 'h8': board['h8']},
        {   'a7': board['a7'], 'b7': board['b7'], 'c7': board['c7'], 'd7': board['d7'],
            'e7': board['e7'], 'f7': board['f7'], 'g7': board['g7'], 'h7': board['h7']},
        {   'a6': board['a6'], 'b6': board['b6'], 'c6': board['c6'], 'd6': board['d6'],
            'e6': board['e6'], 'f6': board['f6'], 'g6': board['g6'], 'h6': board['h6']},
        {   'a5': board['a5'], 'b5': board['b5'], 'c5': board['c5'], 'd5': board['d5'],
            'e5': board['e5'], 'f5': board['f5'], 'g5': board['g5'], 'h5': board['h5']},
        {   'a4': board['a4'], 'b4': board['b4'], 'c4': board['c4'], 'd4': board['d4'],
            'e4': board['e4'], 'f4': board['f4'], 'g4': board['g4'], 'h4': board['h4']}, 
        {   'a3': board['a3'], 'b3': board['b3'], 'c3': board['c3'], 'd3': board['d3'],
            'e3': board['e3'], 'f3': board['f3'], 'g3': board['g3'], 'h3': board['h3']}, 
        {   'a2': board['a2'], 'b2': board['b2'], 'c2': board['c2'], 'd2': board['d2'],
            'e2': board['e2'], 'f2': board['f2'], 'g2': board['g2'], 'h2': board['h2']},
        {   'a1': board['a1'], 'b1': board['b1'], 'c1': board['c1'], 'd1': board['d1'],
            'e1': board['e1'], 'f1': board['f1'], 'g1': board['g1'], 'h1': board['h1']}     
    ]

    # Print the column headers for the chess board.
    print('  | A  | B  | C  | D  | E  | F  | G  | H  |')
    print('-' * 43)

    # Loop through the list and each dictionary to print the piece that occupies the space
    # or blank if there is no piece present in the space.
    for dict_spaces in list_of_spaces:
        print(f'{row_num} | ', end='')
        row_num -= 1
        for v in dict_spaces.values():
            print(f'{v} | ', end='')
        print('\n' + ('-' * 43))
    print()

    print(f"White pieces removed from play: {', '.join(removed_pieces['removedWhite'])}")
    print(f"Black pieces removed from play: {', '.join(removed_pieces['removedBlack'])}")
    print()


def pawn_promotion(chess_board, pawn_space, player):
    """Promotes a pawn to a piece of the player's choosing.

    Args:
        chess_board (dict): Dictionary of the game board's spaces and pieces.
        pawn_space (dict.key): The key of the space on the board that the pawn is in.
        This will be a key in the chess_board dict.
        player (str): The color of the piece to promote.

    Returns:
        dict: An updated dictionary of the game board's spaces and pieces.
    """
    if player == 'white':
        promotion = pyip.inputMenu(['wq', 'wk', 'wb', 'wr'], numbered=True,
                                   prompt='\nWhat would you like to promote your pawn to?\n')
        chess_board[pawn_space] = promotion
    else:
        promotion = pyip.inputMenu(['bq', 'bk', 'bb', 'br'], numbered=True,
                                   prompt='\nWhat would you like to promote your pawn to?\n')
        chess_board[pawn_space] = promotion

    return chess_board


def chess_turns(chess_board, player_moves, removed_pieces, player_white, player_black):
    """Allows either player to take a turn moving one of their chess pieces.
    Keeps track of the number of moves each player has taken, removed pieces
    that each player has, and the board for the spaces/pieces. Ensures that the
    player using the black pieces does not have more moves than the player using
    the white pieces.

    Args:
        chess_board (dict): Dictionary of the game board's spaces and pieces.
        player_moves (dict): Current number of moves each player has taken.
        removed_pieces (dict): Pieces removed from play for each player.
        player_white (str): The first player's name.
        player_black (str): The second player's name.
    """
    white_final_rank_spaces = ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
    black_final_rank_spaces = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
    piece_moved = ''

    while True:
        if player_moves['playerWhite'] == player_moves['playerBlack']:
            time.sleep(0.75)
            print_board(chess_board, removed_pieces, player_white, player_black)
            print(f'{player_white}\'s turn...\n')
            starting_space = ''
            destination_space = ''
            move = pyip.inputMenu(['Move Piece', 'Save and Exit'], numbered=True)

            if move == 'Move Piece':
                while starting_space not in chess_board.keys():
                    starting_space = pyip.inputStr(prompt='\nType the space that the piece " \
                        "you would like to move resides in (e.g. a2) > ')
                    piece_moved = chess_board[starting_space]

                while destination_space not in chess_board.keys() \
                    and destination_space != starting_space:
                    destination_space = pyip.inputStr(prompt='\nType the space that you would " \
                        "like to move the piece to (e.g. a3) > ')

                if chess_board[destination_space] != '  ':
                    removed_pieces['removedBlack'].append(chess_board[destination_space])
                chess_board[destination_space] = chess_board[starting_space]
                chess_board[starting_space] = '  '

                # Check if a white pawn has reached its final rank and is due for a promotion.
                if piece_moved == 'wp' and destination_space in white_final_rank_spaces:
                    print('\nYour pawn is due for a promotion!')
                    time.sleep(0.75)
                    chess_board = pawn_promotion(chess_board, destination_space, player='white')
                    removed_pieces['removedWhite'].append(piece_moved)

                player_moves['playerWhite'] += 1
            else:
                save_board(chess_board, player_moves, removed_pieces, player_white, player_black)
                sys.exit(0)

        elif player_moves['playerWhite'] > player_moves['playerBlack']:
            time.sleep(0.75)
            print_board(chess_board, removed_pieces, player_white, player_black)
            print(f'{player_black}\'s turn...\n')
            starting_space = ''
            destination_space = ''
            move = pyip.inputMenu(['Move Piece', 'Save and Exit'], numbered=True)

            if move == 'Move Piece':
                while starting_space not in chess_board.keys():
                    starting_space = pyip.inputStr(prompt='\nType the space that the piece " \
                        "you would like to move resides in (e.g. a7) > ')
                    piece_moved = chess_board[starting_space]

                while destination_space not in chess_board.keys() \
                    and destination_space != starting_space:
                    destination_space = pyip.inputStr(prompt='\nType the space that you would " \
                        "like to move the piece to (e.g. a6) > ')

                if chess_board[destination_space] != '  ':
                    removed_pieces['removedWhite'].append(chess_board[destination_space])
                chess_board[destination_space] = chess_board[starting_space]
                chess_board[starting_space] = '  '

                # Check if a black pawn has reached its final rank and is due for a promotion.
                if piece_moved == 'bp' and destination_space in black_final_rank_spaces:
                    print('\nYour pawn is due for a promotion!')
                    time.sleep(0.75)
                    chess_board = pawn_promotion(chess_board, destination_space, player='black')
                    removed_pieces['removedBlack'].append(piece_moved)

                player_moves['playerBlack'] += 1
            elif move == 'Save and Exit':
                save_board(chess_board, player_moves, removed_pieces, player_white, player_black)
                sys.exit(0)
        else:
            print('\nERROR: Black has more moves taken than White! Exiting program with an error!')
            sys.exit(1)


def main():
    """Main function to run the program.
    """
    # Clear the screen and get player names for white/black.
    os.system('cls' if os.name == 'nt' else 'clear')
    player_white = input('Enter a player name for White: ')
    time.sleep(0.5)
    player_black = input('Enter a player name for Black: ')
    time.sleep(0.5)
    print(f'Player 1: {player_white}')
    print(f'Player 2: {player_black}')

    chess_board, player_moves, removed_pieces = load_board()
    chess_turns(chess_board, player_moves, removed_pieces, player_white, player_black)


if __name__ == "__main__":
    main()
