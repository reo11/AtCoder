from math import factorial
MOD = 10**9 + 7

# 階乗を用意
fact = [1] * (10**5 + 1)
for i in range(1, 10**5 + 1):
    fact[i] = fact[i-1] * i
    fact[i] %= MOD

def comb(n, k, p):
    """power_funcを用いて(nCk) mod p を求める"""
    global fact
    if n < 0 or k < 0 or n < k:
        return 0
    if n == 0 or k == 0:
        return 1
    a = fact[n]
    b = fact[k]
    c = fact[n-k]
    return (a*power_func(b, p-2, p)*power_func(c, p-2, p)) % p

def power_func(a, b, p):
    """a^b mod p を求める"""
    if b == 0:
        return 1
    if b % 2 == 0:
        d = power_func(a, b//2, p)
        return d*d % p
    if b % 2 == 1:
        return (a*power_func(a, b-1, p)) % p

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans = 0

# pos
for i in range(n-1):
    c = comb(n-1-i, k-1, MOD)
    ans += a[n-1-i] * c
    ans %= MOD
    ans -= a[i] * c
    ans %= MOD
print(ans)

