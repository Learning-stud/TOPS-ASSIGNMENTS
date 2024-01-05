
# create and display all combination of letterrs

# create and display all combination of letters
combinations = {'1': ['j', 'a', 'y'], '2': ['d', 'e', 'v', 'a', 'n', 's', 'h', 'u']}

# nested loops to generate all combinations
combinations_add = []   # for storing the value 
for char1 in combinations['1']: # loop for first value
    for char2 in combinations['2']: # loop for second value
        combinations_add.append(char1 + char2) # using append to add the value  and after the vlue will be added then concetination of every posible combination

print("All Combinations of Letters:", combinations_add)

