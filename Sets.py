import timeit
#  a set is an unordered collection with no duplicate elements. It includes membership testing and
#  eliminating duplicate entries.
list_sequence = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
set_sequence2 = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5}
set_sequence = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5}
print(set_sequence)  # removes duplicates
print(set(list_sequence))  # set function to convert to a set
print(set_sequence.issubset(set_sequence2))  # if the set sequence contains the elements of another set
print(set_sequence.issuperset(set_sequence2))  # if the set sequence contains all the elements of another set
print(set_sequence.isdisjoint(set_sequence2))  # returns True if the two sets have a null intersection

#  membership operators
print(1 in set_sequence)  # fast membership testing
print(6 not in set_sequence)

#  set operations on unique letters... does not affect the original set
string_set_sequenceA = set("hello")
string_set_sequenceB = set("world")
a_union = string_set_sequenceA.union(string_set_sequenceB)  # combines both set without duplicates
print(a_union)
an_intersection = string_set_sequenceA.intersection(string_set_sequenceB)  # gives similar values in both sets
print(an_intersection)
print(string_set_sequenceA)  # unique letters in a
the_difference = string_set_sequenceA.difference(string_set_sequenceB)
print(the_difference)  # unique letters in a but not in b
print(string_set_sequenceA - string_set_sequenceB)  # unique letters in a but not in b
print(string_set_sequenceA & string_set_sequenceB)  # unique letters in both a and b
symmetric_difference = string_set_sequenceA.symmetric_difference(string_set_sequenceB)
print(symmetric_difference)  # prints unique letters in both a and b but not similar values present in both of them

#  affects the original set
print("affecting original set")
string_set_sequenceA.update(string_set_sequenceB)  # union
print(string_set_sequenceA)
string_set_sequenceA.intersection_update(string_set_sequenceB)  # intersection
string_set_sequenceA.difference_update(string_set_sequenceB)  # difference
string_set_sequenceA.symmetric_difference_update(string_set_sequenceB)  # symmetric difference


my_set = {1, 2, 3, 4, 5}
my_set.add(6)  # appends
my_set.discard(1)  # removes the element 1
my_set.clear()  # clears the set
print(my_set)
my_frozenset = frozenset([1, 2, 3, 4, 5])  # immutable
print(my_frozenset)



