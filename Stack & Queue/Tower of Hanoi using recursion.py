#Solving Towers of Hanoi problem using recursion
def TOH(n,A,B,C):
    if(n>0):
        TOH(n-1,A,C,B)
        print("Move a disc from ",A,"to ",C)
        TOH(n-1,B,A,C)
		
n=int(input("Enter size of the tower:"))
TOH(n,'A','B','C')