# print dictionary where the keys are numbers between 1 to 15.

# empty dictionary
my_dict = {}

# using for loop  because we have to apply range between 0 to 16

for numbers in range(1,16):
 my_dict[numbers] = numbers ** 2


print("Dictionary With Numbers Between 1 to 15 : ")
print(my_dict)
