
#function to check if stack is empty
def isEmpty(stack):
    return len(stack) ==0

#function to push in values to the stack
def push(stack,element):
    stack.append(element)

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

#function to reverse a stack       
def reverse(stack):
    temp1 = []
    while not isEmpty(stack):
        push(temp1,pop(stack))
    temp2 = []
    while not isEmpty(temp1):
        push(temp2,pop(temp1))
    while not isEmpty(temp2):
        push(stack,pop(temp2))

    
    


stack=[]#creating a stack 

push(stack,1)
push(stack,2)
push(stack,3)
push(stack,4)
push(stack,5)

print("\nStack initially:")
print_stack(stack)

print("\nStack After reversal:")
reverse(stack)
print_stack(stack)
