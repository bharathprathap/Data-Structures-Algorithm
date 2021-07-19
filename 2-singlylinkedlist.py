class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    #function to traverse to the end of the linked list at insert node to last
    def to_end(self,n):
        
        newnode=Node(n)
        
        if self.head is None:
            self.head=newnode
            return
        
        temp=list.head
        while(temp!=None and temp.next != None):
            temp=temp.next
        temp.next=newnode
        
        
    #function to traverse to a particular position in the linked list at that position
    def in_between(self,n,p):
        
        newnode=Node(n)
        temp=list.head
        for i in range(0,p-1):
            temp=temp.next
            
        newnode.next=temp.next
        temp.next=newnode
        
        
    #function to print the linked lisy
    def listprint(self):
        
        printval = self.head
        while printval is not None:
            print (printval.item,end=" ")
            printval = printval.next
    
    #function to traverse to end and delete the last element
    def del_last(self):
        
        temp = self.head
        previous = None
        while temp.next:
            previous = temp
            temp = temp.next

        previous.next = None
        temp = None
            
        
            
    #function to search for a value and delete that node        
    def del_mid(self,n):

        temp = self.head
        previous = None

        while temp:
            if temp.item == n:
                break
            previous = temp
            temp = temp.next

        previous.next = temp.next
        temp = None     
    
    #function to traverse through the linked list    
    def traversal(self):
        
        temp = self.head
        while(self.head):
            print(self.head.item,end=' ')
            self.head = self.head.next
        self.head = temp  
        
    #function to search for an element    
    def search(self,n):
        
        temp = self.head 
        while(temp):
            if(temp.item == n):
               print("Element is present in the linked list")
               return 1
            temp = temp.next
            
        print("The element  is not present in the linked list")
        
    

    
list=LinkedList() #a-Creation

list.head=Node(1)
second=Node(2)
third=Node(3)

list.head.next=second
second.next=third

print("\nLinked list initially:")
list.listprint()

n=int(input("\nenter element to insert at start:"))
newnode = Node(n)      # b-Insertion at Start
newnode.next = list.head
list.head = newnode

print("\nLinked list after insertion:")
list.listprint()


n=int(input("\nenter element to insert at end:")) # b-Insertion at end
list.to_end(n)

print("\nLinked list after insertion to end:")
list.listprint()

n=int(input("\nenter element to insert in between:")) # b-Insertion in between
p=int(input("\nenter position(index) you want to enter it into:"))
list.in_between(n,p)

print("\nLinked list after insertion in between:")
list.listprint()

list.head=list.head.next # c- deletion from beginning

print("\nLinked list after deletion from beginning:") 
list.listprint()

n=int(input("\nenter element to delete:")) # c-Deletion in between
list.del_mid(n)

print("\nLinked list after deletion :") 
list.listprint()
    
list.del_last() # c-deletion from end

print("\nLinked list after deletion from end:\n")
list.traversal() # d- traversal

n=int(input("\nenter element to search:"))
list.search(n)



    