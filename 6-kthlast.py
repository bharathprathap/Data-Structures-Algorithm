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
        
  
    #function to print the linked lisy
    def listprint(self):
        
        printval = self.head
        while printval is not None:
            print (printval.item,end=" ")
            printval = printval.next
    
  
        

    
list=LinkedList() #a-Creation

n=int(input("Enter number of inputs:"))

m=int(input())
list.head=Node(m)
temp=list.head
for i in range(1,n):
    m=int(input())
    list.to_end(m)
    

print("\nLinked list :")
list.listprint()

k=int(input("\nEnter k:"))

for i in range(0,n-k):
    temp=temp.next
    
print(temp.item)
    