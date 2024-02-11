# WHAT IS FILE FUNCTION IN PYTHON ?
# WHAT IS THE KEYWORD TO VCREATE AND WRITE FILE


"""
ANSWER

OPEN() FUNCTION IS USED TO WORK WITH FILES IN PYTHON

"""

file = open('file.txt', 'w')
file.write("Hello How R U")

# another way to do it

with open('file.txt','w') as file:
 file.write("Hello how R   ")