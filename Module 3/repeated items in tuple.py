# Python program to find the repeated items of a tuple.


mytuple=(1,1,2,3,4,5,5,6,7,7)
for i in mytuple:
    if mytuple.count(i)>1:
        print("Item is repeated")
