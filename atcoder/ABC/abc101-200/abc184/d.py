a, b, c = map(int, input().split())
# 確率DPをする

dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]
dp[a][b][c] = 1
for i in range(a, 100):
    for j in range(b, 100):
        for k in range(c, 100):
            if i == 100 or j == 100 or k == 100:
                continue
            if a > 0:
                dp[i + 1][j][k] += dp[i][j][k] * (i / (i + j + k))
            if b > 0:
                dp[i][j + 1][k] += dp[i][j][k] * (j / (i + j + k))
            if c > 0:
                dp[i][j][k + 1] += dp[i][j][k] * (k / (i + j + k))
ans = 0
for i in range(a, 101):
    for j in range(b, 101):
        for k in range(c, 101):
            if i == 100 or j == 100 or k == 100:
                ans += dp[i][j][k] * ((i - a) + (j - b) + (k - c))
print(ans)
