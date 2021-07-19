class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    
    def __init__(self):
        self.head = None
        
    #function to push in values to the stack
    def push(self,data):
        temp = self.head
        self.head = Node(data)
        self.head.next = temp
    
    #function to remove the top value from the stack
    def pop(self):
        
        if self.IsEmpty():
            print("\nThe Stack is empty")
        else:
            temp=self.head
            self.head = self.head.next
            temp=None
            print("\nTop element popped out")
            
    #function to check if stack is empty
    def IsEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
    #function that prints the topmost element of stack
    def peek(self):
        if self.IsEmpty():
            print("The stack is empty")
        else:
            print('The topmost element is: ' , self.head.data)
   
    #function that prints the stack         
    def print_stack(self):
        
        print("\nStack:")
        temp=self.head
        while(temp != None):
            print(temp.data,end = " ")
            temp = temp.next
        return
    

    
stack = Stack()#creating a stack 
while(True):
    
    print("\nEnter option to perform operations on Stack:\n1. PUSH\n2. POP\n3. PEEK\n4. PRINT \n5. EXIT")
    option =int(input())
    if(option ==1):
        element=int(input("Enter element:"))
        stack.push(element) 
        
    elif(option ==2):
        stack.pop()
        
    elif(option==3):
        stack.peek()
        
    elif(option == 4):
        stack.print_stack()

    else:
        break




            