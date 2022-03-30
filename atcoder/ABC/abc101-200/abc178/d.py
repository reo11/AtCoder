s = int(input())
MOD = 10**9+7
dp = [0] * 10000
dp[0] = 1
dp[1] = 0
dp[2] = 0
for i in range(3, s+1):
    dp1 = dp[i-1] if i - 1 >= 0 else 0
    dp2 = dp[i-3] if i - 3 >= 0 else 0
    dp[i] = dp1 + dp2
    dp[i] %= MOD
print(dp[s])