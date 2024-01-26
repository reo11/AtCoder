import math

MOD = 10**9 + 7


def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)


print(permutations_count(1998, 3) % MOD)
