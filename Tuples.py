import sys
import timeit

#  tuples is a collection that contains a number of values separated by commas and enclosed within parenthesis.
#  It is also ordered, immutable, and allows duplicates


tuple_sequence = 1, 2, 3, 4, 5
print(tuple_sequence)

#  tuples are also immutable unlike lists meaning it cannot be changed but it can contain mutable objects like a list.
tuple_sequence2 = ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
tuple_sequence2[0][0] = 11
print(tuple_sequence2)

#  tuples may also be nested
tuple_sequence3 = tuple_sequence, (6, 7, 8, 9, 10)
print(tuple_sequence3)

#  tuples with one item needs to have a comma after it. One element-tuples are their data types.
one_item_tuple = ("hello",)
print(one_item_tuple)

# looping through a tuple
for element in tuple_sequence:
    print(element)

#  to change an item inside tuple, convert to a list, change an item, and then convert to a tuple.
list_tuple = list(tuple_sequence)
list_tuple[0] = "hello"
print(tuple(list_tuple))

# unpacking tuples
another_tuple = ("Luis", 19, "Philippines")
name, age, country = another_tuple
print(name)
print(age)
print(country)

# tuples vs lists
another_tuple2 = ("Hello", 19, 20, 21, True)
another_list = ["Hello", 19, 20, 21, True]
print(sys.getsizeof(another_tuple2), "bytes")
print(sys.getsizeof(another_list), "bytes")  # bytes are larger

# timing tuples and lists
print(timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000))  # tuples are faster to create



