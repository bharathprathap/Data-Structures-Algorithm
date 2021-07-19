import array

arr=array.array('i',[1,2,3,4,5])  #a

n=int(input("\nenter element to insert:"))
arr.insert(0,n)#b-at start

m=int(input("\nenter element to insert at back:"))
arr.append(m) #b -at end

ind=int(input("\nenter index to insert:"))
n=int(input("\nenter element to insert:"))
arr.insert(ind,n)#b-at index

val=int(input("enter element to search:"))
n=int(input("\nenter element to insert:"))
arr.insert(arr.index(val)+1,n) #b-based on value

print("Array:")
for i in range(0,len(arr)): 
    print(arr[i],end=" ")

arr.pop(0) # c-delete from start
arr.pop() # c-delete from end
ind=int(input("\nenter index to delete:"))
arr.pop(ind)# c-delete at an index
n=int(input("\nenter value to delete:"))
arr.remove(n)#  c-delete based on value


for i in range(0,len(arr)): #d- traversal
    print(arr[i],end=" ")
  
val=int(input("\nenter element to search:"))#e-search based on value
print("index:",arr.index(val))
    
ind=int(input("\nenter index to search:"))  #e-search based on index
print("value:",arr[ind])