# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def factorial(num):
    result = 1
    for number in range(num, 0, -1):
        result *= number
    return result


def climbStairs(n):
    # return the combination since distinct steps and choose 2.
    return factorial(n) //(factorial(n-2))




print(factorial(3))
print(climbStairs(3))
print(climbStairs(4))
print(climbStairs(2))