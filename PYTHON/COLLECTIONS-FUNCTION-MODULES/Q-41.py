
# create and display all combination of letterrs

# create and display all combination of letters
combinations = {'1': ['j', 'a', 'y'], '2': ['d', 'e', 'v', 'a', 'n', 's', 'h', 'u']}

# nested loops to generate all combinations
combinations_add = []
for char1 in combinations['1']:
    for char2 in combinations['2']:
        combinations_add.append(char1 + char2)

print("All Combinations of Letters:", combinations_add)

