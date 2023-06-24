n = int(input())
xy = []

for _ in [0] * n:
    x, y = map(int, input().split())
    xy.append([x, y])

# dp
dp = [[0 for _ in range(2)] for _ in range(n + 1)]

for i in range(n):
    if xy[i][0] == 0:
        # 解毒剤入り
        dp[i + 1][0] = max(dp[i][0], dp[i][1] + xy[i][1], dp[i][0] + xy[i][1])
        dp[i + 1][1] = dp[i][1]
    else:
        # 毒入り
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = max(dp[i][1], dp[i][0] + xy[i][1])
print(max(dp[-1]))