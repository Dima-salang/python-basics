def binary_search(target, array):
    left = 0
    right = len(array)-1

    while left <= right:
        mid = left + (right - left) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            left = mid + 1

        elif target < array[mid]:
            right = mid - 1
    return -1

def recursive_bin_search(target, left, right, array):
    if left <= right:
        mid = left + (right - left) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            return recursive_bin_search(target, mid + 1, right, array)
        else:
            return recursive_bin_search(target, left, mid - 1, array)
    return -1


arr1 = [1, 2, 3, 4, 5, 6 ,7]
print("hello")
print("index of 1 is: ", binary_search(1, arr1))
print("index of 1 is: ", recursive_bin_search(5, 0, len(arr1)-1, arr1))







