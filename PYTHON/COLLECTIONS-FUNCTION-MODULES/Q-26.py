# replace last value of tuple in a list
list_of_tuples = [(1, 2), (3, 4), (5, 6)]
new_value = 10
modified_list = [t[:-1] + (new_value,) for t in list_of_tuples]
print(modified_list)