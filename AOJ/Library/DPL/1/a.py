n, m = map(int, input().split())
c = list(map(int, input().split()))

INF = 10**9
MAX = n + 1
dp = [INF for _ in range(MAX)]
dp[0] = 0
for i in range(m):
    for j in range(len(dp)):
        if j + c[i] < MAX:
            dp[j+c[i]] = min(dp[j] + 1, dp[j+c[i]])

min_v = dp[-1]
for i in range(len(dp)):
    idx = len(dp) - 1 - i
    min_v = min(min_v, dp[idx])
    dp[idx] = min_v

print(dp[n])
