class Graph:
    
    def __init__(self,size):
        self.adj_mat=[]
        for i in range(size+1):
            self.adj_mat.append([0 for i in range(size+1)])
        self.size = size
        
    #function to add an edge to the graph
    def add_edge(self,value1,value2):
        self.adj_mat[value1][value2]=1
        self.adj_mat[value2][value1]=1
    
    #function to remove an edge from the graph   
    def remove_edge(self,value1,value2):
        if(self.adj_mat[value1][value2]==0 or self.adj_mat[value2][value1]==0 ):
            print("\nNo edge exist between these values.")
            return 0
        else:
            self.adj_mat[value1][value2]=0
            self.adj_mat[value2][value1]=0
            
    #function to print the adjacency matrix
    def print_matrix(self):
        for i in range(0,self.size+1):
            for j in range(0,self.size+1):
                print(self.adj_mat[i][j],end=" ")
            print("\n")
 
           
graph =Graph(6)
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

print("The adjacency matrix of the graph is:\n")
graph.print_matrix()
            
        