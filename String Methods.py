# Strings: ordered, immutable, text representation

message = 'This is for you.'
message2 = bin(1234)
print(len(message))  # to know the number of characters in a string.

print(message.upper())  # to convert the string into all uppercase.

print(message.lower())  # to convert the string into all lowercase.

print(message.find('This'))  # to find the index of a character in the string.

print(message.replace('This', 'That'))  # to replace characters in a string.

print('This' in message)  # in-operator to determine if a character is in the string.

print(message2.count("1"))  # counts the number of occurrences of a substring.

print(message2.casefold())  # for caseless matching. Ignores cases when matching.

print(message.strip())  # eliminates all whitespace

print(message.startswith("T"))
print(message.startswith("This"))
print(message.endswith("."))

my_list = message.split()  # returns a list by splitting by given separator
new_string = " ".join(my_list)
print(new_string)


