from fisher_yates_shuffle_algo import fisher_yates_shuffle
# implementation of quick sort using Hoare's partition scheme
""" Basic plan : Shuffle the array
                 Partition so that, for some j:
                    entry arr[j] is in place
                    no larger entry to the left of j
                    no smaller entry to the right of j
                Sort each piece recursively"""
""" This function takes first element as pivot and places all
    elements smaller than the pivot to the left of the pivot
    and all elements greater than the pivot to the right of the pivot
    it returns the index of the last index on the smaller side."""


def partition(arr, low, high):  # key process for quicksort
    pivot = arr[low]
    i = low    # pointer for small side
    j = high    # pointer for greater side

    while True:
        while arr[i] < pivot:
            i += 1

        while arr[j] > pivot:
            j -= 1

        if i >= j:  # if the two pointers crossed
            return j

        arr[i], arr[j] = arr[j], arr[i]     # swap the elements on the pointers


def quick_sort(arr):
    fisher_yates_shuffle(arr)   # we shuffle for performance guarantee
    quick_sort_next(arr, 0, len(arr) - 1)


def quick_sort_next(arr, low, high):
    if low < high:
        p_idx = partition(arr, low, high)   # partition index

        # separately sort elements before and after partition
        quick_sort_next(arr, low, p_idx)     # recursively sort the subarrays
        quick_sort_next(arr, p_idx + 1, high)


# Driver Code
my_array = [5, 2, 3, 1, 8, 10, 4, 9]
print(f"Original array: {my_array}")
quick_sort(my_array)
print(f"Sorted array: {my_array}")




