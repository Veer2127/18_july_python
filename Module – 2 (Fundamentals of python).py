#*Module – 2 (Fundamentals of python)*


#1) Write a Python program to check if a number is positive, negative or zero:

num=int(input("Enter a Number"))
if num>=0:
    print("It is a Positive Number")
elif num==0:
    print("it is zero")
else:
    print("it is a negative number")

# 2)Write a Python program to get the Factorial number of given number.

num=int(input("Enter a Number:"))

fact=1

a=1

while a<=num:
    fact=fact*a
    a=a+1
print("The Factorial of",num,"is",fact)