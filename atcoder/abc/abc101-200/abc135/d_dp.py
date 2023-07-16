MOD = 10 ** 9 + 7
s = str(input())
l = len(s)
dp = [[0 for _ in range(2)] for _ in range(l + 1)]
dp[0][0] = 0
if s[-1] == "5":
    dp[0][1] = 1
else:
    dp[0][1] = 0

for i in range(1, l + 1):
    if s[i] == "?":
        dp[i][0] = (dp[i - 1][0] * 10) % MOD
        dp[i][1] = (dp[i - 1][0] * 10) % MOD
    else:
        dp[i][0] = dp[i - 1][0]
        dp[i][1] = dp[i - 1][1]

print(dp[l][1])
