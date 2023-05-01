n = int(input())
dcs = []
max_d = 0
for _ in range(n):
    d, c, s = map(int, input().split())
    max_d = max(max_d, d)
    dcs.append([d, c, s])

dp = [[0 for _ in range(max_d + 1)] for _ in range(n + 1)]
# dp[i][j]: i個目までの案件の中で、j日目までに得られる最大利益

# 遷移
# 終了日(D_i)が早い順にこなすのが最適で、Sortした後貪欲DP
dcs.sort()

for i in range(1, n + 1):
    d, c, s = dcs[i - 1]
    for j in range(max_d + 1):
        if j <= d and j - c >= 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c] + s)
        else:
            dp[i][j] = dp[i - 1][j]
print(max(dp[-1]))
# print(dp)
