import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = 998244353
n = int(input())
a = list(map(int, input().split()))
inv_n = pow(n, MOD - 2, MOD) # 1/nをあらかじめ計算しておく
memo = [0 for _ in range(n + 1)]

stuck = 0
for i in reversed(range(1, n + 1)):
    res = a[i - 1]
    res += stuck * inv_n
    res %= MOD
    stuck += res
    stuck %= MOD
    res %= MOD
    memo[i] = res

ans = 0
for i in reversed(range(1, n + 1)):
    ans += memo[i] * inv_n
    ans %= MOD
print(ans)