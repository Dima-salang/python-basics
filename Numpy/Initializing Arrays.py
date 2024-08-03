import numpy as np

# All 0s matrix
zeroes = np.zeros((3,10))
print(zeroes)

# all 1s matrix
ones = np.ones((4, 2, 2))
print(ones)

# any other number
full = np.full((3, 3), 100)
print(full)

# random decimal nums
dec = np.random.rand(2, 3)
print(dec)

# random int nums
integer = np.random.randint(5, 6, size=(2, 3))
print(integer)

# identity matrix
matrix = np.identity(4)
print(matrix)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1)
arr2 = np.array([
    [0, 1, 2],
    [3, 4, 5]
])
print(arr2)
arr2 = arr1.copy()
