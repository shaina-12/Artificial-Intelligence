# implementation of Maze Problem
# function to print the solution matrix of the maze
def printSol(solMaze):
    for i in range(8):
        for j in range(8):
            print(str(solMaze[i][j]),end=" ")
        print(end="\n")
# A utility function to check if x, y is valid
# index for N * N Maze
def isSafe(maze,x,y):
    if((x>=0 and x<8) and (y>=0 and y<8) and (maze[x][y]==1)):
        return True
    return False
# function for solving maze problem
def solve(maze,x,y,solMaze):
    # check if one reaches the goal state
    if(x==7 and y==7 and maze[x][y]==1):
        solMaze[x][y] = 1;
        return True
    # Check if maze[x][y] is valid
    if(isSafe(maze,x,y) == True):
        # Check if the current block is already part of solution path.
        if(solMaze[x][y]==1):
            return False
        # mark x, y as part of solution path
        solMaze[x][y] = 1
        # moving forward
        if(solve(maze,x+1,y,solMaze) == True):
            return True
        # moving down
        if(solve(maze,x,y+1,solMaze) == True):
            return True
        # moving backward
        if(solve(maze,x-1,y,solMaze) == True):
            return True
        # moving upward
        if(solve(maze,x,y-1,solMaze) == True):
            return True
        # moving left diagonal down
        if(solve(maze,x+1,y+1,solMaze) == True):
            return True
        # moving left diagonal up
        if(solve(maze,x-1,y-1,solMaze) == True):
            return True
        # moving right diagonal up
        if(solve(maze,x-1,y+1,solMaze) == True):
            return True
        # moving right diagonal down
        if(solve(maze,x+1,y-1,solMaze) == True):
            return True
        # If none of the above movements work then
        # BACKTRACK: unmark x, y as part of solution path
        solMaze[x][y] = 0
        return False

# This function solves the Maze problem using Backtracking.
def solveMaze(maze):
    # creation of solution matrix
    solMaze = [[0 for i in range(8)] for j in range(8)]
    if(solve(maze,0,0,solMaze)==False):
        print('Solution does not exist.')
    else:
         printSol(solMaze)

if __name__ == '__main__':
    maze = [[1,0,0,1,0,0,1,1],
            [1,1,1,0,0,1,1,1],
            [0,0,0,1,1,1,0,1],
            [0,0,1,1,0,0,0,1],
            [1,1,0,1,1,0,1,0],
            [1,1,0,0,1,1,0,0],
            [0,0,0,0,0,1,1,0],
            [0,0,0,0,0,0,1,1]]
    solveMaze(maze)
