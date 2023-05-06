n, w = map(int, input().split())
wv = []
for _ in range(n):
    wv.append(list(map(int, input().split())))
sum_v = sum([x[1] for x in wv])

dp = [[float("inf") for _ in range(sum_v + 1)] for _ in range(2)]
dp[0][0] = 0

for i in range(n):
    for j in range(sum_v + 1):
        if j - wv[i][1] >= 0:
            dp[1][j] = min(dp[0][j], dp[0][j - wv[i][1]] + wv[i][0])
    for j in range(sum_v + 1):
        dp[0][j] = min(dp[0][j], dp[1][j])

ans = 0
for i in range(sum_v + 1):
    if dp[1][i] <= w:
        ans = max(ans, i)
# print(dp)
print(ans)
