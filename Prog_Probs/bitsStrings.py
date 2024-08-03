def generate_valid_strings(length):
    valid_strings = []

    # Case 1: Strings starting with "01"
    valid_strings.append("01" + format(i, '0' + str(length - 2) + 'b') + "10" for i in range(2 ** (length - 2)))

    # Case 2: Strings ending with "10"
    valid_strings.append("10" + format(i, '0' + str(length - 2) + 'b') + "01" for i in range(2 ** (length - 2)))

    return valid_strings

def print_valid_strings(length):
    valid_strings = generate_valid_strings(length)
    for case_strings in valid_strings:
        for string in case_strings:
            print(string)

# Specify the bit length
bit_length = 4  # You can change this to any desired length

# Print all valid bit strings for the specified length
print_valid_strings(bit_length)
