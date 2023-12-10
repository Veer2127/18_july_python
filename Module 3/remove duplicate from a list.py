mylist=[]
n=int(input("How many elements you want to enter? :"))

for i in range(n):
    el=int(input("Enter the elements in list :"))
    mylist.append(el)
print(list(set(mylist)))