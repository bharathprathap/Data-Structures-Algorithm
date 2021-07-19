class Circular_Queue:
    
    def __init__(self,size):
        self.front = -1
        self.rear = -1
        self.size = size
        self.queue = [None]*size
        
    #function to enqueue elements to the queue
    def enqueue(self,element):
        
        if ((self.rear+1) % self.size == self.front):
            print("Overflow!!")
            
        elif(self.isEmpty()):
            self.front +=1
            self.rear +=1
            self.queue[self.rear] = element
            
        else:
            self.rear = (self.rear + 1) % self.size  
            self.queue[self.rear] = element
    
    #function to dequeue elements to the queue        
    def dequeue(self):
        if(self.isEmpty()):
            print("Empty queue")
        elif(self.front == self.rear):
            
            temp=self.queue[self.front]
            self.front = -1
            self.rear = -1
            print("Element dequeued")
            return temp
            
        else:
            temp=self.queue[self.front]
            self.front =(self.front +1) % self.size
            print("Element dequeued")
            return temp
       
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
        if (self.rear >= self.front):  
            for i in range(self.front, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print("\n") 
  
        else: 
            for i in range(self.front, self.size): 
                print(self.queue[i], end = " ") 
            for i in range(0, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print("\n") 
            

    
n=int(input("Enter size:"))
cir_queue=Circular_Queue(n)
flag=0
while(True):
    print("Enter option to perform operations on Circular Queue:\n1. ENQUEUE\n2. DEQUEUE\n3. PEEK\n4. PRINT \n5. EXIT")
    option =int(input())
    if(option ==1):
        
        #flag is implemented to see if its the initial ENQUEUE call,if then the user gets to enqueue multiple elements at a time.
        if(flag==0):
            flag=1
            print("\nEnter elements:")
            for i in range(0,n):
                element=int(input())
                cir_queue.enqueue(element)
        else:
            print("\nEnter element:")
            element=int(input())
            cir_queue.enqueue(element)
           
    elif(option ==2):
        cir_queue.dequeue()
        
    elif(option==3):
        cir_queue.peek()
        
    elif(option == 4):
        cir_queue.print_queue()
    
    else:
        break
    
        
            
        
            