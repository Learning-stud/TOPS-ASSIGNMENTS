to_store = []

with open('file.txt','r') as file:
 for line in file:
  to_store.append(line.strip())

print(to_store)