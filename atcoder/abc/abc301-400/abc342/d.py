from typing import List
from functools import lru_cache
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

@lru_cache(maxsize=None)
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
    return a

counter = defaultdict(lambda: 0)

for ai in a:
    counter_i = defaultdict(lambda: 0)
    if ai == 0:
        counter["0"] += 1
        continue

    for prime in prime_factorize(ai):
        counter_i[prime] += 1
        counter_i[prime] %= 2

    str_list = []
    for k, v in counter_i.items():
        if v == 1:
            str_list.append(str(k))
    counter[" ".join(sorted(str_list))] += 1

ans = 0
for k, v in counter.items():
    ans += v * (v - 1) // 2

ans += counter["0"] * (n - counter["0"])

print(ans)


