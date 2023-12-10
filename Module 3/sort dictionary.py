# Program to sort a dictionary by value. 


import operator

mydict={1:2,3:4,4:3,2:1,0:0}
print("Original dictionary:",mydict)
sort_mydict=sorted(mydict.items(),key=operator.itemgetter(1))
print("Dictionary in ascending order by value:",sort_mydict)
sort_mydict=dict(sorted(mydict.items(),key=operator.itemgetter(1),reverse=True))
print("Dictionary in descending order by value:",sort_mydict)