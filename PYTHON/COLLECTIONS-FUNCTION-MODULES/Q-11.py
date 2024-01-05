#Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

def get_unique_elements(input_list):
    return list(set(input_list)) #set from a input list

# Take input as a string and convert it to a list
original_input = input("Enter Values separated by spaces: ")
original_list = original_input.split()   # split it by default in the list values 

unique_elements = get_unique_elements(original_list)
print("List with Unique Elements: ", unique_elements)
