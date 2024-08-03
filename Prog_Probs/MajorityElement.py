def find_majority_dict(nums_arr):
    # dictionary approach
    num_dict = {}
    max_key = 0
    max_val = 0
    for num in nums_arr:
        if num not in num_dict:
            num_dict.update({num: 1})
        else:
            num_dict[num] += 1
    print(num_dict.items())
    for key, val in num_dict.items():
        if val > max_val:
            max_val = val
            max_key = key
    return max_key


def find_majority_sort(nums_arr):
    # we use the fact that the majority element is n/2 + 1 and therefore if you sort it so that duplicate
    # elements are grouped together, then they would always extend over to half of the array.
    # then we can just return the num at n/2 index.
    sorted_arr = sorted(nums_arr)
    print(sorted_arr)
    return sorted_arr[len(sorted_arr) // 2]


def find_majority_moore_algo(nums_arr):
    """The Boyer-Moore voting algorithm is one of the popular optimal # algorithms which is used to find the
    majority element among the given elements that have more than N/ 2 occurrences. # This algorithm works on the
    fact that if an element occurs more than N/2 times, # it means that the remaining elements other than this would
    definitely be less than N/2.

    # First, choose a candidate from the given set of elements if it is the same as the candidate element,
    # increase the votes. Otherwise, decrease the votes if votes become 0, select another new element as the new
    candidate.

    # Intuition Behind Working : # When the elements are the same as the candidate element, votes are incremented
    whereas when some other element is found # (not equal to the candidate element), we decreased the count. This
    actually means that we are decreasing the priority of # winning ability of the selected candidate, since we know
    that if the candidate is in majority it occurs more than N/2 times # and the remaining elements are less than
    N/2. We keep decreasing the votes since we found some different element(s) than the # candidate element. When
    votes become 0, this actually means that there are the equal  number of votes for different # elements,
    which should not be the case for the element to be the majority element. So the candidate element cannot # be the
    majority and hence we choose the present element as the candidate and continue the same till all the elements #
    get finished. The final candidate would be our majority element. We check using the 2nd traversal to see whether
    # its count is greater than N/2. If it is true, we consider it as the majority element. """

    # O(n) time complexity
    # 0(1) space complexity

    candidate = -1
    votes = 0
    # find majority candidate
    for num in range(len(nums_arr)):
        if votes == 0:
            candidate = nums_arr[num]
            votes = 1
        else:
            if nums_arr[num] == candidate:
                votes += 1
            else:
                votes -= 1
    count = 0
    # check if majority candidate occurs more than n/2 times
    for num in range(len(nums_arr)):
        if nums_arr[num] == candidate:
            count += 1
    if count > len(nums_arr) // 2:
        print(f"Majority element is: {candidate} with {count} frequency")
        return candidate
    else:
        return -1


print(find_majority_dict([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 3]))
print(find_majority_sort([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 3, 0, 0, 0, 0]))
print(find_majority_moore_algo([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 3, 0, 0, 0, 0]))
