def recursive(n, n2):
    if (n < n2):
        return -3
    else:
        return recursive(n-n2, n2+3) + n2

print(recursive(15, 3))