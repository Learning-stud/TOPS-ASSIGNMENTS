# combine two dictionary adding values for common keys
from collections import Counter

d1 = {'a':'100','b':'200','c':'300'}
d2 ={'a':'300','d':'200','e':'400'}

combined = dict(Counter(d1)+Counter(d2))


print("Combined Dictionary",combined)