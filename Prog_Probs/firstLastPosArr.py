"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 


"""

from typing import List

def searchRange(nums:List[int], target:int) -> List[int]:
    
    if not nums:
        return [-1, -1]

    left = 0
    right = len(nums)-1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            leftPointer = rightPointer = mid
            while leftPointer != 0 and nums[leftPointer-1] == nums[mid]:
                    leftPointer -= 1
            while rightPointer+1 != len(nums) and nums[rightPointer+1] == nums[mid]:
                    rightPointer += 1
            return [leftPointer, rightPointer]
        elif target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
    
    return [-1, -1]
    

print(searchRange([5, 7, 7, 8, 8, 10], 6))
print(searchRange([], 10))
print(searchRange([5, 7, 7, 8, 8, 10, 10, 10], 11))
