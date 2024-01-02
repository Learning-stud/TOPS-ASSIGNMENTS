#  Python Function to Check Whether a String is Palindrome:

# palindrome means jo words piche se ya age se start karo padhneme same hi hota he

# the words we lokk and read from both side and when we read uit means same from both way 

def is_palindrome(string):
    """Check if the passed string is a palindrome."""
    return string == string[::-1]

result = is_palindrome("radar")
print("Is 'radar' a palindrome?", result)
