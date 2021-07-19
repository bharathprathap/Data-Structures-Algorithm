class PriorityQueue:
    
    def __init__(self):
        self._qlist = list()
        
    def isEmpty(self):
        return len(self._qlist) == 0
    
    def len(self):
        return len(self._qlist)
    
    def enqueue(self,item,priority):
        entry=_PriorityQEntry(item,priority)
        self._qlist.append(entry)
        
    def dequeue(self):
        
        assert not self.isEmpty(),"Cannot dequeue from an empty queue."
        
        highest=self._qlist[0].priority
        high_index = 0
        for i in range(self.len()):
            if (self._qlist[i].priority < highest):
                highest=self._qlist[i].priority
                high_index = i
        entry=self._qlist.pop(high_index)
        return entry.item
    
class _PriorityQEntry(object):
    def __init__(self,item,priority):
        self.item=item
        self.priority=priority
        
        
pqueue=PriorityQueue()

while(True):
    print("Enter option to perform operations on the priority Queue:\n1. ENQUEUE\n2. DEQUEUE\n3. EXIT")
    option =int(input())
    
    if(option ==1):
        
        n=int(input("Enter length of the priority queue:"))
        for i in range(0,n):
            inp=int(input("Enter element:"))
            priority=int(input("Enter priority:"))
            pqueue.enqueue(inp,priority)
        
    elif(option ==2):
        print("Dequed element:",pqueue.dequeue())
            
    else:
        break


    
