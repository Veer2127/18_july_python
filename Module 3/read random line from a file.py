# Python program to read a random line from a file. 

#fl=open("test.txt","x")
fl=open("test.txt","r+")
#print(fl.read())
print(fl.readlines()[1])