# Program to print the multiplication table of a number.

def print_multiplication_table(num):
    for i in range(1, 10+1):
        product = i * num
        print(f"{i} x {num} = {product}")


print_multiplication_table(13)
