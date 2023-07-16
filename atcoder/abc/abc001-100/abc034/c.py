MOD = 10 ** 9 + 7
w, h = map(int, input().split())

dp = [[1 for _ in range(w)] for _ in range(h)]

for i in range(1, h):
    for j in range(1, w):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        dp[i][j] %= MOD
print(dp[h - 1][w - 1])
