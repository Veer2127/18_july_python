# Python program to find the highest 3 values in a dictionary. 

from heapq import nlargest

mydict={"a":500,"b":1000,"c":567,"d":989,"e":2565}
threelargest=nlargest(3, mydict,key=mydict.get)
print(threelargest)