# • Write a Python program to read a file line by line store it into a variable.

data = ''

with open('file.txt', 'r') as file:
    for line in file:
        data += line

print(data)