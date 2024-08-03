# sort by finding minimum and then swapping
# maintains two subarrays: sorted and unsorted
# time complexity = O(n^2) = quadratic time as you need to compare and exchange

def selection_sort(array, size):
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            # select min index in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swap elements
        (array[i], array[min_index]) = (array[min_index], array[i])


my_array = [6, 1, 3, 5, 9, 2, 1]
selection_sort(my_array, len(my_array))
print(my_array)

