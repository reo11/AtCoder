from math import factorial


def comb(n, r):
    return factorial(n) / factorial(r) / factorial(n - r)


n, k = map(int, input().split())
