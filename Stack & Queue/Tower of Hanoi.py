class stack:

    def __init__(self, name):
        self.data = list()
        self.name = name

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def top(self):
        return self.data[len(self.data) - 1]

    def pop(self):
        return self.data.pop()

def Tower_of_Hanoi(n):
    
    stack_A = stack("A")
    stack_B = stack("B")
    stack_C = stack("C")

    total_moves = (2 ** n) - 1

    
    for i in range(n, 0, -1):
        stack_A.push(i)

    if n % 2 == 0:  
        temp=stack_B
        stack_B=stack_C
        stack_C=temp

    for i in range(total_moves):
        
        if i % 3 == 0:
            move(stack_A, stack_C)
            
        if i % 3 == 1:
            move(stack_A, stack_B)
            
        if i % 3 == 2:
            move(stack_B, stack_C)
        
def move(stack1, stack2):
    if stack1.is_empty():
        stack1.push(stack2.pop())
        print("Move the disk from ",stack2.name, " to ", stack1.name)
    elif stack2.is_empty():
        stack2.push(stack1.pop())
        print("Move the disk from ",stack1.name, " to ", stack2.name)
    elif stack2.top() < stack1.top():
        stack1.push(stack2.pop())
        print("Move the disk from ",stack2.name, " to ", stack1.name)
    else:
        stack2.push(stack1.pop())
        print("Move the disk from ",stack1.name, " to ", stack2.name)




n = int(input("Enter the number disks: "))
Tower_of_Hanoi(n)
