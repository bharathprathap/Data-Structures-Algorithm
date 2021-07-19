
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
    
#function that prints the stack
def print_stack(stack):
    print("\nElements of the stack:")
    for element in stack:
        print(element)

#function to reverse a stack       
def reverse(stack):
    if not isEmpty(stack):
        temp=pop(stack)
        reverse(stack)
        insertAtBottom(stack,temp)
        
#function to insert an element at bottom using recursion
def insertAtBottom(stack, item): 
    if isEmpty(stack): 
        push(stack, item) 
    else: 
        temp = pop(stack) 
        insertAtBottom(stack, item) 
        push(stack, temp) 

    
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