class Node(object):
	def __init__(self, data):
		self.left=None
		self.right=None
		self.data=data
		self.height=1

class AVL_Tree(object):

    #function to insert elements to the AVL tree
    def insert(self,root,val):
        if not root:
            return Node(val)
        elif val<root.data:
            root.left=self.insert(root.left,val)
        else:
            root.right=self.insert(root.right,val)

        root.height=1+max(self.getHeight(root.left),self.getHeight(root.right))
        balance=self.getBalance(root)

        if balance>1 and val<root.left.data:
            return self.rotate_right(root)

        if balance<-1 and val>root.right.data:
            return self.rotate_left(root)

        if balance>1 and val>root.left.data:
            root.left=self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance<-1 and val<root.right.data:
            root.right=self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    #function to delete an element from the AVL tree
    def delete(self,root,key):
        
        if not root:
            return root        
        elif key<root.data:
            root.left = self.delete(root.left, key)
        elif key>root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMin_val(root.right)
            root.data = temp.data
            root.right = self.delete(root.right,temp.data)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance>1 and self.getBalance(root.left) >= 0:
            return self.rotate_right(root)

        if balance<-1 and self.getBalance(root.right) <= 0:
            return self.rotate_left(root)

        if balance>1 and self.getBalance(root.left)<0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance<-1 and self.getBalance(root.right)>0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root
    
    #function to search for a value
    def search(self,root,val):
        
        if root is None:
            return 0
        
        else:
            if root.data==val:
                return root        
            elif root.data>val:
                return self.search(root.left,val)
            else:
                return self.search(root.right,val)
            
    #function to rotate_left an AVL tree
    def rotate_left(self, node):
        
        y=node.right
        x=y.left
        y.left=node
        node.right=x

        node.height=1+max(self.getHeight(node.left),self.getHeight(node.right))
        y.height=1+max(self.getHeight(y.left),self.getHeight(y.right))

        return y

    #function to rotate_right an AVL tree
    def rotate_right(self, node):
        y=node.left
        x=y.right
        y.right=node
        node.left=x

        node.height=1 + max(self.getHeight(node.left),self.getHeight(node.right))
        y.height=1 + max(self.getHeight(y.left),self.getHeight(y.right))

        return y

    #function to return the height
    def getHeight(self, root):
        
        if not root:
            return 0
        return root.height

    #function to calculate the balance factor
    def getBalance(self, root):
        
        if not root:
            return 0

        return self.getHeight(root.left)-self.getHeight(root.right)

    #function to get the minimum value
    def getMin_val(self, root):
        
        if root is None or root.left is None:
            return root
        return self.getMin_val(root.left)

    #function to traverse through and print the BST
    def traverse(self,root):
        
        if root is not None:
            print(root.data)
        if root.left is not None:
            print("Traversing Left",end = ' ')
            self.traverse(root.left)
        if root.right is not None:
            print("Traversing Right",end = ' ')
            self.traverse(root.right)



avl=AVL_Tree()
root_val=int(input("Enter the root node of the BST:"))
root=Node(root_val)

while(True):
    print("Enter option to perform operations on the AVL Tree:\n1. insert\n2. delete\n3. search\n4. print \n5. EXIT")
    option =int(input())    
    
    if(option ==1):
        inp=int(input("Enter element:"))
        avl.insert(root,inp)
        
    elif(option ==2):
        del_elmnt=int(input("Enter element you want to delete:"))
        avl.delete(root,del_elmnt)
        
            
    elif(option ==3):
        val=int(input("Enter value to search:"))
        node=avl.search(root,val)
        if(node==0):
            print("Element not found!")
        else:
            print("Element found!")
    
    elif(option ==4):
        print("Binary search tree:")
        avl.traverse(root)

    else:
        break
