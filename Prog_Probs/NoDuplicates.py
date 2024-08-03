# remove duplicates within an array. traverse arr and if num has duplicates after num, remove num.


def remove_duplicates(arr):
    for num in arr:
        if num in arr[arr.index(num)+1:]:
            arr.remove(num)
    return arr


# remove duplicates using sets
def remove_duplicates_sets(arr):
    arr = set(arr)
    arr = list(arr)
    return arr


print(remove_duplicates([1, 1, 3, 4, 5, 6, 6]))
print(remove_duplicates_sets([1, 1, 3, 4, 5, 6, 6]))
