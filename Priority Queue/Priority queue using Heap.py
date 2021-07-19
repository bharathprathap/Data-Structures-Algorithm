
class Node:
        
    def __init__(self,data,priority):
       self.data = data
       self.priority = priority
       
class PQueue_Heap:
    
    def __init__(self,max):
        self.maxSize = max+1
        self.pq = list()
        self.pq = [0 for i in range(self.maxSize)]
        self.n = 0

    def enqueue(self,data,priority):
        
        self.n += 1
        self.pq[self.n] = Node(data,priority)
        i = self.n
        while(i > 1 and self.pq[i//2].priority > self.pq[i].priority):
            self.pq[i//2],self.pq[i] = self.pq[i],self.pq[i//2]
            i//=2
            
              
    def isEmpty(self):
        if self.n == 0:
            return True
        else:
            return False
    
    def heapification(self,ind):
        minInd = ind
        l = 2*ind
        r = (2*ind)+1
        if(l <= self.n and self.pq[l].priority < self.pq[minInd].priority):
            minInd = l
        if(r <= self.n and self.pq[r].priority < self.pq[minInd].priority):
            minInd = r
        if ind != minInd:
            self.pq[ind],self.pq[minInd] = self.pq[minInd],self.pq[ind]
            self.heapification(minInd)
        
    def dequeue(self):
        
        if self.isEmpty():
            print("The queue is empty !")
        
        elif len(self.pq) == 1:
            item = self.pq.pop(n)
            self.n -= 1
            print('Data:' + str(item.data) + 'Priority' + str(item.priority))
        
        else:
            item = self.pq[1]
            self.pq[1] = self.pq[self.n]
            self.n-=1
            self.heapification(1)
            print('Data: ' + str(item.data) + '  Priority :' + str(item.priority))
            
    def print_queue(self):      
        
        for i in range(1,self.n+1):
            if(2*i + 1 <=self.n):
                print("Root : " , self.pq[i].data ,"     Left Child : ",self.pq[2*i].data,"     Right child : ",self.pq[2*i + 1].data)
            elif(2*i <= self.n):
                print("Root : " ,self.pq[i].data,"     Left Child : ",self.pq[2*i].data,"     Right child : None")
            else:
                print("Leaf node : ",self.pq[i].data)
                
                
n=int(input("Enter length of the priority queue:"))
pqueue=PQueue_Heap(n)
while(True):
    print("Enter option to perform operations on the priority Queue:\n1. ENQUEUE\n2. DEQUEUE\n3. PRINT QUEUE\n4. EXIT")
    option =int(input())
    
    if(option ==1):
        for i in range(0,n):
            inp=int(input("Enter element:"))
            priority=int(input("Enter priority:"))
            pqueue.enqueue(inp,priority)
        
    elif(option ==2):
        print("Dequed element:\n")
        pqueue.dequeue()
        
    elif(option==3):
        print("The priority queue:\n")
        pqueue.print_queue()
            
    else:
        break

