# Write a python program to remove duplicate from list


def remove_duplicates(list_input):
 return list(set(list_input))

# List jo input me leni he

list_to_inputed = [1,2,3,1,2,4,4,5,5]
unipue = remove_duplicates(list_to_inputed)
print("Inputed List",list_to_inputed)
print("List After Removing Duplicates",unipue)