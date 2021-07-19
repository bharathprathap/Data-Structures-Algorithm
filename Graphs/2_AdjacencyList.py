class Node:
    def __init__(self,data):
        self.vertex=data
        self.next=None

class Graph:
        
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices
        
    #function to add an edge to the graph
    def add_edge(self,value1,value2):
        
        node=Node(value2)
        node.next=self.graph[value1]
        self.graph[value1]=node
        
        node=Node(value1)
        node.next=self.graph[value2]
        self.graph[value2]=node
    
    #function to print the graph
    def print_list(self):
        for i in range(0,self.vertices):
            temp=self.graph[i]
            while temp:
                print("-->",temp.vertex,end="")
                temp=temp.next
            print("\n")
        
graph=Graph(7)
graph.add_edge(0,1)
graph.add_edge(0,3)
graph.add_edge(1,2)
graph.add_edge(1,3)
graph.add_edge(1,5)
graph.add_edge(2,5)
graph.add_edge(2,3)
graph.add_edge(2,4)
graph.add_edge(3,4)
graph.add_edge(4,6)
graph.add_edge(1,6)

print("The adjacency list of the graph is:\n")
graph.print_list()
       