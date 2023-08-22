import math
from typing import List
from collections import defaultdict


def prime_factorize(n: int) -> List[int]:
    # 素因数分解
    # Return list of prime factorized result
    # O(sqrt(n))
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return sorted(a)

k = int(input())
k_factors = defaultdict(lambda: 0)

for factor in prime_factorize(k):
    k_factors[factor] += 1

ans = 0
for factor, v in k_factors.items():
    i = 1
    # print(k_factors)
    while k_factors[factor] > 0:
        k_factors[factor] -= 1
        j = i
        while j % factor == 0 and j != 0:
            j //= factor
            k_factors[factor] -= 1
        if k_factors[factor] == 0:
            break
        i += 1
    ans = max(ans, factor * i)
print(ans)