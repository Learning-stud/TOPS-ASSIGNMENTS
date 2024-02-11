#• Write a Python program to write a list to a file.

list = [1, 2, 3, 4, 5]

with open('file.txt', 'w') as file:
    for i in list:
        file.write(str(i) + '\n')