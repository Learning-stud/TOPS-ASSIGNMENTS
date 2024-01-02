# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are the same from a given list of strings.

def count_strings(strings):
 count= 0
 for counts in strings:
  if len(counts) >= 2 and counts[0]== counts [-1]:
     counts += 1
  return count


counted_strings = ["Level","Hello","Devanshu","tirth","Abhishek"]
result_counts = count_strings(counted_strings)

print(f"Nu,ber Of Strings With The  Same First And Last Characte: {result_counts}")