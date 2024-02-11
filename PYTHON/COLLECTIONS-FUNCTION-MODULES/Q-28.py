# remove empty tuples from a list of tuples
lots_of_tuples = [(18,19),(),(5,6),(),(1,2),(),(15,45)]
non_empty_tuples = [tuples for tuples in lots_of_tuples if tuples]
print(non_empty_tuples)