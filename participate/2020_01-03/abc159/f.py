n, s = map(int,input().split())
a = list(map(int,input().split()))
mod = 998244353

dp = [0] * (s+1)
ans = 0
for i in range(n):
    ndp = dp[:]
    if a[i] <= s:
        ndp[a[i]] = (ndp[a[i]] + i + 1) % mod
    for j in range(s):
        if j + a[i] <= s:
            ndp[j+a[i]] = (ndp[j+a[i]] + dp[j]) % mod
    ans = (ans + ndp[s]) % mod
    dp = ndp[:]
print(ans)
