import math as m
from copy import deepcopy

class Node:
    def __init__(self,n,h,l):
        self.node = n
        self.hv = h
        #self.parent = None
        #self.child = None
        self.level = l

open = []
closed = []

def find(state,ele):
    for i in range(3):
        for j in range(3):
            if(ele == state[i][j]):
                return (i,j)
    return (-1,-1)

# here we are using manhatten distance for calculation of heuristic function
def calHeuristic(curr,goal):
    dist = 0
    for i in range(3):
        for j in range(3):
            if(curr[i][j]!=-1):
                i1, j1 = find(goal,curr[i][j])
                dist = dist + m.fabs(i-i1) + m.fabs(j-j1)
    return dist

def swap(node,r1,c1,r2,c2):
    tmp = node[r1][c1]
    node[r1][c1] = node[r2][c2]
    node[r2][c2] = tmp

def cmp(curr,goal):
    for i in range(3):
        for j in range(3):
            if(curr[i][j] != goal[i][j]):
                return False
    return True

def movesGenerator(curr,goal):
    row = 0
    col = 0
    for i in range(3):
        for j in range(3):
            if(curr.node[i][j]==-1):
                row = i
                col = j
                break
    lev = curr.level + 1
    if(row == 0):
        if(col == 0):
            tmp1 = deepcopy(curr.node)
            swap(tmp1,0,0,0,1)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr.node)
            swap(tmp2,0,0,1,0)
            hv2 = calHeuristic(tmp2,goal)
            node1 = Node(tmp1,hv1+lev,lev)
            node2 = Node(tmp2,hv2+lev,lev)
            return (node1,node2)
        if(col == 1):
            tmp1 = deepcopy(curr.node)
            swap(tmp1,0,1,0,0)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr.node)
            swap(tmp2,0,1,1,1)
            hv2 = calHeuristic(tmp2,goal)
            tmp3 = deepcopy(curr.node)
            swap(tmp3,0,1,0,2)
            hv3 = calHeuristic(tmp3,goal)
            node1 = Node(tmp1,hv1+lev,lev)
            node2 = Node(tmp2,hv2+lev,lev)
            node3 = Node(tmp3,hv3+lev,lev)
            return (node1,node2,node3)
        if(col == 2):
            tmp1 = deepcopy(curr.node)
            swap(tmp1,0,2,0,1)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr.node)
            swap(tmp2,0,2,1,2)
            hv2 = calHeuristic(tmp2,goal)
            node1 = Node(tmp1,hv1+lev,lev)
            node2 = Node(tmp2,hv2+lev,lev)
            return (node1,node2)
    if(row == 1):
        if(col == 0):
            tmp1 = deepcopy(curr.node)
            swap(tmp1,1,0,0,0)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr.node)
            swap(tmp2,1,0,1,1)
            hv2 = calHeuristic(tmp2,goal)
            tmp3 = deepcopy(curr.node)
            swap(tmp3,1,0,2,0)
            hv3 = calHeuristic(tmp3,goal)
            node1 = Node(tmp1,hv1+lev,lev)
            node2 = Node(tmp2,hv2+lev,lev)
            node3 = Node(tmp3,hv3+lev,lev)
            return (node1,node2,node3)
        if(col == 1):
            tmp1 = deepcopy(curr.node)
            swap(tmp1,1,1,1,0)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr.node)
            swap(tmp2,1,1,0,1)
            hv2 = calHeuristic(tmp2,goal)
            tmp3 = deepcopy(curr.node)
            swap(tmp3,1,1,1,2)
            hv3 = calHeuristic(tmp3,goal)
            tmp4 = deepcopy(curr.node)
            swap(tmp4,1,1,2,1)
            hv4 = calHeuristic(tmp4,goal)
            node1 = Node(tmp1,hv1+lev,lev)
            node2 = Node(tmp2,hv2+lev,lev)
            node3 = Node(tmp3,hv3+lev,lev)
            node4 = Node(tmp4,hv4+lev,lev)
            return (node1,node2,node3,node4)
        if(col == 2):
            tmp1 = deepcopy(curr.node)
            swap(tmp1,1,2,0,2)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr.node)
            swap(tmp2,1,2,1,1)
            hv2 = calHeuristic(tmp2,goal)
            tmp3 = deepcopy(curr.node)
            swap(tmp3,1,2,2,2)
            hv3 = calHeuristic(tmp3,goal)
            node1 = Node(tmp1,hv1+lev,lev)
            node2 = Node(tmp2,hv2+lev,lev)
            node3 = Node(tmp3,hv3+lev,lev)
            return (node1,node2,node3)
    if(row == 2):
        if(col == 0):
            tmp1 = deepcopy(curr.node)
            swap(tmp1,2,0,1,0)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr.node)
            swap(tmp2,2,0,2,1)
            hv2 = calHeuristic(tmp2,goal)
            node1 = Node(tmp1,hv1+lev,lev)
            node2 = Node(tmp2,hv2+lev,lev)
            return (node1,node2)
        if(col == 1):
            tmp1 = deepcopy(curr.node)
            swap(tmp1,2,1,2,0)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr.node)
            swap(tmp2,2,1,1,1)
            hv2 = calHeuristic(tmp2,goal)
            tmp3 = deepcopy(curr.node)
            swap(tmp3,2,1,2,2)
            hv3 = calHeuristic(tmp3,goal)
            node1 = Node(tmp1,hv1+lev,lev)
            node2 = Node(tmp2,hv2+lev,lev)
            node3 = Node(tmp3,hv3+lev,lev)
            return (node1,node2,node3)
        if(col == 2):
            tmp1 = deepcopy(curr.node)
            swap(tmp1,2,2,1,2)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr.node)
            swap(tmp2,2,2,2,1)
            hv2 = calHeuristic(tmp2,goal)
            node1 = Node(tmp1,hv1+lev,lev)
            node2 = Node(tmp2,hv2+lev,lev)
            return (node1,node2)

def finding(arr,li):
    for i in range(len(li)):
        if(cmp(arr,li[i].node)==True):
            return True
    return False

def printing(curr):
    for i in range(3):
        for j in range(3):
            print(curr[i][j],end=" ")
        print()

def solve(initial,goal):
    j=0
    heurist = calHeuristic(initial,goal)
    start = Node(initial,heurist,0)
    open.append(start)
    while(len(open) != 0):
        open.sort(key=lambda n1: n1.hv)
        curr = deepcopy(open.pop(0))
        print("--------------------")
        print('Step',j+1)
        printing(curr.node)
        closed.append(curr)
        if(cmp(curr.node,goal)):
            print("--------------------")
            print("Goal State Reached!!!")
            print("====================")
            print('Goal State: ')
            printing(goal)
            print('Puzzle is Solved!!!')
            print("====================")
            break
        nodes = movesGenerator(curr,goal)
        j=j+1
        for i in range(len(nodes)):
            if(finding(nodes[i].node,open)==False and finding(nodes[i].node,closed)==False):
                open.append(nodes[i])
        if(j>50):
            print("--------------------")
            print('Max Depth Reached!!!!')
            print("====================")
            print('Puzzle Cannot Be Solved Within The Time!!!')
            print("====================")
            break

# Working in Hill Climbing
initial = [[1, -1, 3], 
            [4, 2, 5], 
            [7, 8, 6]]
goal = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, -1]]
print("====================")
print('Initial State: ')
printing(initial)
print('Start To Solving Puzzle!!!')
print("====================")
print('Steps Followed: ')
solve(initial,goal)
# Not Working in Hill Climbing but Working in A* Algo
"""
initial = [[1,2,3],
            [-1,6,4],
            [7,8,5]]
goal =  [[1,2,3],
            [4,5,6],
            [7,8,-1]]
"""
# Special Case
"""
initial = [[1,2,4],
            [5,-1,7],
            [3,6,8]]
goal = [[1,4,7],
        [2,5,8],
        [3,6,-1]]
"""
