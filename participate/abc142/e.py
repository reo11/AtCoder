n, m = map(int, input().split())
a = [0] * m
b = [0] * m
c = [[] for _ in range(m)]
for i in range(m)
    a[i], b[i] = map(int, input().split())
    c[i] = list(map(int, input().split()))

INF = 1e9

dp = [[INF for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, m+1):
    idx = i - 1
    flag = False
    for c_ in c[idx]:
        if dp[i-1][c_-1] == INF:
            flag = True
            break
    if flag:
        dp[i][0] = dp[i-1][0] + a[idx]
        for c_ in c[idx]:
            dp[i][c_-1] = min(dp[i-1][c_-1], a[i])
