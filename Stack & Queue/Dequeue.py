class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Deque:
    
    def __init__(self):
        self.front = None
        self.rear = None

    #function to check if queue is empty        
    def isEmpty(self):
        if(self.rear == None and self.front == None):
            return True
        else:
            return False
        
    #function to insert elements at Rear of the queue
    def insert_at_Rear(self,data):
        
        newnode = Node(data)
        if(self.isEmpty()):
            self.front =newnode
            self.rear =newnode
            
        else:
            self.rear.next=newnode
            self.rear=newnode
            
    #function to insert elements at front of the queue
    def insert_at_front(self,data):
        
        newnode = Node(data)
        if(self.isEmpty()):
            self.front =newnode
            self.rear =newnode
            
        else:
            newnode.next=self.front
            self.front=newnode
            
    #function to delete elements at the front of the queue    
    def delete_at_front(self):
        if(self.isEmpty()):
            print("Empty queue")
        elif(self.front==self.rear):
            self.front=None
            self.rear=None
        else:
            self.front =self.front.next
            print("Element dequeued")
            
    #function to delete elements at the rear of the queue    
    def delete_at_rear(self):
        if(self.isEmpty()):
            print("Empty queue")
            
        elif(self.front==self.rear):
            self.front=None
            self.rear=None
        else:
            temp=self.front
            while(temp.next!=self.rear):
                temp=temp.next
            temp.next=None
            self.rear=temp
            print("Element dequeued")
    
    #function to return the front element
    def peek(self):
        if(self.isEmpty()):
            print("Empty queue")
        else:
            print("Front Element:",self.front.data)
    
    
    #function to print the queue
    def print_queue(self):
        print("Queue:")        
        temp=self.front
        while(temp != None):
            print(temp.data,end = " ")
            temp = temp.next
        print("\n")
        return
    
    
deque=Deque()
while(True):
    
    print("Enter option to perform operations on Deque:\n1. Insert at Rear\n2. Insert at Front\n3. Delete from front\n4. Delete from rear \n5. PEEK\n6. PRINT \n7. EXIT")
    option =int(input())
    if(option ==1):
        element=int(input("Enter element:"))
        deque.insert_at_Rear(element)
           
    elif(option ==2):
        element=int(input("Enter element:"))
        deque.insert_at_front(element)
        
    elif(option ==3):
        deque.delete_at_front()
        
    elif(option ==4):
        deque.delete_at_rear()
        
    elif(option==5):
        deque.peek()
        
    elif(option == 6):
        deque.print_queue()
    
    else:
        break
    
    