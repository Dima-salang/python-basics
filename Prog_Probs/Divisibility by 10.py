"""
You are provided an array A of size N
 that contains non-negative integers. Your task is to determine whether the number that is formed by selecting the
 last digit of all the N numbers is divisible by 10.
"""


def divisible_by_10():
    print("Enter size of input")
    iterations = input()
    print(f"Enter {iterations} numbers")
    last_digit = []  # Reading input from STDIN
    for i in range(int(iterations)):
        num = input()
        last_digit.append(num[-1])
    formed_num = (int("".join(last_digit)))
    if formed_num % 10 == 0:
        print(f"Yes: {formed_num}")
    else:
        print(f"No: {formed_num}")


divisible_by_10()
