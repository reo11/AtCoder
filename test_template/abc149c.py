from typing import List


def primes(n: int) -> List[bool]:
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return is_prime


x = int(input())
p = primes(10 ** 6)

while True:
    if p[x]:
        break
    else:
        x += 1
print(x)
