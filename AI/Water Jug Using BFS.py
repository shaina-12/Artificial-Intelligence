# implementation of water jug problem using BFS
from collections import deque
# function to solve water jug problem using BFS Approach
def waterJug(cap1,cap2,target):
    # Map is used to store the states, every state is hashed to binary value to indicate either 
    # that state is visited before or not
    visited = {}
    isSolvable = False
    path = []
    # queue to maintain states
    q = deque()
    # initializating with initial state
    q.append((0,0))
    while(len(q)>0):
        # current state
        state = q.popleft()
        #print(state)
        # If this state is already visited
        if(state in visited):
            continue
        # Doesn't met jug constraints
        if(state[0]>cap1 or state[1]>cap2 or state[0]<0 or state[1]<0):
            continue
        # Filling the vector for constructing the solution path
        path.append((state[0],state[1]))
        # Marking current state as visited
        visited[state] = True
        # If we reach the goal state
        if(state[0]==target[0] and state[1]==target[1]):
            isSolvable = True
            #path.append(state)
            print('Jug1\tJug2')
            for i in range(len(path)):
                print(str(path[i][0])+'\t'+str(path[i][1]))
            break
        #print(state)
        # fill the first jug
        if(state[0]<cap1):
            #path.append((cap1,state[1]))
            q.append((cap1,state[1]))
        # fill the second jug
        if(state[1]<cap2):
            #path.append((state[0],cap2))
            q.append((state[0],cap2))
        # empty the first jug
        if(state[0]>0):
            #path.append((0,state[1]))
            q.append((0,state[1]))
        # empty the second jug
        if(state[1]>0):
            #path.append((state[0],0))
            q.append((state[0],0))
        # Pour from 1st jug to 2nd until its full
        if(state[0]>0 and state[0]+state[1]>=cap2):
            #path.append((state[0]-(cap2-state[1]),cap2))
            q.append((state[0]-(cap2-state[1]),cap2))
        # Pour from 2nd jug to 1st until its full
        if(state[1]>0 and state[0]+state[1]>=cap1):
            #path.append((cap1,state[1]-(cap1-state[0])))
            q.append((cap1,state[1]-(cap1-state[0])))
        # Pour all water from 1st to 2nd
        if(state[0]>0 and state[0]+state[1]<=cap2):
            #path.append((0,state[0]+state[1]))
            q.append((0,state[0]+state[1]))
        # Pour all water from 2nd to 1st
        if(state[1]>0 and state[0]+state[1]<=cap1):
            #path.append((state[0]+state[1],0))
            q.append((state[0]+state[1],0))
    # No, solution exists 
    if (not isSolvable):
        print ("No solution")
        #print(path)
    #print(path)
if __name__ == '__main__':
    cap1, cap2 = tuple(map(int,input('Enter the capacity of jug 1 and jug 2: ').split()))
    target = tuple(map(int,input('Enter the final capacity of jug1 and jug 2: ').split()))
    waterJug(cap1,cap2,target)