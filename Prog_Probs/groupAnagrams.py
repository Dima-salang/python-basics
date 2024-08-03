"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once. """


def group_anagrams(self, strs):
    seen = {}
    for string in strs:
        sorted_string = ''.join(sorted(string))
        if sorted_string in seen:
            seen[sorted_string].append(string)
        else:
            seen[sorted_string] = [string]
    ans = [value for value in seen.values()]
    return ans



