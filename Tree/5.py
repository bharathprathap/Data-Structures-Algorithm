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
 
#function to print the tree in a preorder traversal           
def printPreorder(root): 
    
    if root:
        print(root.data,end=" ")
    
        printPreorder(root.left)

        printPreorder(root.right)

    


root = Node(15)
root.left=Node(12)
root.right=Node(13)

root.left.left=Node(5)
root.left.right=Node(6)
root.left.left.left=Node(4)
root.left.left.right=Node(3)
root.left.left.right.left=Node(1)
root.left.left.right.right=Node(2)

root.right.left=Node(7)
root.right.right=Node(8)

print("Tree in preorder traversal:")

printPreorder(root)
print("\n")