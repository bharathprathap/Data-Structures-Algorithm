class Queue:
    
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.queue = list()
        
    #function to enqueue elements to the queue
    def enqueue(self,element):
        if(self.isEmpty()):
            self.front +=1
            self.rear -=1
            self.queue.append(element)
            
        else:
            self.queue.append(element)
            self.rear += 1
    
    #function to dequeue elements to the queue        
    def dequeue(self):
        if(self.isEmpty()):
            print("Empty queue")
        else:
            self.front +=1
            print("Element dequeued")
       
    #function to check if queue is empty        
    def isEmpty(self):
        if(self.rear == -1 and self.front == -1):
            return True
        else:
            return False
        
    #function to return the front element
    def peek(self):
        if(self.isEmpty()):
            print("Empty queue")
        else:
            print("Front Element:",self.queue[self.front])
    
    #function to return the length of the queue        
    def length(self):
        return len(self.queue)
    
    
    #function to print the queue
    def print_queue(self):
        print("Queue:")
        for i in range(self.front,len(self.queue)):
            print(self.queue[i], end=' ')
        print("\n")
            

    
    
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
    
        
            
        
            