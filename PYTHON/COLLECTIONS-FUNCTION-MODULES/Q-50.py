#Sum of All Divisors of a Number:
def sum_of_divisors(number):
    """Calculate the sum of all divisors of a number."""
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return sum(divisors)

result = sum_of_divisors(12)
print("Sum of Divisors of 12:", result)
