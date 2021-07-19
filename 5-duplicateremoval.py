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
        
    
    #Function to remove duplicates
    def del_duplicates(self):

        current = self.head

        while current:
            temp = current
            while temp.next:
                if current.item == temp.next.item:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
            current = current.next
        
    

    
list=LinkedList() 

n=int(input("Enter number of inputs:"))

m=int(input())
list.head=Node(m)
temp=list.head
for i in range(1,n):
    m=int(input())
    list.to_end(m)
    

print("\nLinked list initially:")
list.listprint()

print("\nLinked list after duplicate element removal:")
list.del_duplicates()
list.listprint()
print("\n")
    