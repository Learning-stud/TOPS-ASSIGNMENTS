# Write a Python program to convert a list of characters into a string.


def list_to_string(char_list):
    result_string = ""    #  initializing empty string
    for character in char_list:  # each charcter is added to the result string
        result_string += character #  Each character is append to the result_string in each itration
    return result_string

list_of_character = ['j', 'a', 'y']  # list of character
result_string = list_to_string(list_of_character) # calling the function to convert the list of character to a string

print("List Of Character: ", list_of_character)  # print the orignal list of character
print("Converted String : ", result_string)# print the converted string 
