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


print("      <====================================================================>")

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


# Q-16 => Write a Python program to count the occurrences of each word in a given sentence


'''
The word frequency effect is a psychological phenomenon where recognition times are faster for words seen more frequently than for words seen less frequently. Word frequency depends on individual awareness of the tested language.

'''
print("Q-16 => Write a Python program to count the occurrences of each word in a given sentence ")

print("      <====================================================================>")

sentence = input("Enter Sentence")
words = sentence.split()

word_frequency = {}
for word in words:
    word_frequency[word]= word_frequency.get(word,0) + 1

print("Word Frequency",word_frequency)

print("      <====================================================================>")


# Q-17 =>  Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

print("Q-17  Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string : => : ")

print("      <====================================================================>")

str1 = input( " Enter The First String : => :  ")
str2 = input( " Enter The Second String : => :  ")

new_string = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]

print(" Result: => : ",new_string)

print("      <====================================================================>")


# Q-18 =>  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

print ("Q-18 =>  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.")

print("      <====================================================================>")
given_string = input("Enter a String")

if len(given_string) >= 3:
    if given_string[-3]  == 'ing':
        given_string += 'ly'

    else:
        given_string += 'ing'

print("Result: => : ",given_string)


print("      <====================================================================>")

# Q-19 =>  Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor',replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.


print("Q-19 =>  Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor',replace the whole 'not'...'poor' substring with 'good'. Return the resulting string: => : ")


print("      <====================================================================>")

input_string = input("Enter a String; => : ")

not_index=input_string.find('not')
poor_index=input_string.find('poor')

if not_index != -1 and poor_index != -1 and not_index < poor_index:
    result_string = input_string[:not_index] + ' good' + input_string[poor_index + 4]
else:
    result_string= input_string

print("Result : => : ",result_string)


print("      <====================================================================>")

# Q-20 =>  Write a Python function that takes a list of words and returns the length of the longest one.


print("Q-20 =>  Write a Python function that takes a list of words and returns the length of the longest one: => :  ")

print("      <====================================================================>")

def long_word_length(word_list):
    return max(len(word) for word in word_list)

word = input("Enter a List of Word : => : ").split(',')
print("Length Of The Longest Word: => : ",long_word_length(word))


print("      <====================================================================>")


# Q-21 =>  Write a Python function to reverses a string if its length is a multiple of 4.

print(" Q-21 =>   Write a Python function to reverses a string if its length is a multiple of 4 : => :")

print("      <====================================================================>")

# The above code defines a function called `reverse_string_multiply_of_4` that takes an input string as a parameter. It checks if the length of the input string is divisible by 4. If it is, it returns the reverse of the input string using slicing. If it is not divisible by 4, it returns the input string as is.

def reverse_string_multiply_of_4(input_string):
    if len(input_string) % 4 == 0:
        return input_string[:: -1]
    else:
        return input_string

string_to_reverse= input("Enter A String : => : ")
print("Result : => : ", reverse_string_multiply_of_4(string_to_reverse) )

print("      <====================================================================>")


# Q-22 =>  Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.


print(" Q-22 : => :  Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2,return instead of the empty string. ")

print("      <====================================================================>")

# The above code prompts the user to enter a string. If the length of the string is less than 2, it assigns the value "String is Empty" to the variable `string_result`. Otherwise, it takes the first two characters of the string (`strings[:2]`) and concatenates them with the last two characters of the string (`strings[-2:]`). The resulting string is then assigned to the variable `string_result`. Finally, it prints the value of `string_result`.

strings = input(" Enter a String : => : ")

if len(strings) < 2:
    string_result =  ("String is Empty")
else:
    string_result = strings[:2] + strings[-2:]

print("Result : => : ",string_result)

print("      <====================================================================>")


# Q-23 => Write a Python function to insert a string in the middle of a string.

print("Q-23 => Write a Python function to insert a string in the middle of a string : => : ")

print("      <====================================================================>")

def string_in_middle(main_string,inserted_string):
    middle_index = len(main_string) // 2
    return main_string[:middle_index] + inserted_string + main_string[middle_index]


main_string = input("Enter the Main String : => : ")
inserted_string = input("Enter The String To Insert: => : ")

print("Result : => : ", string_in_middle(main_string,inserted_string))


print("      <====================================================================>")

