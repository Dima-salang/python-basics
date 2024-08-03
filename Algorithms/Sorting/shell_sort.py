# mainly a variation or generalized insertion sort
# the idea is to reduce exchanges. Shell sort allows the exchange of far items
# by making the array h-sorted for a large value of h. We keep reducing the value of h
# until it becomes 1.

# the performance of shell sort depends on the type of sequence used for a given input size
# Best: O(n*log n)
# Worst: O(n^2)
# Average: O(n*log n)
# Space complexity O(1)
# Stability: No

def shell_sort(array, input_size):
    gap = input_size // 2
    while gap > 0:
        for i in range(gap, input_size):
            key = array[i]
            j = i
            while j >= gap and array[j - gap] > key:
                array[j] = array[j - gap]
                j -= gap
            array[j] = key
        gap //= 2
    return array


orig_array = [10, 3, 2, 6, 1, 11, 5, 4]
new_array = shell_sort(orig_array, len(orig_array))
print(new_array)



