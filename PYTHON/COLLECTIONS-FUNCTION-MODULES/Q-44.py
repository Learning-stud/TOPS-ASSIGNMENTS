#  create an dictionary from a string

string = 'Hello Majama Thik ho na vastu '

dictionary  = {}

for words in string:
 dictionary[words] = string.count(words)

 print(dictionary)