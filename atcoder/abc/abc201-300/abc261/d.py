from collections import defaultdict

n, m = map(int, input().split())
x = list(map(int, input().split()))
cy = defaultdict(lambda: 0)

for _ in range(m):
    c, y = map(int, input().split())
    cy[c] = y

# DPする
# dp[i][j]: i番目の箱までコイントスした時に、カウンタの数値がjの時の最大金額
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i):
        # 表
        dp[i][j + 1] = max(dp[i][j + 1], dp[i - 1][j] + x[i - 1] + cy[j + 1])
    for j in range(n + 1):
        # 裏
        dp[i][0] = max(dp[i][0], dp[i - 1][j])
print(max(dp[n]))