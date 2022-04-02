from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(x, y):
    # saisyou koubaisuu
    return (x * y) // gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm, numbers)
