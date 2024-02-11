
# Write a Python program to copy the contents of a file to another file.


list_1 = [1, 2, 3, 4, 5]

with open('file.txt', 'w') as file:
    for i in list_1:
        file.write(str(i) + '\n')