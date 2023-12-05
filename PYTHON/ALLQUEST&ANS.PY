# Q1 => WIRTE A PYTHON PROGRAM TO CHECK IF A NUMBER IS POSITIVE,NEGATIVE OR ZERO.

print(" Q1 => WIRTE A PYTHON PROGRAM TO CHECK IF A NUMBER IS POSITIVE,NEGATIVE OR ZERO. ")
print("      <====================================================================>")

num  = float(input('  Q-1 Enter a number : '))
if num > 0:
    print("Number positive")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")



print("      <====================================================================>")

'''
<====================================================================>
'''
# Q2=> WRITE A PYTHON PROGRAM TO GET THE FACTORAL NUMBER OF GIVEN NUMBER


print("Q2=> WRITE A PYTHON PROGRAM TO GET THE FACTORAL NUMBER OF GIVEN NUMBER : ")
print("      <====================================================================>")

def factrol(n):
    if n == 0 or n ==1:
        return 1
    else :
        return n *factrol(n-1)

num = int(input("Enter a Number"))
print(f"   Factrol of {num}is {factrol(num)}")


print("      <====================================================================>")

'''
<====================================================================>

'''

# Q3 => Write a Python program to get the Fibonacci series of given range.


print("Q3 => Write a Python program to get the Fibonacci series of given range : ")

print("      <====================================================================>")

def fibo(n):
    fib_series = [0,1]
    while len(fib_series) <n :
        fib_series.append(fib_series[-1]+fib_series[-2])
    return fib_series

n = int(input("Enter The Range for Fibonacci Series"))
print(f"Fibonacci series{fibo(n)}")

print("      <====================================================================> ")


'''
<====================================================================>

'''
print("      <====================================================================>")

'''

Q-4 => How Memory is managed in python
Ans =>  Python uses automatic memory management . The core is managed by a private heap space ,
and the interpreter takes care of memory allocation and deallocation.

Q-5 =>  What is the purpose continue statement in python?
The continue statement is used to skip the rest of the code
inside a loop for the current iteration and move to the next iteration...

'''
print("      <====================================================================>")

'''
<====================================================================>
'''
# Q6  Write python program that swap two number with temp variable and without temp variable.


print (" Q6  Write python program that swap two number with temp variable and without temp variable : ")

print("      <====================================================================>")
# with temp variable

a= 5
b= 10
temp = a
a=b
b=temp
# without temp variable
a =5
b=10
a,b = b,a

print("      <====================================================================>")

'''
<====================================================================>

'''
# Q-7 Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.

print("Q-7 Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user: ")

num = int(input( " Enter a Number : "))
if num % 2==0:
    print(" Even Number")
else:
    print(" Odd Number")

# Q-7  Write a Python program to test whether a passed letter is a vowel or not.

print(" Q-7  Write a Python program to test whether a passed letter is a vowel or not : => :   ")


letter = input (" Enter a letter:  ").lower()
if letter in ['a', 'e','i','o','u']:
    print('Vowels')
else:
    print("Not A Vowels")

print("      <====================================================================>")


# Q8   Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

print(" Q-8 Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. ")
print("      <====================================================================>")

a= int(input("Enter First NUmber"))
b= int(input("Enter Second NUmber"))
c= int(input("Enter Third NUmber"))

if a == b or b == c or a == c:
    print("Sum is 0")
else:
    print("Sum is", a + b + c)

print("      <====================================================================>")

# Q9 => Q-9 Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

print(" Q-9   Write a Python program to sum of three given integers. However, if two values are equal sum will be zero ")


letter = input (" Enter a letter:  ").lower()
if letter in ['a', 'e','i','o','u']:
    print('Vowels')
else:
    print("Not A Vowels")

print("      <====================================================================>")


# Q-10  Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

print("Q-10  Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. ")
print("      <====================================================================>")

def check_condition(a,b):
    return a == b or abs(a -b) == 5 or a + b ==5

num1 = int(input("Enter First NUmber: "))
num2 = int(input("Enter Second NUmber: "))

print(check_condition(num1,num2))

# Q-11 Write a python program to sum of the first n positive integers.

print("Q-11 =>  Write a python program to sum of the first n positive integers. ")

print("      <====================================================================>")

n = int(input("Enter a Positive Integer: => : "))

sum_of_integer = n * (n + 1 ) // 2

print(f"Sum of The First {n} Positive integer is {sum_of_integer}")

# Q-12  Write a Python program to calculate the length of a string.

print("Q-12 =>  Write a Python program to calculate the length of a string. ")

print("      <====================================================================>")

string = input("Enter a string: ")
length = len(string)
print(f"Length of the string is {length}")


# Q-13  Write a Python program to count the number of characters (character frequency) in a string


print (" Q-13 Write a Python program to count the number of characters (character frequency) in a string  ")

print("      <====================================================================>")

string = input (" Enter A String")
char_freq = {}
for char in string:
    char_freq[char]= char_freq.get(char,0) + 1

print("Character Frequency", char_freq)


# Q-14 What are negative indexes and why are they used?

'''
Negative indexes in Python are used to access elements from the end of a sequence (list, tuple, string). `-1` represents the last element, -2 the second-to-last, and so on.
'''

# Q-15  Write a Python program to count occurrences of a substring in a string.

print(" Q-15 Write a Python program to count occurrences of a substring in a string.")

print("      <====================================================================>")

main_string = input("Enyter The Main String: => :")
sub_string = input("Enyter The SubString: => :")
count = main_string.count(sub_string)

print("      <====================================================================>")

print(f"Substring {sub_string} occurs {count} times In The Main String")