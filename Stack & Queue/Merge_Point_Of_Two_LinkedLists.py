class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def length(self): 
        temp = self.head 
        count = 0 
  
        while (temp): 
            count += 1
            temp = temp.next
        return count
        
def findmergepoint(list1,list2):
    x=list1.length()
    y=list2.length()
    
    temp1=list1.head
    temp2=list2.head
    
    
    while(temp1.next!=None):
        temp2=list2.head
        while(temp2.next!=None):
            if(temp1==temp2):
                return temp1.item
            temp2= temp2.next
        temp1=temp1.next
        
    return 0
    
#creating linked list 1
list1=LinkedList() 

list1.head=Node(1)  
second=Node(2)
third=Node(3)

list1.head.next=second
second.next=third

#creating linked list 2
list2=LinkedList()

list2.head=Node(4)
fifth=Node(5)
sixth=Node(6)

list2.head.next=fifth
fifth.next=sixth


#creating a merge point
sixth.next=second


val=findmergepoint(list1,list2)
if(val==0):
    print("The linked lists doesnt merge at any point.")
else:
    print("The merging point is the node having the value:",val)




