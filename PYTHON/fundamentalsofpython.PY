# Q1 => WIRTE A PYTHON PROGRAM TO CHECK IF A NUMBER IS POSITIVE,NEGATIVE OR ZERO.

print(" Q1 => WIRTE A PYTHON PROGRAM TO CHECK IF A NUMBER IS POSITIVE,NEGATIVE OR ZERO. ")
print("      <====================================================================>")

# The above code is taking user input for a number and then checking if the number is positive, zero, or negative. It then prints the corresponding message based on the condition.

num = float(input('Enter a number: '))
result = "Positive" if num > 0 else "Zero" if num == 0 else "Negative"
print(result)




print("      <====================================================================>")

'''
<====================================================================>
'''
# Q2=> WRITE A PYTHON PROGRAM TO GET THE FACTORAL NUMBER OF GIVEN NUMBER


print("Q2=> WRITE A PYTHON PROGRAM TO GET THE FACTORAL NUMBER OF GIVEN NUMBER : ")
print("      <====================================================================>")

# The above code is calculating the factorial of a given number. It defines a function called "factrol" that takes an integer parameter "n". If the value of "n" is 0 or 1, the function returns 1. Otherwise, it recursively calls itself with the parameter "n-1" and multiplies the result with "n".

def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")



print("      <====================================================================>")

'''
<====================================================================>

'''

# Q3 => Write a Python program to get the Fibonacci series of given range.


print("Q3 => Write a Python program to get the Fibonacci series of given range : ")

print("      <====================================================================>")

# The above code is generating a Fibonacci series up to a given range. It takes an input from the user for the range of the Fibonacci series and then uses a while loop to generate the series. The series is stored in a list called "fib_series" and starts with the values 0 and 1. The loop continues until the length of the series is less than the given range. In each iteration, the next number in the series is calculated by adding the last two numbers in the series. Finally, the generated Fibonacci series is printed.

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

range_limit = int(input("Enter the range for Fibonacci series: "))
print(f"Fibonacci series: {fibonacci(range_limit)}")


print("      <====================================================================> ")


'''
<====================================================================>

'''
print("      <====================================================================>")

'''

Q-4 => How Memory is managed in python
Ans =>  Python uses automatic memory management . The core is managed by a private heap space ,
and the interpreter takes care of memory allocation and deallocation.

Q-5 => What is the purpose continue statement in python?

ANS => The continue statement is used to skip the rest of the code
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

# The above code is swapping the values of variables a and b. It is using a temporary variable "temp" to store the value of a before swapping. Then, it assigns the value of b to a and the value of temp (which is the original value of a) to b.

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

# The above code is taking an input from the user and checking if the number is even or odd. If the number is divisible by 2 without any remainder, it is considered an even number and the code will print "Even Number". Otherwise, it is considered an odd number and the code will print "Odd Number".

num = int(input("Enter a number: "))
result = "Even" if num % 2 == 0 else "Odd"
print(result)


# Q-7  Write a Python program to test whether a passed letter is a vowel or not.

print(" Q-7  Write a Python program to test whether a passed letter is a vowel or not : => :   ")


# The above code is asking the user to enter a letter and then checks if the entered letter is a vowel (a, e, i, o, u). If the letter is a vowel, it prints "Vowels". Otherwise, it prints "Not A Vowels".

letter = input("Enter a letter: ").lower()
result = "Vowel" if letter in ['a', 'e', 'i', 'o', 'u'] else "Not a Vowel"
print(result)


print("      <====================================================================>")


# Q8   Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

print(" Q-8 Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. ")
print("      <====================================================================>")

# The above code prompts the user to enter three numbers. It then checks if any two of the numbers are equal. If any two numbers are equal, it prints "Sum is 0". Otherwise, it calculates the sum of the three numbers and prints "Sum is" followed by the sum.


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

def sum_of_three_integers(a, b, c):
    if a == b or b == c or a == c:
        return 0
    else:
        return a + b + c

num1, num2, num3 = 3, 3, 6
result = sum_of_three_integers(num1, num2, num3)
print(f"The sum of three integers is: {result}")





print("      <====================================================================>")


# Q-10  Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

print("Q-10  Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. ")
print("      <====================================================================>")

# The above code defines a function called "check_condition" that takes two parameters, "a" and "b". The function checks three conditions:
# 1. If "a" is equal to "b"
# 2. If the absolute difference between "a" and "b" is equal to 5
# 3. If the sum of "a" and "b" is equal to 5

def check_condition(a,b):
    return a == b or abs(a - b) == 5 or  a + b == 5
    num1,num2 = 3,2
    print(check_condition(num1,num2))

# Q-11 Write a python program to sum of the first n positive integers.

print("Q-11 =>  Write a python program to sum of the first n positive integers. ")

print("      <====================================================================>")

# The above code is calculating the sum of the first n positive integers. It prompts the user to enter a positive integer, then calculates the sum using the formula n * (n + 1) // 2. Finally, it prints the sum of the first n positive integers.

n = 5
sum_of_integer = n * (n + 1) // 2
print(f"Sum of the first {n} positive integers is {sum_of_integer}")


# Q-12  Write a Python program to calculate the length of a string.

print("Q-12 =>  Write a Python program to calculate the length of a string. ")

print("      <====================================================================>")

# The above code prompts the user to enter a string, then calculates the length of the string using the len() function. Finally, it prints the length of the string.
user_string = "Hello, World!"
length = len(user_string)
print(f"Length of the string is {length}")



# Q-13  Write a Python program to count the number of characters (character frequency) in a string


print (" Q-13 Write a Python program to count the number of characters (character frequency) in a string  ")

print("      <====================================================================>")

# The above code is calculating the frequency of each character in a given string. It prompts the user to enter a string, and then it iterates through each character in the string. For each character, it checks if it already exists in the char_freq dictionary. If it does, it increments the frequency count by 1. If it doesn't, it adds the character to the dictionary with a frequency count of 1. Finally, it prints the character frequency dictionary.

user_string = "programming"
char_frequency = {char: user_string.count(char) for char in set(user_string)}
print("Character frequency:", char_frequency)



print("      <====================================================================>")

# Q-14 What are negative indexes and why are they used?

'''
Negative indexes in Python are used to access elements from the end of a sequence (list, tuple, string). `-1` represents the last element, -2 the second-to-last, and so on.

my_list = [1, 2, 3, 4, 5]
last_element = my_list[-1]  # Access the last element
second_last_element = my_list[-2]  # Access the second-to-last element

'''

# Q-15  Write a Python program to count occurrences of a substring in a string.

print(" Q-15 Write a Python program to count occurrences of a substring in a string.")

print("      <====================================================================>")

# The above code is asking the user to input a main string and a sub string. It then counts the number of occurrences of the sub string within the main string and stores the count in the variable "count".

main_str = "Hello, hello, hello, how low?"
sub_str = "hello"
occurrences = main_str.lower().count(sub_str.lower())
print(f"The substring '{sub_str}' appears {occurrences} times in the main string.")


print("      <====================================================================>")




# Q-16 => Write a Python program to count the occurrences of each word in a given sentence


'''
The word frequency effect is a psychological phenomenon where recognition times are faster for words seen more frequently than for words seen less frequently. Word frequency depends on individual awareness of the tested language.

'''
print("Q-16 => Write a Python program to count the occurrences of each word in a given sentence ")

print("      <====================================================================>")



# The above code is counting the frequency of each word in a given sentence. It splits the sentence into individual words, creates a dictionary called `word_count`, and then iterates through each word. For each word, it checks if it already exists in the `word_count` dictionary. If it does, it increments the count by 1. If it doesn't, it adds the word to the dictionary with a count of 1. Finally, it prints the word frequency dictionary.

user_sentence = "How are You , How Is your Day going ?"
words = user_sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print("Word frequency:", word_count)


print("      <====================================================================>")


# Q-17 =>  Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

print("Q-17  Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string : => : ")

print("      <====================================================================>")

# The above code takes two strings as input from the user and then creates a new string by combining parts of the two input strings. It takes the first two characters from the second string and combines it with the remaining characters from the first string. It also takes the first two characters from the first string and combines it with the remaining characters from the second string. The new string is then printed as the result.

str1 = "hello"
str2 = "world"
new_str = str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
print("Combined string with swapped characters:", new_str)


print("      <====================================================================>")


# Q-18 =>  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

print ("Q-18 =>  Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.")

print("      <====================================================================>")
# The above code takes a string as input from the user and checks if the length of the string is greater than or equal to 3. If it is, it checks if the last three characters of the string are 'ing'. If they are, it appends 'ly' to the string. If they are not, it appends 'ing' to the string. Finally, it prints the resulting string.

def ing_to_string(s):
    if len(s) >= 3:
        return s + "ing"
    else:
        return s

user_str = "play"
modified_str = ing_to_string(user_str)
print("Modified string:", modified_str)




print("      <====================================================================>")

# Q-19 =>  Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor',replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.


print("Q-19 =>  Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor',replace the whole 'not'...'poor' substring with 'good'. Return the resulting string: => : ")


print("      <====================================================================>")

# The above code takes a string as input from the user. It then checks if the string contains the word 'not' followed by the word 'poor'. If this condition is met, it replaces the substring 'not' to 'good' and removes the substring 'poor' from the original string. Finally, it prints the modified string or the original string if the condition is not met.

# Function definition: 'replace_substring' naam ka ek function define kiya gaya hai
def replace_substring(main_str):   # defining a function
    not_index = main_str.find("not")
    poor_index = main_str.find("poor")




# aa line check kare 6e k "not" ane "poor" bannev string main_string ma 6e ane "not" "poor" ni pehla aave 6e.agar aa condition satisfy thai,to main_str string ma "not" thi pehla no hisso , "good" ame "poor" na pachina hissa maline,puri "not " "poor" substring ne "good"thi replace kare 6e.

    if not_index != -1 and poor_index != -1 and not_index < poor_index:
        main_str = main_str[:not_index] + "good" + main_str[poor_index + 4:]


user_str = "The weather is not that poor today."

result_str = replace_substring(user_str)

print("Resulting string:", result_str)



print("      <====================================================================>")

# Q-20 =>  Write a Python function that takes a list of words and returns the length of the longest one.


print("Q-20 =>  Write a Python function that takes a list of words and returns the length of the longest one: => :  ")

print("      <====================================================================>")

# The above code defines a function called `long_word_length` that takes a list of words as input. It then uses a generator expression to find the length of each word in the list and returns the maximum length.

# The above code defines a function called `longest_word_length` that takes a list of words as input. It uses a generator expression to iterate over each word in the list and calculates the length of each word. The `max` function is then used to find the maximum length among all the words in the list. The function returns this maximum length.

def longest_word_length(word_list):
    return max(len(word) for word in word_list)

# The above code is defining a list of words called "words_list" and then printing the length of the longest word in that list.

words_list = ["apple", "banana", "cherry", "date"]
print("Length of the longest word:", longest_word_length(words_list))


print("      <====================================================================>")


# Q-21 =>  Write a Python function to reverses a string if its length is a multiple of 4.

print(" Q-21 =>   Write a Python function to reverses a string if its length is a multiple of 4 : => :")

print("      <====================================================================>")

# The above code defines a function called `reverse_string_multiply_of_4` that takes an input string as a parameter. It checks if the length of the input string is divisible by 4. If it is, it returns the reverse of the input string using slicing. If it is not divisible by 4, it returns the input string as is.

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

# The above code defines a function called `string_in_middle` that takes two parameters: `main_string` and `inserted_string`.

def string_in_middle(main_string,inserted_string):
    middle_index = len(main_string) // 2
    return main_string[:middle_index] + inserted_string + main_string[middle_index]


main_string = input("Enter the Main String : => : ")
inserted_string = input("Enter The String To Insert: => : ")

print("Result : => : ", string_in_middle(main_string,inserted_string))


print("      <====================================================================>")

