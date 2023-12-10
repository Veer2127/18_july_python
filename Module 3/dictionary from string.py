# Write a Python program to create a dictionary from a string.

from collections import defaultdict, Counter
mystr="w3resource"
mydict={}
for letter in mystr:
    mydict[letter]=mydict.get(letter,0)+1
print(mydict)