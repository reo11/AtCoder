n, s = map(int, input().split())
a = list(map(int, input().split()))
MOD = 998244353

dp = [0 for _ in range(s+1)]
dp[0] = 1
for v in a:
    for i in reversed(range(s-v+1)):
        dp[i+v] += dp[i] * (MOD+1) // 2
        dp[i+v] %= MOD

print(dp[s] * pow(2, n, MOD) % MOD)