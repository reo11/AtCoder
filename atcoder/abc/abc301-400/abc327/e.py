import math
from decimal import Decimal

n = int(input())
p = list(map(int, input().split()))
INF = float("inf")
MAX_NUM = 5100

# 上位m個を使うのが最適
# 0.9**iを前計算
# 長さkの最大スコアを求め続ける
# dp
# dp[i][j]: 左端が右からiで長さがjの時の最大スコア
memo = [1, 0.9]
sums = [1, 1.9]
bias = [0, 1200]
for i in range(2, MAX_NUM + 1):
    memo.append(memo[-1] * 0.9)
    sums.append(sums[-1] + memo[-1])
    bias.append(1200 / math.sqrt(i))

dp = [[-INF] * (n + 1) for _ in range(n + 1)]

# length = 1を初期化
for i in range(1, n + 1):
    dp[1][i] = max(dp[1][i - 1], p[-i] - 1200)

for length in range(2, n + 1):
    for i in range(length, n + 1):
        if dp[length - 1][i - 1] == -INF:
            continue
        r = dp[length - 1][i - 1] + bias[length - 1]
        r *= sums[length - 2]
        r += memo[length - 1] * p[-i]
        r /= sums[length - 1]
        r -= bias[length]
        # print(length, i, r)
        dp[length][i] = max(dp[length][i], r)

ans = -INF
for i in range(len(dp)):
    for j in range(len(dp[i])):
        ans = max(ans, dp[i][j])
print(ans)