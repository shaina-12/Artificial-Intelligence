# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 14:17:42 2022

@author: hp
"""

import numpy as np
from PIL import Image
player, opponent = 'x', 'o'

# player - computer
# opponent - player

board = np.array([['_','_','_'],
                ['_','_','_'],
                ['_','_','_']])

# This function returns true if there are moves remaining on the board. It returns false if there are no moves left to play.
def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if(board[i][j] == '_') :
                return True
    return False

# This is the evaluation function 
def evaluate(b) :
    # Checking for Rows for X or O victory.
    for row in range(3) :    
        if(b[row][0] == b[row][1] and b[row][1] == b[row][2]):       
            if(b[row][0] == player):
                return 10
            elif(b[row][0] == opponent):
                return -10
    # Checking for Columns for X or O victory.
    for col in range(3) :
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
            if (b[0][col] == player) :
                return 10
            elif(b[0][col] == opponent) :
                return -10
    # Checking for Diagonals for X or O victory.
    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
        if (b[0][0] == player) :
            return 10
        elif(b[0][0] == opponent) :
            return -10
    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
        if (b[0][2] == player) :
            return 10
        elif(b[0][2] == opponent) :
            return -10
    # Else if none of them have won then return 0
    return 0

# This is the minimax function. It considers all the possible ways the game can go and returns the value of the board
def minimax(board,depth,isMax):
    score = evaluate(board)
    # If Maximizer has won the game return his/her evaluated score
    if(score==10):
        return score
    # If Minimizer has won the game return his/her evaluated score
    if(score==-10):
        return score
    # If there are no more moves and no winner then it is a tie
    if(isMovesLeft(board)==False):
        return 0
    # If this maximizer's move
    if(isMax):
        best = -1000
        # Traverse all the cells
        for i in range(3):
            for j in range(3):
                # check if cell is empty
                if(board[i][j]=="_"):
                    # Make the move
                    board[i][j] = player
                    # Call minimax recursively and choose the maximum value
                    best = max(best,minimax(board,depth+1,not isMax))
                    # Undo the move
                    board[i][j] = "_"
        return best
    # If this minimizer's move
    else:
        best = 1000
        # Traverse all the cells
        for i in range(3):
            for j in range(3):
                # check if cell is empty
                if(board[i][j]=="_"):
                    # make the move
                    board[i][j] = opponent
                    # Call minimax recursively and choose the maximum value
                    best = min(best,minimax(board,depth+1,not isMax))
                    # Undo the move
                    board[i][j] = "_"
        return best
        
# This will return the best possible move for the player
def findBestMove(board):
    bestVal = -1000
    bestMove = (-1,-1)
    # Traverse all cells, evaluate minimax function for all empty cells. And return the cell with optimal value.
    for i in range(3):
        for j in range(3):
            # check if the cell is empty
            if(board[i][j]=='_'):
                # make the move
                board[i][j] = player
                # compute evaluation function for this move.
                moreVal = minimax(board,0,False)
                # undo the move
                board[i][j] = "_"
                if(moreVal>bestVal):
                    bestMove = (i,j)
                    bestVal = moreVal
    print("The value of the best Move is :", bestVal)
    print()
    return bestMove

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
        row = int(input('Enter the row number (1 - row 1, 2 - row 2 and 3 - row 3): '))
        col = int(input('Enter the col number (1 - col 1, 2 - col 2 and 3 - col 3): '))
        if(((row>0 and row<4) and (col>0 and col<4)) and board[row-1][col-1]=='_'):
            break
        else:
            print('Invalid Index! Please enter the correct index.')
    board[row-1][col-1] = symbol

"""
# Driver code
board = [
    [ 'x', 'o', 'x' ],
    [ 'o', 'o', 'x' ],
    [ '_', '_', '_' ]
]
bestMove = findBestMove(board)
print("The Optimal Move is :")
print("ROW:", bestMove[0], " COL:", bestMove[1])
"""

def solve(choice,name):
    for turn in range(9):
        if(turn%2==0):
            if(choice=="n"):
                print('Computer '+'\'s Turn (X)')
                bestMove = findBestMove(board)
                row = bestMove[0]
                col = bestMove[1]
                board[row][col] = player
                if(won(player)):
                    print('Computer Wins')
                    break
            else:
                print(name+'\'s Turn (O)')
                place(opponent)
                if(won(opponent)):
                    print(name+' Wins')
                    break
        else:
            if(choice=="n"):
                print(name+'\'s Turn (O)')
                place(opponent)
                if(won(opponent)):
                    print(name+' Wins')
                    break
            else:
                print('Computer '+'\'s Turn (X)')
                bestMove = findBestMove(board)
                row = bestMove[0]
                col = bestMove[1]
                board[row][col] = player
                if(won(player)):
                    print('Computer Wins')
                    break
    if((not won(player)) and (not won(opponent))):
        print('Draw')

def play():
    print('                                                    Tic Tac Toe Game                                                    ')
    print('Welcome To The Game!')
    name = input("Enter your name: ")
    choice = input("Do you want to play first ? (y/n)")
    im = Image.open('Tic Tac Toe.png')
    im.show()
    solve(choice,name)

if __name__=="__main__":
    play()