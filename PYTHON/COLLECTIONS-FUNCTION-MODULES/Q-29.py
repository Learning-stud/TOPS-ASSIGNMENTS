# unzip a list of tuples into individuals lists:
list_of_tuples = [(1,'a'),(45,'e'),(58,'f')]
unzipped = list(zip(*list_of_tuples))
print(unzipped)