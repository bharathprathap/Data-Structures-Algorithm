class Queue:
    def __init__(node):
        node.data = []

    #function to check if queue is empty  
    def isEmpty(node):
        return node.data == []

    #function to enqueue elements to queue
    def enqueue(node, data):
        node.data.insert(0,data)

    #function to dequeue elements to queue
    def dequeue(node):
        return node.data.pop()


#function to reverse the queue     
def Reverse():    
    if(queue.isEmpty()):
        return
    temp = queue.data[-1]
    queue.dequeue()
    Reverse()
    queue.enqueue(temp)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)

print("\nQueue before reversal:")
print(queue.data)
Reverse()
print("\nAfter reversal:")
print(queue.data)