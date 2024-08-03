"""Given an integer array nums, return true if any value appears at least twice in the array,
 and return false if every element is distinct.
 """


def contains_duplicates(arr):
    # we just check if the num has duplicates for the whole sliced list
    counter = 0
    for num in arr:
        if num in arr[counter+1:]:
            return True
        else:
            counter += 1
    return False


def contains_duplicates_set(arr):
    # we just make it a set. if num is in set, we return True. If it is not, we add it to the set.
    num_set = set()
    for num in arr:
        if num in num_set:
            return True
        num_set.add(num)
    return False


def contains_duplicates_len_set(arr):
    # here, we just use the fact that if there are duplicates, the set will reduce the len of the arr
    # if the len of the set does not match the len of arr, there are duplicates.
    num_set = set(arr)
    if len(num_set) != len(arr):
        return True
    return False


duplicates = [1, 1, 2, 3]
no_duplicates = [1, 2, 3, 4]
print(contains_duplicates(duplicates))
print(contains_duplicates(no_duplicates))
print(contains_duplicates([3, 3]))

print("Contains duplicates set")
print(contains_duplicates_set([3, 3]))
print(contains_duplicates_set(duplicates))
print(contains_duplicates_set(no_duplicates))

print("Contains duplicates using len of num set")
print(contains_duplicates_len_set(duplicates))
print(contains_duplicates_len_set(no_duplicates))
