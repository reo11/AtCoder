from collections import defaultdict

n, a, x, y = map(int, input().split())
size = 5
dp = [defaultdict(int) for _ in range(size)]

dp[0][n] = 0
for i in range(1, size):
    keys = dp[i - 1].keys()
    for key in keys:
        dp[i][key] = dp[i - 1][key]
        dp[i][key // a] += x
        for j in range(1, 7):
            dp[i][key // j] += (y / 6)

print(dp)
