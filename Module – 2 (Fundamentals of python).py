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
    iteration and move on to the next iteration without executing the remaining code in the loop body.'''

#6)Write python program that swap two number with temp variable and without temp variable. 

  #withtempvariable

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))

temp=a
print("The value of temp variable is:",temp)

a=b
print("The value of a is",a)

b=temp
print("The value of b is",b)


'''Without temp variable'''
a=int(input('Enter the value of a:'))
b=int(input("Enter the value of b:"))

a,b=b,a

print('A:',a)
print("B:",b)


'''7)Write a Python program to find whether a given number is even or odd,
       print out an appropriate message to the user.'''
   
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


#11) Write a python program to sum of the first n positive integers.

n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integers:", sum_num)


#12)Write a Python program to calculate the length of a string.

str = input("Enter a string: ")

counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)

#13) Write a Python program to count the number of characters (character frequency) in a string

n=input("Enter the String: ")
s=()
for i in n:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
print(s)


#14) What are negative indexes and why are they used?

'''--> In Python, negative indexes are used to access elements from a sequence 
        (like strings, lists, or tuples) in a reverse order. Instead of counting from 
        the beginning of the sequence, negative indexes count from the end. The last element 
        in the sequence is at index -1, the second-to-last element is at index -2, and so on.'''



#15) Write a Python program to count occurrences of a substring in a string.

str1 = 'hello Welcome to tops!'
print(str1.count("wel"))



#16)Write a Python program to count the occurrences of each word in a given sentence

str='hello welcome to tops!'
print(str.find("to"))



#17) Write a Python program to get a single string from two given strings,
    #separated by a space and swap the first two characters of each string.

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


'''18) Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add
'ly' instead if the string length of the given string is less than 3, leave it
unchanged.'''

mystr=input("Enter a string: ")

if len(mystr)<3:
    print("Unchange",mystr)

if mystr.endswith('ing'):
    mystr='ly'
elif len(mystr)>=3:
    mystr+='ing'
print(mystr)


'''19) Write a Python program to find the first appearance of the substring
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the
whole 'not'...'poor' substring with 'good'. Return the resulting string.'''

def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))

#20)Write a Python function that takes a list of words and returns the length
    #of the longest one.

mystr="Hello and welcome to tops!"

print(len(mystr)) 

#21) Write a Python function to reverses a string if its length is a multiple of 4.

mystr=input('Enter a string:')

length=len(mystr)

print("Length=",length)

if length%4==0:
    print("Reverse of string is", mystr[::-1])

else:
    print("The string is not reversed")


'''22) Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string.'''








#23)Write a Python function to insert a string in the middle of a string.

test_str = 'welcome the tops!'
mid_str = 'to'

a = test_str.split()
b = len(a) // 3

n = ' '.join(a[:b] + [mid_str] + a[b:])

print("The original string is : " + str(test_str))
print("The formulated string is : " + str(n))




