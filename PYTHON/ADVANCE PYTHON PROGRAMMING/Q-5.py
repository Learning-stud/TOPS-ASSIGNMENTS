#  • Write a Python program to read last n lines of a file.

numbers = int(input("Enter how many lines do you want (only numbers)? : "))

with open('file.txt', 'r') as file:
    lines = file.readlines()[-numbers:]
    for line in lines:
        print(line.strip())  # strip() is used to remove the newline character at the end of each line