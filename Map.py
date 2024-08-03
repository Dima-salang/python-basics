# the map function returns a map obj which is an iterator of the results after applying the given function to each
# item of a given iterable.
# Map is used if you want to call a function to every element of a list
# You can also just use list comprehensions


numbers = [2, 4, 5, 6]


def add_nums(num):
    return num + num


print(list(map(add_nums, numbers)))
print(list(map(lambda x: x + x, numbers)))  # one-liner
print(list(map(str, numbers)))

print([add_nums(num) for num in numbers]) # you can just use list comprehension
