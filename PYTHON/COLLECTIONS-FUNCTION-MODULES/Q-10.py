#Write a Python program to generate and print a list of the first and last 5 elements where the values are square of numbers between 1 and 30.

square = [ i ** 2 for i in range (1,31)]    # i ** 2  is used to find the cube root
print("The First Elemnts")
print(square[:5]) # [:5]   is used to print the values from positive index

print("The last Elements ")
print(square[-5:])  # [:-5 is used to print the values from negative index  {: this sign is used to reversed  }]