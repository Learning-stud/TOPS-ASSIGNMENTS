#Q-2 how to remove last object from list

lists = ["jay ","abhishek" ,"devanshu","nehru","ganddhi"]

#  by given the index number of the object we can remove the object from list and if we want to remove the whole object in list we have to just use inbuilt pop function

lists.pop(4)
print(lists)

list2 = [2,33,222,14,25]

list2.pop(-2)

# the output will be 2,33,222,25 & the number which will be popout will be 44!
print(list2)