# function to calculate factoral of a number (non-negative number)0

def factoral(numbers):
 result = 1
 for number in range(1,numbers+1):
  result *= number
  return result

 num = int(input("Enter Factorsl Num: "))
 print("Factoral : ",factoral(num))