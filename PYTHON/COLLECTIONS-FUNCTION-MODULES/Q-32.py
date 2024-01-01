#  Write a Python script to check if a given key already exists in a
# dictionary
my_dict = {'a': 'abhishek', 'b':'bhavesh','c':'charmi','d':'david'}

# function to check if  a key exists in the dictionary
def key_exists(dictionary,key_to_check):
 return key_to_check in dictionary


# key to check
key_to_check = 'c'

if(key_exists,my_dict):
 print(f"The Key '{key_to_check}', Exists In The Dictionary .Its Value Is : {my_dict[key_to_check]}")
else:
 print(f"The Key '{key_to_check}' Does Not Exists In The Dictionary")

