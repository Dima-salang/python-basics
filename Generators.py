# a simple way of creating iterators.
# A generator is a function that returns an object(iterator) which we can iterate over(one value at a time)

def add_nums(a_list):
    for i in a_list:
        yield i + i  # pauses the function saving all its states and later continues on successive calls
        #  this saves a lot on memory than using lists


print(next(add_nums([1, 2, 3, 4, 5])))
my_nums = (x+x for x in [1, 2, 3, 4, 5])  # a generator object with list comprehension. Instead of square brackets.
for num in my_nums:
    print(num)

