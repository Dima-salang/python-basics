# divide and conquer algorithm
# we divide the array into two subarrays and then sort them then merge both
# first subarray is arr[l..m]
# second subarray is arr[m+1..h]

# Time Complexity = O(n*log(n)) same for best, worst, and average
# Auxiliary Space = O(n)
# Stable = Yes

def merge(arr):
    if len(arr) > 1:
        m = len(arr) // 2  # get median

        # create two sub-arrays and copy halves of merged array
        L = arr[:m]
        R = arr[m:]

        # Sort two halves
        merge(L)
        merge(R)

        # initialize three pointers
        # i for initial index of first subarray
        # j for initial index of second subarray
        # k for initial index of merged array
        i = j = k = 0

        # Until we reach the length of 1st and 2nd subarray
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:  # compare elems of subarrays
                arr[k] = L[i]  # then assign to merged array
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # When we run out of elems in either L or R, we copy the remaining
        while i < len(L):  # if satisfied, skip
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Driver Program
my_array = [13, 12, 11, 5, 4, 3, 2]
print(f"Given array is: {my_array}")
merge(my_array)
print(f"Sorted array is: {my_array}")





