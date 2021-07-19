class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
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
        
    


root = Node("+")
root.left=Node("-")
root.right=Node("-")

root.left.left=Node("+")
root.left.right=Node("w")
root.left.left.left=Node("x")
root.left.left.right=Node("*")
root.left.left.right.left=Node("y")
root.left.left.right.right=Node("z")

root.right.left=Node("u")
root.right.right=Node("v")

inOrder_traverse(root)
print("\n")