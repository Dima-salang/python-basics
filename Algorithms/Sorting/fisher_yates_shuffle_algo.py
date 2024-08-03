from random import randint

# Fisher-Yates shuffling algorithm aka Knuth Sort
# This algorithm produces a uniformly random permutation of the input array in linear time
# This is good to randomize a given array or shuffle a deck of cards.
# in iteration i, pick an integer r between 0 and i uniformly at random
# Swap arr[i] and arr[r]


def fisher_yates_shuffle(arr):
    for i in range(0, len(arr)):
        j = randint(0, i + 1)
        arr[j], arr[i] = arr[i], arr[j]
    return arr


arr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_arr = fisher_yates_shuffle(arr_list)
print(new_arr)




