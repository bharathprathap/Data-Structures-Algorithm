class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

#function to insert elements into the BST        
def insert(root,val):
    
    if root is None:
        return Node(val)
    
    else:
        if root.data == val:
            return root
        elif root.data>val:
            root.left=insert(root.left,val)
        else:
            root.right=insert(root.right,val)
            
    return root

#function to search for a value in the BST
def search(root,val):
    
    if root is None:
        return 0
    
    else:
        if root.data==val:
            return root        
        elif root.data>val:
            return search(root.left,val)
        else:
            return search(root.right,val)

#function to traverse through and print the BST
def traverse(root):
    if root is not None:
        print(root.data)
    if root.left is not None:
        print("Traversing Left",end = ' ')
        traverse(root.left)
    if root.right is not None:
        print("Traversing Right",end = ' ')
        traverse(root.right)

#function to return the smallest value in the BST
def getMin(root):
    
    temp = root
    while(temp.left is not None):
        temp = temp.left
    return temp

#function to delete a value from the BST which is passed a parameter
def deletion(root,data):
    
    if root is None:
        return root
    
    if data < root.data:
        root.left = deletion(root.left,data)

    elif data > root.data:
        root.right = deletion(root.right,data)
    
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        minimum = getMin(root.right)
        root.data = minimum.data
        root.right = deletion(root.right,minimum.data)
    return root



root_val=int(input("Enter the root node of the BST:"))
root=Node(root_val)

while(True):
    print("Enter option to perform operations on the BST:\n1. insert\n2. delete\n3. search\n4. print the BST\n5. EXIT")
    option =int(input())    
    
    if(option ==1):
        inp=int(input("Enter element:"))
        insert(root,inp)
        
    elif(option ==2):
        del_elmnt=int(input("Enter element you want to delete:"))
        deletion(root,del_elmnt)
        
            
    elif(option ==3):
        val=int(input("Enter value to search:"))
        node=search(root,val)
        if(node==0):
            print("Element not found!")
        else:
            print("Element found!")
    
    elif(option ==4):
        print("Binary search tree:")
        traverse(root)

    else:
        break
            
            
        
        
        
    