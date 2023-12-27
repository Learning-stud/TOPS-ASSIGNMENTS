# Write a python function that takes two list and return true if they have at lest one common member
def common_member(list1,list2):
 return any(number
  in list2 for number
  in list1)
  # anyfunction check the values is true

list_a=[1,2,3,4]
list_b=[3,4,5,6]
print("List have Commo Menbers? ",common_member(list_a,list_b))
