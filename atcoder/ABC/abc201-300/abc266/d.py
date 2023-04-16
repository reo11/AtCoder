import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
txa = dict()
for _ in range(n):
    t, x, a = map(int, input().split())
    txa[t] = [x, a]

# 時刻iにx_jにいる時の最大値
dp = [[-float("inf") for j in range(7)] for i in range(100001)]
dp[0][1] = 0

for i in range(1, 100001):
    for j in range(1, 6):
        if i in txa and txa[i][0] == j - 1:
            # すぬけ君を捕まえる
            dp[i][j] = max(
                dp[i - 1][j] + txa[i][1],
                dp[i - 1][j - 1] + txa[i][1],
                dp[i - 1][j + 1] + txa[i][1],
            )
        else:
            # 移動するだけ
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1])

print(max(dp[-1]))
