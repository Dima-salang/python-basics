import numpy as np
# the numbers you can represent by a given num of bits would be 2 ** n where n = bits
# 2 bits would only be able to represent 2 numbers: 0 and 1
# Why is Numpy arrays are faster than lists? *Fixed types - Faster to read less bytes of memory and no type checking when iterating
# , *Contiguous memory

# one-dimensional arrays
numpy_array = np.array([1, 2, 3])
print(numpy_array)
print(numpy_array[0])
# Get specific element - array[r, c]
print(numpy_array[[0, 1]])  # multi-indexing
print(numpy_array.reshape(3, 1))
# Iterating through arrays
for x in numpy_array:
    print(x)


# Array Types
another_array = np.array([1, 2.5, 3.14, 5])
print(another_array.dtype)  # float64
print(numpy_array.dtype)  # int32
an_array = np.array([1, 2], dtype=np.int8)
print(an_array.dtype)

# Dimensions and shapes
dimensional_array = np.array([
    [1, 2, 3],
    [3, 2, 1]
])
print(dimensional_array)
print(dimensional_array.shape)  # number of rows and columns
print(dimensional_array.size)  # total number of elements
print(dimensional_array.ndim)  # total number of dimensions
print(dimensional_array.nbytes)
# Get specific row
print(dimensional_array[0, :])
# Get specific column
print(dimensional_array[:, 0])
# reassign element
dimensional_array[0, 1] = 5
print(dimensional_array)
# iterating through 2-d arrays
for x in dimensional_array:
    for y in x:
        print(y)

three_dimensions = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
    ],
    [
        [7, 8, 9],
        [0, 1, 2]
    ]
])
print(three_dimensions)
print(three_dimensions[0, 0, 0])
print(three_dimensions.shape)
print(three_dimensions.size)
print(three_dimensions.ndim)
# flattening arrays
print(three_dimensions.reshape(-1))
# iterating through 3-d arrays
for x in three_dimensions:
    for y in x:
        for z in y:
            print(z)
# iterating with nditer
for x in np.nditer(three_dimensions):
    print(x)

# Joining arrays
arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr2 = np.array([
    [7, 8, 9],
    [11, 12, 13]
])

print(np.concatenate((arr1, arr2)))
print(np.concatenate((arr1, arr2), axis=1))

# splitting arrays
print(np.array_split(arr1, 3))

# searching arrays
print(np.where(arr1 == 1))
print(np.where(arr1 % 2 == 0))
print(np.searchsorted(arr1, 3))

# sorting arrays
print(np.sort(arr1))


