from functools import reduce


def gcd(a, b):
    # saidai kouyakusuu
    while b:
        a, b = b, a % b
    return a


def gcd_list(numbers):
    return reduce(gcd, numbers)
