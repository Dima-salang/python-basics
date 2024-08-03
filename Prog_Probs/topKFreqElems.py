"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""


def top_k_freqs(self, nums: List[int], k: int) -> List[int]:
    freq_map = {}
    ans = []
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    # using a sort key to sort the freq_map by the values
    # it is the same as:
    # def sort_key(word):
    #   return word[1]
    sorted_dict = sorted(freq_map.items(), key=lambda item: item[1], reverse=True)
    for i in sorted_dict[:k]:
        ans.append(i[0])
    return ans


