 # Write a Python program to read first n lines of a file.

numbers = int(input("Enter The lines do u want (only numbers) ? : "))

with open('file.txt', 'r') as file:
    print(file.readlines()[:numbers])