# Write a Python program to check whether a list contains a sub list


def is_sublist(lst,sub_list):
 return all(x in lst for x in sub_list)

my_list = [1,2,3,[1,2,3,],4,5]
sub_list = [1,2,3]
print(is_sublist(my_list,sub_list))
