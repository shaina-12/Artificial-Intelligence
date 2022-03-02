import heapq as pq
import math # to initialize minimum to infinity
from collections import defaultdict # dictionary of sets

# class that implements priority queue
class PriorityQueue:
    def __init__(self):
        self.__queue = []
        self.__index = 0
    def insert(self,item,priority):
        pq.heappush(self.__queue,(priority,self.__index,item))
        self.__index += 1
    def remove(self):
        return pq.heappop(self.__queue)[-1]
        #self.__index -= 1
    def isEmpty(self):
        return len(self.__queue) == 0
    def getSize(self):
        return self.__index

class Graph:
    def __init__(self,vertices):
        #self.__numV = n
        self.__nodes = vertices[:]
        self.__graph = {node:{} for node in self.__nodes}
        self.__elist = []
    def addEdge(self,u,v,cost):
        for edges in self.__elist:
            if(u==edges[0] and v==edges[1]):
                print("Please Enter The Correct Edge!!!")
                return
        self.__graph[u].update({v:cost})
        self.__elist.append([u,v,cost])
    def primsMST(self,source):
        priority_queue = { source : 0 }
        added = [False] * len(self.__elist)
        min_span_tree_cost = 0
        while priority_queue :
            # Choose the adjacent node with the least edge cost
            node = min(priority_queue, key=priority_queue.get)
            cost = priority_queue[node]
            # Remove the element from a dictionary in python
            del priority_queue[node]
            if(node < len(added) and added[node] == False):
                min_span_tree_cost += cost
                added[node] = True
                for item in list(self.__graph[node].items()):
                    adjnode = item[0]
                    adjcost = item[1]
                    if(adjnode < len(added) and added[adjnode] == False):
                        priority_queue[adjnode] = adjcost
        return min_span_tree_cost
    # function to get the cost of optimal path found
    def get_cost(self,visited_nodes):
        if len(visited_nodes)<=1:
            return 0
        else:
            total_cost=0
            i=1
            while i<len(visited_nodes):
                for temp_edge in self.__elist:
                    if visited_nodes[i-1]==temp_edge[0] and visited_nodes[i]==temp_edge[1]:
                        total_cost=total_cost+temp_edge[2]
                i=i+1
            for temp_edge in self.__elist:
                    if visited_nodes[0]==temp_edge[0] and visited_nodes[len(visited_nodes) - 1]==temp_edge[1]:
                        total_cost=total_cost+temp_edge[2]
            return total_cost
    def tspUsingAStar(self,initial_node):
        #print(self.__graph)
        if(not self.__elist):
            print('Error: Graph does not contain edges!!!')
        else:
            if(initial_node in self.__nodes):
                print("Initial node:",initial_node)
                # creating a prioirty queue
                queue = PriorityQueue()
                iteration =  1
                # calculates the cost
                # g_cost = cost b/w two nodes
                # h_cost = heuristic function which calculates the cost of MST from that particular node
                # f_cost = total cost
                # here we are calculating the cost of initial node
                g_cost, h_cost = 0, self.primsMST(initial_node)
                f_cost = g_cost + h_cost
                queue.insert((initial_node,g_cost,h_cost),f_cost)
                # visited_nodes keeps the track of order of visited nodes added to the path
                # visited_nodes acts like a closed list
                visited_nodes = []
                visited_nodes.append(initial_node)
                while(len(visited_nodes) < len(self.__nodes)):
                    print("-------------------Iteration no.",iteration,"-------------------")
                    # check if children there is any node remained to expand while goal state is not reached
                    if queue.isEmpty():
                        print("Error : Goal state cannot be reached. Graph is not connected!!!")
                        return 0,[]
                    # a item of the queue is a 3-tuple: (current_node, g_cost, h_cost)
                    current_node, g_cost, h_cost = queue.remove()
                    # remaining_nodes is generated by checking unexpanded neighbous for current_node
                    # functionality of remaining_nodes partially resembles the functionality of fringe_list
                    remaining_nodes = []
                    # gets all the successors of "current_node"
                    successors = list(self.__graph[current_node].items())
                    #print('Shaina',successors)
                    minimum = math.inf
                    a,b,c,d=0,0,0,0
                    temp_successors=[]
                    for successor in successors:
                        if successor[0] not in visited_nodes:
                            temp_successors.append(successor)
                    print("Successor of",current_node,": ",temp_successors)
                    if(len(temp_successors)!=0):
                        for successor in temp_successors:
                            # empty the remaining nodes to remove the nodes from previous iteration
                            remaining_nodes.clear()
                            destination, weight = successor # unpack two tuple successor
                            # add unvisited nodes to remaining_nodes
                            for i in self.__nodes:
                                if(i not in visited_nodes):
                                    remaining_nodes.append(i)
                            print("Remaining nodes:",remaining_nodes)
                            # if remaining node contains a single unvisited node, h_cost = 0 for that single node
                            if(len(remaining_nodes)==1):
                                print('Yes')
                                new_g_cost = g_cost + weight
                                h_cost = 0
                                f_cost = new_g_cost + h_cost
                                print("Node:",destination,"f_cost:",f_cost,"g_cost:",new_g_cost,"h_cost:",h_cost)
                                a,b,c,d=destination,f_cost,new_g_cost,h_cost
                            else:
                                # create a temorary graph using nodes from remaining_nodes 
                                #lengths = len(remaining_nodes)
                                temp_graph = Graph(remaining_nodes)
                                # add edges to temporary graph if remaining_nodes exist in original graph 
                                for temp_edge in self.__elist:
                                    if(temp_edge[0] in remaining_nodes and temp_edge[1] in remaining_nodes):
                                        temp_graph.addEdge(temp_edge[0],temp_edge[1],temp_edge[2]) 
                                # calculates costs for temporary graph
                                new_g_cost = g_cost + weight
                                h_cost = temp_graph.primsMST(destination)
                                f_cost = new_g_cost + h_cost
                                print("Node:",destination,"f_cost:",f_cost,"g_cost:",new_g_cost,"h_cost:",h_cost)
                                # choose the minimum f_cost of all the successors
                                if(f_cost < minimum):
                                    minimum = f_cost
                                    a,b,c,d=destination,f_cost,new_g_cost,h_cost
                        print("CHOSEN NODE : \nParent:",current_node,"Child:",a,"f_cost:",b,"g_cost:",c,"h_cost:",d)
                        destination=a
                        f_cost=b
                        new_g_cost=c
                        h_cost=d
                        # add this minimum node to visited_nodes whuch represents our path
                        visited_nodes.append(destination)
                        # add the minimum successor to queue
                        queue.insert((destination, new_g_cost, h_cost), f_cost)
                        print("Visited nodes till now:",visited_nodes)
                        iteration = iteration + 1
                        # verifies that reached the goal
                        if(len(visited_nodes) == len(self.__nodes)):
                            print("\n===========Goal state reached===========\n")
                if(len(visited_nodes) == len(self.__nodes)):
                    return visited_nodes
            else:
                print('Error: the node(s) not exists in the graph!!')

def printPath(path):
    print("=================Path found=================")
    print("final path:")
    for i in range(len(path)-1):
        print(path[i],"->",path[i+1])
    print(path[len(path)-1],"->",path[0])

g=Graph([0,1,2,3])

g.addEdge(0, 1, 10) 
g.addEdge(1, 0, 10)

g.addEdge(0, 2, 15) 
g.addEdge(2, 0, 15)

g.addEdge(0, 3, 20) 
g.addEdge(3, 0, 20)

g.addEdge(1, 2, 35) 
g.addEdge(2, 1, 35)

g.addEdge(1, 3, 25) 
g.addEdge(3, 1, 25)

g.addEdge(3, 2, 30) 
g.addEdge(2, 3, 30)


path = g.tspUsingAStar(0) # executes the algorithm
total_cost = g.get_cost(path)
if total_cost:
    printPath(path)
    print("total_cost",total_cost)
else:
    print('Did not reach the goal!')