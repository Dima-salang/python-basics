def anagram(string1, string2):
    # this sorting takes O(NlogN) time.
    # basically, it's the same as
    return sorted(list(string1)) == sorted(list(string2))


# another method would also be converting each char in the string to ascii representation and getting the sum
# if the sum of the strings is equal, then they are anagrams.

