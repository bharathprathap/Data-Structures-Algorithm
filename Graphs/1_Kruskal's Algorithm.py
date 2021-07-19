class Node:
    def __init__(self,src,dest,weight):
        self.src=src
        self.dest=dest
        self.weight = weight

class Graph:
    
    def __init__(self,vertices):
        
        self.vertices = vertices
        self.adj_Mat = list()
        self.edges = 0

    #function to find if the values belong to the same set
    def find(self,parent,vertex):
        if parent[vertex] == -1:      
            return vertex
        return self.find(parent,parent[vertex])

    #funtion to do union operation of two sets
    def union(self,parent,rank,src,dest):
        
        src_parent = self.find(parent,src)
        dest_parent = self.find(parent,dest)
        
        if rank[src_parent] < rank[dest_parent]:
            parent[src_parent] = dest_parent
            
        if rank[src_parent] > rank[dest_parent]:
            parent[dest_parent] = src_parent
            
        else:
            parent[src_parent] = dest_parent
            rank[dest_parent] += 1

    #function to add an edge to the graph
    def add_edge(self,v1,v2,weight):
        
        self.adj_Mat.append(Node(v1,v2,weight))
        self.edges += 1

    #function to sort the graph based on their weight
    def sort(self):
        
        for i in range(self.edges):
            for j in range(i+1,self.edges):
                if(self.adj_Mat[i].weight > self.adj_Mat[j].weight):
                    self.adj_Mat[i],self.adj_Mat[j] = self.adj_Mat[j],self.adj_Mat[i]

    #function to find the MST using kruscal's algorithm
    def kruskals(self):
        
        temp = list()
        parent = [-1 for i in range(self.vertices)]
        rank = [0 for i in range(self.vertices)]
        
        i,j = 0,0
        self.sort()
        
        while(i < (self.vertices-1) and j < self.edges):
            
            src_parent = self.find(parent,self.adj_Mat[j].src)       
            dest_parent = self.find(parent,self.adj_Mat[j].dest)      
            if src_parent == dest_parent:
                j += 1
                continue
            self.union(parent,rank,src_parent,dest_parent)
            temp.append(self.adj_Mat[j])
            i += 1
            j += 1
            
        return temp


graph = Graph(6)
graph.add_edge(0,1,6)
graph.add_edge(0,2,3)
graph.add_edge(0,4,7)
graph.add_edge(1,2,4)
graph.add_edge(1,3,2)
graph.add_edge(1,5,5)
graph.add_edge(2,3,3)
graph.add_edge(2,4,8)
graph.add_edge(3,5,2)
ans = graph.kruskals()

alph="ABCDST" 
totalweight=0

for i in range(len(ans)):
    totalweight+=ans[i].weight
    print(alph[ans[i].src],"->",alph[ans[i].dest],",weight:",ans[i].weight)
print("Minimum Cost Spanning Tree:",totalweight)