# Write a python program to remove duplicate from list

# remove _duplcate Function converts the list to set and then back to list
def remove_duplicates(list_input):
 return list(set(list_input))  # set is used to remove duplcate values

list_to_inputed = [1,2,3,1,2,4,4,5,5]
unipue = remove_duplicates(list_to_inputed)
print("Inputed List",list_to_inputed)
print("List After Removing Duplicates",unipue)