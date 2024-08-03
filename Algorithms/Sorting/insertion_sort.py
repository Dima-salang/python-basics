# insertion sort is quadratic time for worst case = O(N^2)
# efficient for small input sizes... Best case = Linear
# Also good for partially sorted arrays; it is adaptive = Linear time complexity


def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key
    return array


orig_array = [10, 3, 2, 6, 1, 11, 5, 4]
new_array = insertion_sort(orig_array)
print(new_array)


