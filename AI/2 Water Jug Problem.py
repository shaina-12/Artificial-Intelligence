# implementation of two water jug problem
# operations for solving water jug problem are:
# 1. Empty the first jug completely
# 2. Empty the second jug completely
# 3. Fill the first jug
# 4. Fill the second jug
# 5. Fill the water from the second jug into the first jug until the first jug is full 
# or the second jug has no water left
# 6. Fill the water from the first jug into the second jug until the second jug is full 
# or the first jug has no water left
from collections import defaultdict
# Recursive function which prints the intermediate steps to reach the final solution 
# and return boolean value (True if solution is possible, otherwise False). 
# j1 and j2 are the amount of water present in both jugs at a certain point of time.
# mj1 and mj2 are the maximum capacity of jug 1 and jug 2 resp.
# fcj is the final capacity to be obtained in either of two jugs. 
# vis is the boolean dictionary to track the solution. 
def pourJug(j1,j2,mj1,mj2,fcj,vis):
    # check for our goal and returns true if it is achieved 
    if((j1==fcj and j2== 0) or (j1==0 and j2==fcj)):
        print(str(j1)+'\t'+str(j2))
        return True
    # checks if we have already visited the combination or not. If not, then it proceeds further.
    if(vis[(j1,j2)] == False):
        print(str(j1)+'\t'+str(j2))
        # changes the boolean value of the combination as it is visited. 
        vis[(j1,j2)] = True
        # check for all the 6 possibilities and see if a solution is found in any one of them.
        return (pourJug(0, j2, mj1, mj2, fcj, vis) # condition 1
            or pourJug(j1, 0, mj1, mj2, fcj, vis) # condition 2
            or pourJug(mj1, j2, mj1, mj2, fcj, vis) # condition 3
            or pourJug(j1, mj2, mj1, mj2, fcj, vis) # condition 4
            or pourJug(j1 + min(j2,(mj1-j1)), j2 - min(j2,(mj1-j1)), mj1, mj2, fcj, vis) # condition 5
            or pourJug(j1 - min(j1,(mj2-j2)), j2 + min(j1,(mj2-j2)), mj1, mj2, fcj, vis)) # condition 6
    # Return False if the combination is already visited to avoid repetition otherwise 
    # recursion will enter an infinite loop.
    else:
        return False
    
def main():
    # getting the maximum capacity of jug 1 and jug 2
    maxJug1 = int(input('Enter the maximum capacity of jug 1: '))
    maxJug2 = int(input('Enter the maximum capacity of jug 1: '))
    # assigning initial capacity of jug 1 and jug 2
    jug1 = 0
    jug2 = 0
    # getting the final capacity to be obtained in either of two jugs 
    finalCap= int(input('Enter the final capacity of the jug: '))
    # initializing the dictionary with default value as False
    visited = defaultdict(lambda: False)
    print('Jug1\tJug2')
    # method for solving water jug problem
    pourJug(jug1,jug2,maxJug1,maxJug2,finalCap,visited)

if __name__=="__main__":
    main()
