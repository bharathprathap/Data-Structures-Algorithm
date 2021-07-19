class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
        self.flag = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
          
    def detect_Loop(self):
        
        temp=self.head
        while (temp != None):
            
            if (temp.flag == 1):
                print("A loop is present.")
                return 
    
            temp.flag = 1; 
            temp = temp.next;   
        print("No loop present.")
        return
    
list=LinkedList() #example 1.(loop present)

list.head=Node(1)
second=Node(2)
third=Node(3)
third.next=list.head

list.head.next=second
second.next=third

print("\nChecking for loop in example1..")
list.detect_Loop()


list2=LinkedList() #example2 (loop not present)

list2.head=Node(8)
two=Node(5)
three=Node(3)
list2.head.next=two
two.next=three

print("\nChecking for loop in example2..")
list2.detect_Loop()


