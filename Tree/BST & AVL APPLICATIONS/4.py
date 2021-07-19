class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nodeCount = 0
        
        
#function to insert elements into the BST        
def insert(root,val):
    
    if root is None:
        return Node(val)
    
    else:
        if root.data == val:
            return root
        elif root.data>val:
            root.left=insert(root.left,val)
            root.nodeCount+=1
        else:
            root.right=insert(root.right,val)
            
    return root
        
#function to find the kth smallest element       
def kthSmallest(root, k):
     
    if (root == None):
        return None         
    count = root.nodeCount + 1
    if (count == k):
        return root
    if (count > k):
        return kthSmallest(root.left, k) 
    return kthSmallest(root.right, k - count)


root =Node(5)
insert(root,4)
insert(root,3)
insert(root,2)
insert(root,1)
insert(root,6)
insert(root,7)
insert(root,8)

k=int(input("Enter k:"))
ans=kthSmallest(root,k)
print("The",k,"th smallest element is:",ans.data)
