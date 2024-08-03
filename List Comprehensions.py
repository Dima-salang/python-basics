import math

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing
# list.
# The Syntax: newlist = [expression for item in iterable if condition == True]

my_list = ["apple", "banana", "orange"]
shorter_code = [item for item in my_list if item.startswith("a")]
print(shorter_code)

my_list2 = [2, 3, 4]
scalar_multiplication = [5 * x for x in my_list2]
print(scalar_multiplication)

my_list3 = [1, 4, 5, 6, 10, 54, 45, 32, 31, 9]
is_even = [num for num in my_list3 if num % 2 == 0]
print(is_even)






