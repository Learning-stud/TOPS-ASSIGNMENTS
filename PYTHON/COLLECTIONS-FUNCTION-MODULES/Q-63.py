#How will you create a dictionary using tuples in Python?
# Using tuples as key-value

print("--------------------------------------- ---------------Using dict() Constructor:---------")

tuple1 = ('a', 1)
tuple2 = ('b', 2)
tuple3 = ('c', 3)

# Creating a dictionary using dict() constructor
result_dict = dict([tuple1, tuple2, tuple3])

print("Dictionary from Tuples:", result_dict)


print("--------------------------------------- Dictionary Comprehension------------------------")

# Using tuples as key-value pairs
tuple_1 = ('a', 1)
tuple_2 = ('b', 2)
tuple_3 = ('c', 3)

# Creating a dictionary using dictionary comprehension
result_dict = {key: value for key, value in [tuple_1, tuple_2, tuple_3]}

print("Dictionary from Tuples:", result_dict)
