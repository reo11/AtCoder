from math import factorial


def comb(n, r):
    return factorial(n) / factorial(r) / factorial(n - r)


def perm(n, r):
    return factorial(n) // factorial(n - r)


MOD = 10**9 + 7

n = int(input())
c = list(map(int, input().split()))
c.sort(reverse=True)

ans = 0
for i in range(1, n + 1):
    ans += comb(n, i) * i * c[i - 1] * 2
    ans %= MOD
print(ans)
