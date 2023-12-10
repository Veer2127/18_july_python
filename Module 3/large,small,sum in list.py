# a Python function to get the largest number, smallest num and sum of all from a list.

mylist=[]
n=int(input("Enter number of list : "))

for n in range(n):
    value=int(input("Enter values : "))
    mylist.append(value)
    
print("Maximum element in the list is :", max(mylist))
print("Minimum element in the list is :", min(mylist))
print("Sum of elements in the list is :", sum(mylist))



