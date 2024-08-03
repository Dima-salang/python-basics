"""
A suffix array is an array which contains all of the sorted suffixes of a string.

The actual suffix array is the array of sorted indices. This provides a compressed representation of the sorted
suffixes without actually needing to store the suffixes.

"""


def build_suffix_array(string):

    string += '$'

    string_size = len(string)

    suffixes = [(string[i:], i) for i in range(string_size)]

    suffixes.sort()

    suffix_array = [suffix[1] for suffix in suffixes]

    return suffix_array


text = "hello world"
suffix_array = build_suffix_array(text)
print(suffix_array)


