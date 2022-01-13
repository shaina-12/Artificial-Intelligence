import numpy as np
from PIL import Image;
board = np.array([['_','_','_'],
                ['_','_','_'],
                ['_','_','_']])
def checkRow(symbol):
    for i in range(3):
        if(board[i][0] == board[i][1] == board[i][2] == symbol):
            return True 
    return False
def checkCol(symbol):
    for i in range(3):
        if(board[0][i] == board[1][i] == board[2][i] == symbol):
            return True 
    return False
def checkDiagonal(symbol):
    if(board[0][0] == board[1][1] == board[2][2] == symbol):
        return True
    elif(board[0][2] == board[1][1] == board[2][0] == symbol):
        return True
    else:
        return False
def won(symbol):
    return (checkRow(symbol) or checkCol(symbol) or checkDiagonal(symbol))
def place(symbol):
    print(np.matrix(board))
    while(1):
        row = int(input('Enter the row number (1 - row 1, 2 - row 2 and 3 - row 3: '))
        col = int(input('Enter the col number (1 - col 1, 2 - col 2 and 3 - col 3: '))
        if(((row>0 and row<4) and (col>0 and col<4)) and board[row-1][col-1]=='_'):
            break
        else:
            print('Invalid Index! Please enter the correct index.')
    board[row-1][col-1] = symbol
def play():
    print('                                                    Tic Tac Toe Game                                                    ')
    print('Welcome To The Game!')
    p1name = input('Player 1: Enter the name (Symbol X): ')
    p2name = input('Player 2: Enter the name (Symbol O): ')
    print()
    p1s='X'
    p2s='O'
    im = Image.open('Tic Tac Toe.png')
    im.show()
    for turn in range(9):
        if(turn%2==0):
            print(p1name+'\'s Turn')
            place(p1s)
            if(won(p1s)):
                print(p1name+' Wins')
                break
        else:
            print(p2name+'\'s Turn')
            place(p2s)
            if(won(p2s)):
                print(p2name+' Wins')
                break
    if((not won(p1s)) and (not won(p2s))):
        print('Draw')
    print('Thank you for playing the game. :)')
if __name__=="__main__":
    play()
