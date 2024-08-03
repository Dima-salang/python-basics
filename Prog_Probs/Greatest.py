def greatest():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    num3 = input("Enter third number: ")

    return max(num1, max(num2, num3))


print(greatest())
