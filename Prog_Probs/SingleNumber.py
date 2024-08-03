"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

# brute-force approach
def single_number(nums):
    for elem in nums:
       if nums.count(elem) == 1:
            return elem


# we can also use sorting but that would be O(nlogn) for sorting and then O(n) for looping.

# we can also just use a hashmap or a dictionary to track frequencies.

def single_number_dict(nums):
    nums_dict = {}

    for elem in nums:
        if elem not in nums_dict:
            nums_dict.update({elem: 1})
        else:
            nums_dict[elem] += 1

    for key, value in nums_dict.items():
        if value == 1:
            return key


"""
Use Xor/Bit Manipulation
Intuition:
Xor of any two num gives the difference of bit as 1 and same bit as 0.
Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
So, we will always get the single element because all the same ones will evaluate to 0 and 0^single_number = single_number.
Time: O(n)
Space: O(1)
"""


def single_number_xor(nums):
    xor = 0
    for num in nums:
        xor ^= num

    return xor
