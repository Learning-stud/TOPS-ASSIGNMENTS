# write a function to find smallest ,largest and sum of all from the list
# The code `num = []` initializes an empty list called `num`.
num = []  # initializing
add = 0  # assigning  default value
for i in range(5):  # defining the range
# `num_to_take`.  
 num_to_take = int(input("Enter the Number: => :"))
 num.append(num_to_take)   # adding the element

# The code `num.sort()` is sorting the list `num` in ascending order.

num.sort()
smallest = num[0]  # First element
largest = num[-1] # Last Elements
add = smallest + largest  #
print("Sorted List :  ", num)
print("Smallest Number :  ", smallest)
print("largest Number :  ", largest)
print("Sum Of All Number :  ", add)
