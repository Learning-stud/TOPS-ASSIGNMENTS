import random

# How can you pick a random item from a list or tuple?

my_list = [1, 2, 3, 4, 5]
random_item = random.choice(my_list)
print("Random Item from List:", random_item)


#  How can you pick a random item from a range?

random_from_range = random.randrange(1, 10)
print("Random Item from Range [1, 10):", random_from_range)

#  How can you get a random number in python?

random_number = random.random()
print("Random Number:", random_number)

#  How will you set the starting value in generating random numbers?

'''

randint() accepts two arguments

1st => First argument is for start of the range
2nd => Second argument is for end of the range
So you can specify the first argument to set the starting value

'''
print("Random Number :",random.randint(1,100)) # generates random number between 1 to 100

# Generating some random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]

print("Random Numbers:", random_numbers)


#  How will you randomizes the items of a list in place?

random_list = [1, 2, 3, 4, 5]
random.shuffle(random_list)   # using shuffle funcion  it will change the value like we shuffle cards
print("Randomized List:", random_list)


