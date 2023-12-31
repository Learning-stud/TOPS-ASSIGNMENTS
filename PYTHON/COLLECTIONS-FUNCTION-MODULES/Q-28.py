# remove empty tuples from a loist of tuples
lost_of_tuples = [(18,19),(),(5,6),(),(1,2),(),(15,45)]
non_empty_tuples = [tuples for tuples in lost_of_tuples if tuples]
print(non_empty_tuples)