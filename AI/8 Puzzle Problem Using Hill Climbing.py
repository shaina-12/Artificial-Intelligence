from copy import deepcopy

class Node:
    def __init__(self,n,h):
        self.node = n
        self.hv = h
        self.child = None

visited = []

def calHeuristic(curr,goal):
    hv = 0
    for i in range(3):
        for j in range(3):
            if(curr[i][j]!=goal[i][j]):
                hv = hv + 1
    return hv-1

def swap(node,r1,c1,r2,c2):
    tmp = node[r1][c1]
    node[r1][c1] = node[r2][c2]
    node[r2][c2] = tmp

def movesGenerator(curr,goal):
    row = 0
    col = 0
    for i in range(3):
        for j in range(3):
            if(curr[i][j]==-1):
                row = i
                col = j
                break
    if(row == 0):
        if(col == 0):
            tmp1 = deepcopy(curr)
            swap(tmp1,0,0,0,1)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr)
            swap(tmp2,0,0,1,0)
            hv2 = calHeuristic(tmp2,goal)
            node1 = Node(tmp1,hv1)
            node2 = Node(tmp2,hv2)
            return (node1,node2)
        if(col == 1):
            tmp1 = deepcopy(curr)
            swap(tmp1,0,1,0,0)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr)
            swap(tmp2,0,1,1,1)
            hv2 = calHeuristic(tmp2,goal)
            tmp3 = deepcopy(curr)
            swap(tmp3,0,1,0,2)
            hv3 = calHeuristic(tmp3,goal)
            node1 = Node(tmp1,hv1)
            node2 = Node(tmp2,hv2)
            node3 = Node(tmp3,hv3)
            return (node1,node2,node3)
        if(col == 2):
            tmp1 = deepcopy(curr)
            swap(tmp1,0,2,0,1)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr)
            swap(tmp2,0,2,1,2)
            hv2 = calHeuristic(tmp2,goal)
            node1 = Node(tmp1,hv1)
            node2 = Node(tmp2,hv2)
            return (node1,node2)
    if(row == 1):
        if(col == 0):
            tmp1 = deepcopy(curr)
            swap(tmp1,1,0,0,0)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr)
            swap(tmp2,1,0,1,1)
            hv2 = calHeuristic(tmp2,goal)
            tmp3 = deepcopy(curr)
            swap(tmp3,1,0,2,0)
            hv3 = calHeuristic(tmp3,goal)
            node1 = Node(tmp1,hv1)
            node2 = Node(tmp2,hv2)
            node3 = Node(tmp3,hv3)
            return (node1,node2,node3)
        if(col == 1):
            tmp1 = deepcopy(curr)
            swap(tmp1,1,1,1,0)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr)
            swap(tmp2,1,1,0,1)
            hv2 = calHeuristic(tmp2,goal)
            tmp3 = deepcopy(curr)
            swap(tmp3,1,1,1,2)
            hv3 = calHeuristic(tmp3,goal)
            tmp4 = deepcopy(curr)
            swap(tmp4,1,1,2,1)
            hv4 = calHeuristic(tmp4,goal)
            node1 = Node(tmp1,hv1)
            node2 = Node(tmp2,hv2)
            node3 = Node(tmp3,hv3)
            node4 = Node(tmp4,hv4)
            return (node1,node2,node3,node4)
        if(col == 2):
            tmp1 = deepcopy(curr)
            swap(tmp1,1,2,0,2)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr)
            swap(tmp2,1,2,1,1)
            hv2 = calHeuristic(tmp2,goal)
            tmp3 = deepcopy(curr)
            swap(tmp3,1,2,2,2)
            hv3 = calHeuristic(tmp3,goal)
            node1 = Node(tmp1,hv1)
            node2 = Node(tmp2,hv2)
            node3 = Node(tmp3,hv3)
            return (node1,node2,node3)
    if(row == 2):
        if(col == 0):
            tmp1 = deepcopy(curr)
            swap(tmp1,2,0,1,0)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr)
            swap(tmp2,2,0,2,1)
            hv2 = calHeuristic(tmp2,goal)
            node1 = Node(tmp1,hv1)
            node2 = Node(tmp2,hv2)
            return (node1,node2)
        if(col == 1):
            tmp1 = deepcopy(curr)
            swap(tmp1,2,1,2,0)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr)
            swap(tmp2,2,1,1,1)
            hv2 = calHeuristic(tmp2,goal)
            tmp3 = deepcopy(curr)
            swap(tmp3,2,1,2,2)
            hv3 = calHeuristic(tmp3,goal)
            node1 = Node(tmp1,hv1)
            node2 = Node(tmp2,hv2)
            node3 = Node(tmp3,hv3)
            return (node1,node2,node3)
        if(col == 2):
            tmp1 = deepcopy(curr)
            swap(tmp1,2,2,1,2)
            hv1 = calHeuristic(tmp1,goal)
            tmp2 = deepcopy(curr)
            swap(tmp2,2,2,2,1)
            hv2 = calHeuristic(tmp2,goal)
            node1 = Node(tmp1,hv1)
            node2 = Node(tmp2,hv2)
            return (node1,node2)

def cmp(curr,goal):
    for i in range(3):
        for j in range(3):
            if(curr[i][j] != goal[i][j]):
                return False
    return True

def findAnswer(parent,curr,goal):
    if(curr.node in visited):
        print("====================")
        print('No Goal Stata Reached!!!')
        print('Local Maxima Is: ')
        printing(parent.node)
        return
    if(cmp(curr.node,goal)):
        print("====================")
        print('Goal State Reached!!!')
        print('Goal State: ')
        printing(curr.node)
        return
    #print('test',curr.node)
    visited.append(curr.node)
    curr.child = movesGenerator(curr.node,goal)
    mini = 999999
    ind = -1
    #for i in range(len(curr.child)):
    #    print('hi',curr.child[i].hv)
    for i in range(len(curr.child)):
        if(curr.child[i].hv < mini and curr.child[i].node not in visited):
            mini = curr.child[i].hv
            ind = i
    ctr = 0
    for i in range(len(curr.child)):
        if(curr.child[i].hv==mini):
            ctr = ctr + 1                          
    if(ctr > 1):
        print("====================")
        print('No Goal State Reached!!!')
        print('Local Maxima Is: ')
        print(curr.node)
        return
    findAnswer(curr,curr.child[ind],goal)
    return 

def printing(curr):
    for i in range(3):
        for j in range(3):
            print(curr[i][j],end=" ")
        print()

def solve(initial,goal):
    heurist = calHeuristic(initial,goal)
    parent = None
    start = Node(initial,heurist)
    findAnswer(parent,start,goal)
    #ans = findAnswer(start,goal)
    #print(ans.node)

def main():
# Working
    initial = [
        [1, -1, 3],
        [4, 2, 5],
        [7, 8, 6]
    ]
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, -1]
    ]
    print("====================")
    print('Initial State: ')
    printing(initial)
    print("====================")
    solve(initial,goal)
    print("====================")
# Not Working
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
main()
