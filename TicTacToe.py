# Tic Tac Toe

# This was a small project for the udemy course, Complete Python Bootcamp by Jose Portilla


import random

# Function to print the game board, as a list, where each index 1-9 corresponds
#   with a number on a numpad.  3 by 3 board.

#from IPython.display import clear_output  # for jupyter notebook only

def display_board(board):

    print('\n'*10)      # instead of clear_output() to "refresh" the board
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    

#test_board = [' ']*10
#display_board(test_board)

# Function that can take in a player input and assign marker as 'X' or 'O'

def player_input():

    marker= ''

    # KEEP ASKING PLAYER 1 to choose X or O

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()

    # ASSIGN PLAYER 2, the opposite marker
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return(player1,player2)


# Function that takes in the board list object, a marker ('X' or 'O'), and
#   a desired position (number 1-9) and assigns it to the board.

def place_marker(board, marker, position):

    board[position] = marker


# Function that takes in a board and a mark (X or O) and then checks to see if
#   that mark makes them win the game.

def win_check(board, mark):

    # Winning stipulation

    # ALL ROWS, and check to see if they all share same marker.
    return ((board[1] == mark and board[2] == mark and board[3] == mark ) or
    (board[4] == mark and board[5] == mark and board[6] == mark ) or
    (board[7] == mark and board[8] == mark and board[9] == mark ) or
    # ALL COLUMNS, and check to see if marker matches
    (board[9] == mark and board[6] == mark and board[3] == mark ) or
    (board[8] == mark and board[5] == mark and board[2] == mark ) or
    (board[7] == mark and board[4] == mark and board[1] == mark ) or
    # 2 diagonals, check to see match.
    (board[9] == mark and board[5] == mark and board[1] == mark ) or
    (board[7] == mark and board[5] == mark and board[3] == mark ))
   

# Function to randomly choose who goes first   
def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


# Function to check if the space chosen is open
def space_check(board,position):

    return board[position] == ' '


# Checks if the board is full
def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False

    # BOARD IS FULL IF WE RETURN TRUE
    return True


# Function to take in the player's position choice, while also using space_check()
def player_choice(board):

    position = 0 

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))

    return position


# Asks if the user want's to play the game again.
def replay():

    choice = input("Play again? Enter Yes or No")

    return choice == 'Yes'


print('Welcome to Tic Tac Toe!')

# This while loop is where the actual game logic is coded

while True:

    ## set everything up (board, player1, player 2, choose markers X or O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    ## GAME PLAY
    
    while game_on:

        if turn == "Player 1":

            # show board
            display_board(the_board)

            # choose a position
            position = player_choice(the_board)

            # place marker on position
            place_marker(the_board,player1_marker, position)

            # check if theyw on
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = "Player 2"

        else:
            # show board
            display_board(the_board)

            # choose a position
            position = player_choice(the_board)

            # place marker on position
            place_marker(the_board,player2_marker, position)

            # check if theyw on
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = "Player 1"
        
            # if neither, next player's turn



    if not replay():
        break