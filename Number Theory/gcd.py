def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, (a % b))


print(gcd(206, 40))

# Euclid's Algorithm for GCD. The gcd of a and b is the largest int
# that divies both a and b with no remainder.

# The idea of the algorithm is based on the observation that, if r
# is the remainder when a is divided by b, then the common divisors
# of a and b are precisely the same as b and r. Thus, we can use:
# gcd(a, b) = gcd(b, r) to successively reduce the problem by
# computing the gcd of smaller and smaller ints.
