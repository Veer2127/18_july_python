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

nnum=int(input('Enter a number:'))
f=1

for i in range(1,num+1):
    f=f*i

print("Factorial:",f)

#3)Write a Python program to get the Fibonacci series of given range.

num=int(input("Enter a number:"))

num1=0
num2=1
print(num1)
print(num2)

for i in range(2,num+1):
    num3=num1+num2
    print(num3)
    num1=num2
    num2=num3

#4) How memory is managed in Python?
'''--> In Python, memory management is primarily managed through a private
    heap space that contains all the objects and data structures. 
    The Python memory manager takes care of allocating and deallocating memory for these objects.
    It uses various strategies to efficiently manage memory, such as reference counting, 
    garbage collection, and memory pools.'''

#5) What is the purpose continue statement in python?
'''-->The continue statement in Python is used within loops
    (e.g., for loop, while loop) to skip the rest of the current 
    iteration and move on to the next iteration without executing the remaining code in the loop body.

#6)Write python program that swap two number with temp variable and
   without temp variable. 

#with temp variable

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))

temp=a
print("The value of temp variable is:",temp)

a=b
print("The value of a is",a)

b=temp
print("The value of b is",b)


#Without temp variable
a=int(input('Enter the value of a:'))
b=int(input("Enter the value of b:"))

a,b=b,a

print('A:',a)
print("B:",b)


 # 7)Write a Python program to find whether a given number is even or odd,
 # print out an appropriate message to the user.
   
     n=int(input("Enter a number:"))
oddsum=0
evensum=0

for i in range(1,n+1):
    if i%2==0:
        evensum=evensum+i

    else:
        oddsum=oddsum+i

print("Oddsum:",oddsum)
print("Evensum:",evensum)

#8) Write a Python program to test whether a passed letter is a vowel or not.

 i=input("Enter a letter:")

if i in "aeiou":
     print("Passed Letter is Vowel:")
else:
     print("Passed Letter is not a vowel:")

#9) Write a Python program to sum of three given integers. However, if
    #two values are equal sum will be zero.

    a=int(input("Enter First value :"))
b=int(input("Enter second value :"))
c=int(input("Enter third value :"))

if a==b or b==c or c==a:
    print("sum is :",0)
else:
    print("sum is :",a+b+c)

#10) Write a Python program that will return true if the two given integer
#    values are equal or their sum or difference is 5. 

    num1=int(input("Enter a number 1:-"))
num2=int(input("Enter a number 2:-"))

if num1==num2 or num1+num2==5 or num1-num2==5:
    print("True")

else:
    ("False")

    
    


    
