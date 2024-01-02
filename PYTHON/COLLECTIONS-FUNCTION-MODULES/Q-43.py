# combine values list of dictionary


list_of_dictionary = [
    {'item': 'mobile', 'amount': 10000},
    {'item': 'laptop', 'amount': 40000},
    {'item': 'computer', 'amount': 50000}
]

combined_dictionary = {} # dictionary to store combined values

for dictionary in list_of_dictionary:  # iterate through each dictionary in list
    combined_dictionary[dictionary['item']] = dictionary['amount'] # using 'item' key as the key and 'amount' as the value in the combined  dictionary
print("Combined Dictionary:", combined_dictionary)
