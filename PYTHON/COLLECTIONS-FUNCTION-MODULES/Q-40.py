#Why Do You Use the zip() Method in Python?

# the zip method is used to combine two or more iterable elements-wise


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

combined = list(zip(list1, list2))

print("Combined Result:", combined)
