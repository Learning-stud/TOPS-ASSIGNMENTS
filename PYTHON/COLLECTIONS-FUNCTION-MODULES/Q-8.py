# Write a python program to check a list is empty or not

def list_empty(input_list):
 return not bool(input_list)


empty_list=[]
not_empty = [1,2,3]
print("List Empty",list_empty(empty_list))
print("List Empty",list_empty(not_empty))