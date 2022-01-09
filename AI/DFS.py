from collections import defaultdict
class Graph:
    def __init__(self,n):
        self.n = n
        self.graph = defaultdict(list)
        self.visited = [False for i in range(n)]
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def DFS(self,s):
        self.visited[s] = True
        print(s,end=' ')
        for i in self.graph[s]:
            if(self.visited[i] == False):
                self.DFS(i)

n = 4
g = Graph(n)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.DFS(2)