# Q1 => WIRTE A PYTHON PROGRAM TO CHECK IF A NUMBER IS POSITIVE,NEGATIVE OR ZERO.

print("Q1 => WIRTE A PYTHON PROGRAM TO CHECK IF A NUMBER IS POSITIVE,NEGATIVE OR ZERO.")
print("<====================================================================>")

num  = float(input('  Q-1 Enter a number : '))
if num > 0:
    print("Number positive")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")



print("<====================================================================>")

'''
<====================================================================>
'''
# Q2=> WRITE A PYTHON PROGRAM TO GET THE FACTORAL NUMBER OF GIVEN NUMBER


print("Q2=> WRITE A PYTHON PROGRAM TO GET THE FACTORAL NUMBER OF GIVEN NUMBER : ")
print("<====================================================================>")

def factrol(n):
    if n == 0 or n ==1:
        return 1
    else :
        return n *factrol(n-1)

num = int(input("Enter a Number"))
print(f"   Factrol of {num}is {factrol(num)}")


print("<====================================================================>")

'''
<====================================================================>

'''

# Q3 => Write a Python program to get the Fibonacci series of given range.


print("Q3 => Write a Python program to get the Fibonacci series of given range : ")

print("<====================================================================>")

def fibo(n):
    fib_series = [0,1]
    while len(fib_series) <n :
        fib_series.append(fib_series[-1]+fib_series[-2])
    return fib_series

n = int(input("Enter The Range for Fibonacci Series"))
print(f"Fibonacci series{fibo(n)}")

print("<====================================================================> /n")


'''
<====================================================================>

'''
print("<====================================================================>")

'''

Q-4 => How Memory is managed in python
Ans =>  Python uses automatic memory management . The core is managed by a private heap space ,
and the interpreter takes care of memory allocation and deallocation.

Q-5 =>  What is the purpose continue statement in python?
The continue statement is used to skip the rest of the code
inside a loop for the current iteration and move to the next iteration...

'''
print("<====================================================================>")

'''
<====================================================================>
'''
# Q6  Write python program that swap two number with temp variable and without temp variable.


print (" Q6  Write python program that swap two number with temp variable and without temp variable : ")

print("<====================================================================>")
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

print("<====================================================================>")

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


