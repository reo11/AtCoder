from functools import reduce

# python > pypy


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(x, y):
    return (x * y) // gcd(x, y)


def gcd_list(numbers):
    return reduce(gcd, numbers)


def lcm_list(numbers):
    return reduce(lcm, numbers)


n = int(input())
a = list(map(int, input().split()))

print(gcd_list(a))
