# the filter function returns an iterator where the items are filtered through a function to test if the item is
# accepted or not. If true or false. filter(function, iterable)
# you can also just use list comprehensions

numbers = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x % 2 == 0, numbers)))  # checks if a number is even or not.
print([num for num in numbers if num % 2 == 0])

