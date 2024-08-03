# A lambda functions is a small anonymous function.
# It can take any num of args, but can only have one expression
# The power of lambda is shown when you use them as an anonymous function inside another function
# Use lambda functoins when an anonymous function is required for a short period of time

x = lambda a, b: a + b
print(x(5, 3))


def build_quad_func(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


build_quad_func(1, 2, 3)(3)
