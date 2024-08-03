# dict subclass for counting hashable objs
# It is a collection where elements are stored as dictionary keys and their counts are stored as dict values
from collections import Counter

string = "aaaabbbbccccc"
my_counter = Counter(string)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))
print(list(my_counter.elements()))
print(my_counter.total())
print(my_counter.items())