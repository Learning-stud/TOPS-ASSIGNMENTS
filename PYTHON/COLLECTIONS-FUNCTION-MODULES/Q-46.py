# Write a Python function to check whether a number is in a given range

def is_in_range(number, lower, upper):
    """Check if number is in the given range."""
    return lower <= number <= upper

result = is_in_range(10, 5, 15)
print("Is 10 in the range [5, 15]?", result)
