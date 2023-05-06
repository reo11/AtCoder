n, w = map(int, input().split())
wv = []
for _ in range(n):
    wv.append(list(map(int, input().split())))

dp = [[0 for _ in range(w + 1)] for _ in range(2)]

for i in range(n):
    for j in range(w + 1):
        if j - wv[i][0] >= 0:
            dp[1][j] = max(dp[0][j], dp[0][j - wv[i][0]] + wv[i][1])
    for j in range(w + 1):
        dp[0][j] = max(dp[0][j], dp[1][j])
# print(dp)
print(max(dp[-1]))

