# can be w for write and a for append and r+ for reading and writing
with open("Pounds.py", "r+") as f:
    read_data = f.read()
    print(read_data)
    print(f.readline())  # to read a single line
    print(f.readlines())  # returns all lines the file as a list
    for line in f:
        # loops over lines in a file for memory efficiency
        print(line, end="")
    print(f.write("Hello !"))  # writes the content of string to the file and returns the num of chars written
    print(f.readable())  # returns True if file is readable
    print(f.writable())  # returns True if file is writable

