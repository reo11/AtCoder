from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))


def gcd(a: int, b: int) -> int:
    # 最大公約数
    # (12, 18) -> 6
    while b:
        a, b = b, a % b
    return a


def prime_factorize(n: int):
    # 素因数分解
    # Return list of prime factorized result
    # O(sqrt(n))
    counter = defaultdict(int)
    while n % 2 == 0:
        counter[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            counter[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        counter[n] += 1
    return counter


gcd_value = a[0]
for ai in a[1:]:
    gcd_value = gcd(gcd_value, ai)

ans = 0
flag = True
for ai in a:
    ci = prime_factorize(ai // gcd_value)
    for key, value in ci.items():
        if key != 2 and key != 3:
            flag = False
            break
        else:
            ans += value

if flag:
    print(ans)
else:
    print(-1)
