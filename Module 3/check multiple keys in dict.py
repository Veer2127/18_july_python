# Python program to check multiple keys exists in a dictionary.


mydict={
    "Name": "Manav",
    "Subject": "Python",
    "ID": 2
}
print(mydict.keys()>= {"Name","Subject"})
print(mydict.keys()>={"Name","Manav"})
print(mydict.keys()>={"ID","Name"})