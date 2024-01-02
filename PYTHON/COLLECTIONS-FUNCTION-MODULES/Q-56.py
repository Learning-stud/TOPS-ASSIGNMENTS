import random

#  Write a Python program to read a random line from a file

file=open("fQ-56.txt","r")
line=file.readlines()

random_line=random.choice(line).strip() # strip for removing whitespaces

print("Radom Line :",random_line)