
#function to check if stack is empty
def isEmpty(stack):
    return len(stack) ==0

#function to push in values to the stack
def push(stack,element):
    stack.append(element)
    print("\n",element," pushed")

#function to remove the top value from the stack
def pop(stack):
    if(isEmpty(stack)):
        print("\nstack is empty")
    else:
        return stack.pop()
    
#function that prints the topmost element of stack
def peek(stack):
    n=len(stack)
    print("\nPeek:",stack[n-1])
    
#function that prints the stack
def print_stack(stack):
    print("\nElements of the stack:")
    for element in stack:
        print(element)

    
    


stack=[]#creating a stack 
while(True):
    
    print("Enter option to perform operations on Stack:\n1. PUSH\n2. POP\n3. PEEK\n4. PRINT \n5. EXIT")
    option =int(input())
    if(option ==1):
        element=int(input("Enter element:"))
        push(stack,element) 
           
    elif(option ==2):
        pop(stack)
        
    elif(option==3):
        peek(stack)
        
    elif(option == 4):
        print_stack(stack)
    
    else:
        break
                

