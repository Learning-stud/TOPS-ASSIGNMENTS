# • Write a Python program to append text to a file and display the text

with open('file.txt', 'a') as file:
    file.write('\n Next line : TEXT')

with open('file.txt', 'r') as file:
    data = file.read()
    print(data)