class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    #function to traverse to the end of the linked list at insert node to last
    def to_end(self,n):
        
        newnode=Node(n)
        
        if self.head is None:
            self.head=newnode
            return
 
        self.tail.next=newnode
        self.tail= newnode
        self.tail.next=self.head
        
        
        
    #function to traverse to a particular position in the linked list at that position
    def in_between(self,n,p):
        
        newnode=Node(n)
        temp=list.head
        for i in range(0,p-1):
            temp=temp.next
            
        newnode.next=temp.next
        temp.next=newnode
        
        
    
    #function to delete the first element
    def del_first(self):
        
        if(self.head == self.tail ):      
            self.head = None
            self.tail = None
            
        else:
            self.head = self.head.next;    
            self.tail.next = self.head; 
    
    
    #function to traverse to end and delete the last element
    def del_last(self):
        
        if(self.head == self.tail):
            self.head = None
            self.tail = None
            
        else:
            temp = self.head
            while(temp.next is not self.tail):
                temp = temp.next
            self.tail = temp
            self.tail.next = self.head
            
        
            
    #function to search for a value and delete that node        
    def del_mid(self,n):

        if(self.head == self.tail):
            self.head = None
            self.tail = None
        else:
            temp = self.head
            for _ in range(n-1):
                temp = temp.next
            temp.next = temp.next.next 
    
    #function to traverse through the linked list    
    def traversal(self):
        
        temp = self.head
        while(self.head != self.tail):
            print(self.head.item,end=' ')
            self.head = self.head.next
        self.head = temp  
        print(self.tail.item)
        
    #function to search for an element    
    def search(self,n):
        
        temp = self.head 
        while(temp != self.tail):
            if(temp.item == n):
               print("Element is present in the linked list")
               return 1
            temp = temp.next
        if(self.tail==n):
            print("Element is present in the linked list")
            return 1
            
        print("The element  is not present in the linked list")
        
    

    
list=LinkedList() #a-Creation

list.head=Node(1)
second=Node(2)
third=Node(3)
list.tail=third

list.head.next=second
second.next=third
third.next=list.head

print("\nLinked list initially:")
list.traversal()

n=int(input("\nenter element to insert at start:"))
newnode = Node(n)      # b-Insertion at Start
newnode.next = list.head
list.head = newnode
list.tail.next=list.head

print("\nLinked list after insertion:")
list.traversal()


n=int(input("\nenter element to insert at end:")) # b-Insertion at end
list.to_end(n)

print("\nLinked list after insertion to end:")
list.traversal()

n=int(input("\nenter element to insert in between:")) # b-Insertion in between
p=int(input("\nenter position(index) you want to enter it into:"))
list.in_between(n,p)

print("\nLinked list after insertion in between:")
list.traversal()

list.del_first() # c- deletion from beginning

print("\nLinked list after deletion from beginning:") 
list.traversal()

n=int(input("\nenter element to delete:")) # c-Deletion in between
list.del_mid(n)

print("\nLinked list after deletion :") 
list.traversal()
    
list.del_last() # c-deletion from end

print("\nLinked list after deletion from end:\n")
list.traversal() # d- traversal

n=int(input("\nenter element to search:"))
list.search(n)



    