# We use the wildcard or * notation as our function's argument when we have doubts about the number of arguments we
# should pass in a function

# *args is used in function definitions to pass a variable number of arguments to a function. It allows you to take in
# more arguments than the number of formal arguments that you previously defined. It is an argument collector and
# collects positional arguments passed into it. It's same with keyword args but for keyword arguments.
def multiply(letter, *args, **kwargs):
    print(args, kwargs, letter)


multiply("a", 123, 24, number=23)
