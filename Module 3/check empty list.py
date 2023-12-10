# Program to check a list is empty or not

mylist=[]

n=int(input("Enter number of list elements : "))

for i in range(n):
    el=input("Enter the list elements : ")
    mylist.append(el)
    print(mylist)

if mylist==[]:
    print("Your list is empty")
else:
    print("Your list is not empty")
