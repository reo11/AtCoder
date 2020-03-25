n, w = map(int, input().split())
vw = [input().split() for _ in range(n)]
vw = [(int(x[0]), int(x[1]))for x in vw]

dp = [0 for _ in range(w+1)]

for i in range(n):
    for j in range(w):
        if j + vw[i][1] < w + 1:
            dp[j + vw[i][1]] = max(dp[j + vw[i][1]], dp[j] + vw[i][0])
print(max(dp))
