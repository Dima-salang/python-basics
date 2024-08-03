def findMaxConsecutiveOnes(nums):
    max_cons_ones = 0
    cons_ones = 0
    for i in nums:
        if i == 0:
            cons_ones = 0
        else:
            cons_ones += 1
            max_cons_ones = max(cons_ones, max_cons_ones)
    return max_cons_ones


print(findMaxConsecutiveOnes([1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))