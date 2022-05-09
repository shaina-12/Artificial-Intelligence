# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 23:08:39 2022

@author: Shaina Mehta
"""

# assumption  - we are taking the undirected graph
def addEdge(adj,v,w):
    # here we are creating adjuscency list
    adj[v].append(w)
    adj[w].append(v)
    return adj
# assign colors (starting from 0) to all
# vertices and prints the assignments of colors
def graphColoring(adj,V):
    result = [-1]*V
    # assign the first color to first vertex
    result[0]=0
    # a temporary array to store the above colors.
    # true value of available colors mean that the
    # color cr is assigned to one of its adjacent vertices
    available = [False]*V
    # assign colors to remaining V-1 vertices
    for u in range(1,V):
        # process all adjacency vertices and 
        # flag their colors as unavailable
        for i in adj[u]:
            if(result[i]!=-1):
                available[result[i]] = True
        # find the first available color
        cr = 0
        while(cr<V):
            if(available[cr]==False):
                break
            cr+=1
        # assign the found color
        result[u] = cr
        # reset the values back to false
        # for the next iteration
        for i in adj[u]:
            if(result[i]!=-1):
                available[result[i]]=False
    # print the result
    for u in range(V):
        print("Vertex",u,"---> Color",result[u])
            
if __name__ == "__main__":
    g1 = [[] for i in range(5)]
    g1 = addEdge(g1, 0, 1)
    g1 = addEdge(g1, 0, 2)
    g1 = addEdge(g1, 1, 2)
    g1 = addEdge(g1, 1, 3)
    g1 = addEdge(g1, 2, 3)
    g1 = addEdge(g1, 3, 4)
    print("Coloring of graph: ")
    graphColoring(g1, 5)
    