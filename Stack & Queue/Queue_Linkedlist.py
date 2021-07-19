-class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    
    def __init__(self):
        self.front = None
        self.rear = None

    #function to check if queue is empty        
    def isEmpty(self):
        if(self.rear == None and self.front == None):
            return True
        else:
            return False
        
     #function to enqueue elements to the queue
    def enqueue(self,data):
        
        newnode = Node(data)
        if(self.isEmpty()):
            self.front =newnode
            self.rear =newnode
            
        else:
            self.rear.next=newnode
            self.rear=newnode
            
     #function to dequeue elements to the queue        
    def dequeue(self):
        if(self.isEmpty()):
            print("Empty queue")
        else:
            self.front =self.front.next
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
    
    
queue=Queue()
while(True):
    
    print("Enter option to perform operations on Queue:\n1. ENQUEUE\n2. DEQUEUE\n3. PEEK\n4. PRINT \n5. EXIT")
    option =int(input())
    if(option ==1):
        element=int(input("Enter element:"))
        queue.enqueue(element)
           
    elif(option ==2):
        queue.dequeue()
        
    elif(option==3):
        queue.peek()
        
    elif(option == 4):
        queue.print_queue()
    
    else:
        break
    
    