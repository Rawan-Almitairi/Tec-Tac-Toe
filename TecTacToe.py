import random

#create the board:
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# variables:
current_player = ''
gameRunning = False
play_with_computer = False
computer_letter = ''
player_letter = ''

def main():
    global gameRunning, play_with_computer, player_letter, computer_letter, current_player

    print("welcome to Tic Tac Toe game!")
    # choose to play with computer or no
    play_with = input("do you want to play with computer? y/n ").lower()
    if play_with == 'y':
        play_with_computer = True
    # choose the letter
    letter = input("will you use X or O? ").upper()
    while letter not in ['X', 'O']:
        letter = input("invalid input! choose X or O").upper()
    player_letter = letter
    computer_letter = 'X' if letter == 'O' else 'O'

    # choose to start first or not
    who_start = input("do you want to play first? y/n ").lower()
    if who_start == 'y':
        current_player = player_letter
    else:
        current_player = computer_letter

    # run the game:
    gameRunning = True
    while gameRunning:
        displayBoard(board)
        #check the first player
        if current_player == player_letter:
            player_move(board, player_letter)
        else:
            if play_with_computer:
                computer_move(board, computer_letter)
            else:
                player_move(board, current_player)
        #winner:
        if check_win(board, current_player):
            displayBoard(board)
            print(current_player+" wins!")
            gameRunning = False
        elif check_draw(board): #التعادل
            displayBoard(board)
            print("it is a draw!")
            gameRunning = False
        else:
            switching()
    #play again
    play_again = input("do you want to play again? y/n ").lower()
    if play_again == 'y':
        main()

#display the X O board:
def displayBoard(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('----------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('----------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()

#player choice
def player_move(board, letter):
    place_no = int(input("enter a number from 1 to 9: "))
    if place_no >= 1 and place_no <= 9 and board[place_no - 1] == '-':
        board[place_no - 1] = letter
    else:
        print("invalid input or the player in that position")
        player_move(board, letter)

#computer choice
def computer_move(board, letter):
    place_free = [ i for i in range(9) if board[i] == '-']
    place = random.choice(place_free)
    board[place] = letter
    print("computer choose place: ", place+1)

#check the winner
def check_win(board, letter):
    return (
        board[0] == board[1] == board[2] == letter or
        board[3] == board[4] == board[5] == letter or
        board[6] == board[7] == board[8] == letter or
        board[0] == board[3] == board[6] == letter or
        board[1] == board[4] == board[7] == letter or
        board[2] == board[5] == board[8] == letter or
        board[0] == board[4] == board[8] == letter or
        board[2] == board[4] == board[6] == letter
    )

#check draw
def check_draw(board):
    for i in board:
        if i == '-' :
            return False
    return True

#switching the turn
def switching():
    global current_player
    if current_player == player_letter:
        current_player = computer_letter
    else:
        current_player = player_letter

#call the main function to start
main()
