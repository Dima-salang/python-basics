import math

num = input("Enter a number: ")  # input for a number
num_sqrt = int(num) ** 0.5  # square root
print(num_sqrt)

# Check if a number is squared
def is_square(n):
    result = math.sqrt(n) # Get sqrt
    if result * result == float(n): # multiply result again to compare to the argument
        return True
    else:
        return False

is_square(25)

# //


def is_square2(n2):
    return n2 >= 0 and (n2**0.5) % 1 == 0 # You can use remainder to check if squared as decimal points are remainders.


def is_square3(n3):
    if n3 < 0:
        return False

    sqrt = math.sqrt(n3)

    return sqrt.is_integer()
