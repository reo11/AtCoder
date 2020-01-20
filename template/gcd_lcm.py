from functools import reduce

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
