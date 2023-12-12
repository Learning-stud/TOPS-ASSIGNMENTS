# write a function to find smallest ,largest and sum of all from the list
# The code `num = []` initializes an empty list called `num`.
num = []
for i in range(10):
 # The code `num_to_take = int(input("Enter the Number: => :"))` is taking user input and converting
 # it to an integer. It prompts the user to enter a number and assigns that number to the variable
# `num_to_take`.
 num_to_take = int(input("Enter the Number: => :"))
 num.append(num_to_take)

# The code `num.sort()` is sorting the list `num` in ascending order.

num.sort()
smallest = num[0]
largest = num[-1]
print("Sorted List :  ", num)
print("Smallest Number :  ", smallest)
print("largest Number :  ", largest)
