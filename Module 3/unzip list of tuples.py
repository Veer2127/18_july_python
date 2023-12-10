# Python program to unzip a list of tuples into individual lists.


mytuple=[(1,2),(3,4),(5,6),(7,8),(9,10)]
print(list(zip(*mytuple)))