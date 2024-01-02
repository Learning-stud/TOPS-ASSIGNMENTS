#Python Function to Check Whether a Number is Perfect:

def is_perfect_number(number):
    """Check if number is a perfect number."""
    divisors = [values for values in range(1, number) if number % values == 0]
    return sum(divisors) == number

result = is_perfect_number(28)
print("Is 28 a perfect number?", result)
