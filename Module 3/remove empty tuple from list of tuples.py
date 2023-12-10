# Python program to remove an empty tuple(s) from a list of tuples.


mylist=[(),(),("manav","python"),("Java","CSS"),("computer","tops")]
mylist=[t for t in mylist if t]
print(mylist)