#  Sort a dictionary by value (ascending and descending)

my_dict = {'a': 100, 'b': 200, 'c': 50}
sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1])) # for ascending order
sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True)) # descending order 

print(sorted_dict_asc)
print(sorted_dict_desc)