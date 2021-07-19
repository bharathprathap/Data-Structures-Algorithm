class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    #function to search for an element
    def search(self,data):
        
        if self is None:
            return None
        
        if self.data == data:
            return self
        
        if data < self.data and self.left:
            return self.left.search(data)
        if self.right:
            return self.right.search(data)
        else:
            return None

    #function to find the minimum value
    def findMin(self):
        if(self.left != None):
            node = self.left.findMin()
            return node
        else:
            return self
        

#function to find the inorder successor of a given value
def successor_find(node,data):
    
    n = node.search(data)
    if n is None:
        return None
    if n.right:
        return n.right.findMin()
    else:
        successor = None
        parent = node
        while parent != n:
            if n.data < parent.data:
                successor = parent
                parent = parent.left
            else:
                parent = parent.right
        return successor
    

root=Node(32)
root.left = Node(27)
root.right = Node(36)
root.left.left = Node(22)
root.left.right = Node(30)
root.right.right = Node(45)
root.right.left = Node(34)



ans=successor_find(root,22)
print("Inorder successor:\n",ans.data)

