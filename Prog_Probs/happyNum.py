"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
"""

"""
We can actually solve this using the Floyd Cycle Detection Algorithm.
"""


def is_happy(nums):
    trans_str = str(nums)
    parsed_num = parse_num(trans_str)
    counter = 0
    while counter < 50:
        if parsed_num == 1:
            return True
        else:
            parsed_num = parse_num(str(parsed_num))
            counter += 1
    return False
            


def parse_num(trans_str):
    sum = 0
    for num in trans_str:
        trans_num = int(num)
        print(f"{trans_num}^2", end=" ")
        sqred = trans_num **2
        sum += sqred
    print(f"= {sum}")
    return sum

        

num = 323
if is_happy(num):
    print(num, " is happy!")
else:
    print(num, " is not happy! :<")
    print(num, " is happy!")
