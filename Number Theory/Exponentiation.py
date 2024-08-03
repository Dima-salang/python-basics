# Usual method
# O(n)

def exp(base, exponent):
    result = 1
    while exponent > 0:
        result *= base
        exponent -= 1
    return result


print(exp(2, 5))


def exp_by_squaring(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return (1/base) ** exponent
    elif exponent % 2 == 0:
        return exp_by_squaring((base ** (base/2)), 2)
    else:
        return base * (base ** (base-1)/2) ** 2


print(exp_by_squaring(3, 6))