#  find  repeated items of a tuple

my_tuple = (1,2,2,3,4,4,5,6,6)
duplicate = set(repeat for repeat in my_tuple if my_tuple.count(repeat) > 1 )
print(duplicate)
