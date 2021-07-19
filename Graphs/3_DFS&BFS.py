class Graph:
        
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for i in range(vertices)] 
        
    #function to add an edge to the graph
    def add_edge(self,value1,value2):
        
        self.graph[value1].append(value2)
    
    
    #function to print the graph in DFS method
    def DFS(self,src):   
                 
        visited = [False for i in range(self.vertices)]
        stack=[]
        stack.append(src)

        while (len(stack)):
            
            src =stack.pop()
            
            if (not visited[src]):
                print(src,end=' ')
                visited[src] = True
                
            for node in self.graph[src]:
                if (not visited[node]):
                    stack.append(node)
                    
    #function to print the graph in BFS method
    def BFS(self,src):   
                 
        visited = [False for i in range(self.vertices)]
        queue=[]
        queue.append(src)

        while (len(queue)):
    
            src=queue.pop(0)
            if (not visited[src]):
                print(src,end=' ')
                visited[src] = True
                
            for node in self.graph[src]:
                if (not visited[node]):
                    queue.append(node)
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

print("Graph in Depth First traversal(DFS):")
graph.DFS(0)

print("\nGraph in Breadth First traversal(BFS):")
graph.BFS(0)
       