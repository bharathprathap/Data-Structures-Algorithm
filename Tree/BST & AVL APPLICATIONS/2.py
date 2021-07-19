class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBinaryTree(root):
    
    if root is None:
        return True
    if(isSubtreeLesser(root.left,root.data) and isSubtreeGreater(root.right,root.data) 
       and isBinaryTree(root.left) and isBinaryTree(root.right)):
        return True
    else:
        return False
        
def isSubtreeGreater(root,val):
    
    if root is None:
        return True
    if( root.data > val and isSubtreeGreater(root.left,val) and isSubtreeGreater(root.right,val)):
        return True
    else:
        return False
    
def isSubtreeLesser(root,val):
    
    if root is None:
        return True
    if( root.data <= val and isSubtreeLesser(root.left,val) and isSubtreeLesser(root.right,val)):
        return True
    else:
        return False
     
#Example 1
root =Node(3)
root.left = Node(2)
root.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(4)
 
print("Example1:")       
ans=isBinaryTree(root)
if ans == True:
    print("The binary tree is a BST.")
else:
    print("The binary tree is not a BST.")
    
#Example 2
root =Node(3)
root.left = Node(2)
root.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
 
print("Example2:")       
ans=isBinaryTree(root)
if ans == True:
    print("The binary tree is a BST.")
else:
    print("The binary tree is not a BST.")