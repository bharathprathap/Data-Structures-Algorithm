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
    
    #bool function check if there enodeists a left child branch
    def hasLeft(self):
        
        if(self.left):
            return 1
        else:
            return 0
        
    #bool function check if there enodeists a right child branch
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
            
#function to search for an element
def search(node,val):
    
    if node.data == val:
        return True
    
    if(node.hasLeft()):
        
        lft=search(node.left,val)
        if(lft==True):
            return True
          
    if(node.hasRight()):
        ryt=search(node.right,val)
        if(ryt==True):
            return True
        else:
            return False
        
#function to calculate the depth of a tree from rootnode to a given node
def findDepth(root, node):
   
    if (root == None):
        return -1
    
    depth = -1
 
    if (root.data == node):
        return depth + 1
 
    depth = findDepth(root.left, node)
    if depth >= 0:
        return depth + 1
    depth = findDepth(root.right, node)
    if depth >= 0:
        return depth + 1
    return depth


class NotFound(Exception):
    pass



#building a tree
root = Node('+')
root.left=Node("-")
root.right=Node("-")

root.left.left=Node("+")
root.left.right=Node(6)
root.left.left.left=Node(3)
root.left.left.right=Node("*")
root.left.left.right.left=Node(2)
root.left.left.right.right=Node(1)

root.right.left=Node(5)
root.right.right=Node(4)

x=int(input("enter value of node to search:"))
if(search(root,x)):
    print("Node with the value ",x,"exists with depth=",findDepth(root,x))
else:
    try:
        if(search(root,x)==False):
            raise NotFound
    except NotFound:
        print("Error:Node with value ",x," not found")
