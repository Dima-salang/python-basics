#  dictionaries are indexed by keys. It is best to think of it as a set of key: value pairs, with the
#  requirement that the keys are unique. A pair of braces create an empty dictionary and placing a comma-separated
#  list of key:value pairs within the braces adds initial key:value pairs to the dictionary.

dict_type = {"james": 123, "jim": 1234, "jam": 12345}
dict_type["jin"] = 123456  # adding a key value pair
print(dict_type)

print(dict_type["james"])  # accessing key to get value.
del dict_type["jam"]  # deleting key jam and its value.
print(dict_type)
print(list(dict_type))  # converting a dictionary to a list
sorted(dict_type)  # sorting
print(dict(dict_type))  # converting list to dictionary

dictionary1 = {"name": "James", "age": 19, "country": "Philippines"}
dictionary1.update(name="Luis", nationality="Filpino")
print(dictionary1)


# Looping techniques
# When looping through dictionaries, the key and corresponding value can be accessed through items()
for key, value in dict_type.items():
    print(key, value)

# When looping through a sequence, the position index and corresponding key can be retrieved at the same time
# using the enumerate() function.

for index, key in enumerate(dict_type):
    print(index, key)

# To loop over two sequences at the same time, use zip() function.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alphabet = ["a", "b", "c", "d", "e"]

for num, letter in zip(numbers, alphabet):
    print(num, letter)


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
hour_freq = dict()
hours_lst = []
handle = open(name)
for line in handle:
    line_split = line.split()
    if line_split:

        if line_split[0] == "From ":
            hours = line_split[5].split(':')
            hour_freq[hours] = hour_freq.get(hours, 0)+1

for key, value in hour_freq.items():
    hours_lst.append((key, value))
    print((key, value))

hours_lst.sort()
for hour, count in hours_lst:
    print(f"{hour} {count}")
