"""Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k. """


def containsNearbyDuplicates(nums, k):
    nums_indices = {}  # create a dictionary to store previously seen elems
    for i, num in enumerate(nums):
        if num in nums_indices and abs(i - j) <= k:
            return True
        nums_indices[num] = i
    return False

