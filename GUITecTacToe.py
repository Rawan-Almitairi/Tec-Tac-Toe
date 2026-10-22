from tkinter import *
from tkinter import messagebox
import copy

# create the window
top = Tk()
top.title("Tic Tac Toe")
buttons = {}
# board: (Dict)
board = {
    i: '' for i in range(1,10)
}

current_player = 'X'
computer_letter = 'O'
player_letter = 'X'
play_computer = True

# click to add X or O
def click(i):
    global current_player, computer_letter
    if board[i]== '':
        board[i] = current_player
        buttons[i]['text'] = current_player
        #win
        if check_win(board, current_player):
            messagebox.showinfo('Game over', current_player + " win!")
            ask_play()
            return
        #draw
        elif check_draw(board):
            messagebox.showinfo('Game over', " draw!")
            ask_play()
            return
        # switching the turns
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

        if play_computer and current_player == computer_letter:
            top.after(300, computer_move)

# check who win
def check_win(board,letter):
    wins = [
        (1,2,3),(4,5,6),(7,8,9),
        (1,4,7),(2,5,8),(3,6,9),
        (1,5,9),(3,5,7)
    ]
    for winn in wins:
        if board[winn[0]] == board[winn[1]] == board[winn[2]] == letter:
            return True
    return False

# check if it draw
def check_draw(board):
    for i in board:
        if board[i] == '' :
            return False
    return True

# play again
def restart_game():
    global current_player, board
    board = {
        i: '' for i in range(1, 10)
    }
    current_player = 'X'
    for i in buttons:
        buttons[i]['text'] = ''
    init_game()

def ask_play():
    # ask to play again
    if messagebox.askyesno('Game Over', 'Do you want to play again?'):
        restart_game()
    else:
        top.quit()

# play with computer smart AI
def computer_move():
    global computer_letter
    # win
    for i in board:
        if board[i] == '':
            copy = board.copy()
            copy[i] = computer_letter
            if check_win(copy, computer_letter):
                click(i)
                return
    for i in board:
        if board[i] == '':
            copy = board.copy()
            copy[i] = player_letter
            if check_win(copy, player_letter):
                click(i)
                return
    # corners
    for i in [1,3,7,9]:
        if board[i] == '':
            click(i)
            return
    #center
    if board[5] == '':
        click(5)
        return
    # any place
    for i in board:
        if board[i] == '':
            click(i)
            return

def init_game():
    global current_player, player_letter, computer_letter, play_computer
    play_computer = messagebox.askyesno('Play', 'play with computer?')
    letter = messagebox.askyesno('Letter', 'choose X?')
    if letter:
        player_letter = 'X'
        computer_letter = 'O'
    else:
        player_letter = 'O'
        computer_letter = 'X'

    Start_play = messagebox.askyesno('Start', 'Do you to start first?')
    current_player = player_letter if Start_play else computer_letter

    if play_computer and current_player == computer_letter:
        top.after(300, computer_move)

#create 9 btns (to be the board of the game)
for i in range(1, 10):
    btn = Button(top, text='', width=10, height=4, command=lambda i=i: click(i))
    btn.grid(row=(i-1)//3, column=(i-1)%3)
    buttons[i] = btn

init_game()

top.mainloop()


