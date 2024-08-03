numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0])
print(numbers[1])
print(numbers[4:])
print(numbers[-1])
print(numbers[::2])  # step 2
print(numbers[::-1])  # reverse list
# List concatenation

words = ["Hello", "Fish", "Cow", "Beef"]
print(numbers + words)

# Strings are immutable while Lists are mutable
words[0] = "Python"
print(words)
# Can also add elements inside a list using append()
words.append("Chicken")
print(words)

# len() for number of elements inside list.
print(len(words))


def sum_arr(array1):
    array1[3] = 39

array2 = [1, 2, 3, 4, 5]
sum_arr(array2)

print(array2)


