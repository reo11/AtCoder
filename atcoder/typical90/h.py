n = int(input())
s = input()
s_atcoder = "atcoder"
m = len(s_atcoder)
MOD = 1000000007

# dp[i][j]: 上からi文字目までで、j文字までを完成させられる数
# dp[n][m]が答えとなる

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(n):
    dp[i][0] = 1

for i in range(1, n + 1):
    for j in range(m + 1):
        dp[i][j] = dp[i - 1][j]
    for j in range(1, m + 1):
        # print(s_atcoder[j - 1], s[i - 1], i, j)
        if s_atcoder[j - 1] == s[i - 1]:
            dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] %= MOD
print(dp[n][m])