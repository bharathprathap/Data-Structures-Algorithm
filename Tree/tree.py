class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    #function to insert a node to the tree
    def insert(self, data):
        
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    #function to return the left child branch of a node
    def left(self): 
        
        return self.left
    
    #function to return the right child branch of a node
    def right(self): 
        
        return self.right
    
    #bool function check if there exists a left child branch
    def hasLeft(self):
        
        if(self.left):
            return 1
        else:
            return 0
        
    #bool function check if there exists a right child branch
    def hasRight(self):
        
        if(self.right):
            return 1
        else:
            return 0
    
    #function to print the tree
    def PrintTree(self):
        
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
            
#function to perform inOrder_traverse
def inOrder_traverse(node):
    
    if(node.hasLeft()):
        print("(",end="")
        inOrder_traverse(node.left)
    print(node.data,end="")    
    if(node.hasRight()):
        inOrder_traverse(node.right)
        print(")", end="")
#function to print an arithmetic expression      
def printExpression(node):
    
    if(node.hasLeft()):
        print("(")
        inOrder_traverse(node.left)
    
    print(node.data)
    
    if (node.hasRight()):
        inOrder(node.right())
        print(")")