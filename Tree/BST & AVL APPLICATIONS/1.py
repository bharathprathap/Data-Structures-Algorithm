class Node:
    def __init__(self,data):
        self.data = data
        self.right= None
        self.left= None

#function minimize the height of the BST       
def bst_minimizer(array):
    
    if not array :
        return None
    mid=((len(array))//2)
    root= Node(array[mid])
    root.left=bst_minimizer(array[:mid])
    root.right=bst_minimizer(array[mid+1:])
    return root

#function to traverse through and print the BST
def traverse(root):
    
    if root is not None:
        print("Root node: ", root.data)
    if root.left is not None:
        print("Traversing Left",end = ' ')
        traverse(root.left)
    if root.right is not None:
        print("Traversing Right",end = ' ')
        traverse(root.right)


array=[]     
n=int(input("Enter the length of the array:"))
for i in range(0,n):
    inp=int(input("Enter input:"))
    array.append(inp)

array.sort()

root_node=bst_minimizer(array)
print("Sorted array to a balanced Binary Search Tree:")
traverse(root_node)
    
    