import itertools

def permute(str_arr):
    perms = set(itertools.permutations(str_arr))
    for perm in perms:
        joined_str = "".join(perm)
        print(joined_str)

permute(["b", "o", "b", "a"])
