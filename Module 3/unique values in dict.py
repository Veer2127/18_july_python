# Python program to print all unique values in a dictionary.


mydict={"ID":1,"ID":2,"ID":3,"ID":4,"ID":3,"ID":2,"ID":5,"ID":1}
mylist=[]

for value in mydict.values():
    if value in mylist:
        continue
    else:
        mylist.append(value)

    print(mylist)