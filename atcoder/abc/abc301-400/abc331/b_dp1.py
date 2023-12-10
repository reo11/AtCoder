n, s, m, l = map(int, input().split())
INF = float('inf')
# dp[i]: i個の卵を買うのにかかる最小の金額
dp = [INF] * (n + 13) # 12個が最大なので

dp[0] = 0
# 貰うDP
for i in range(6, len(dp)):
    if i - 6 >= 0:
        dp[i] = min(dp[i], dp[i - 6] + s)
    if i - 8 >= 0:
        dp[i] = min(dp[i], dp[i - 8] + m)
    if i - 12 >= 0:
        dp[i] = min(dp[i], dp[i - 12] + l)

print(min(dp[n:]))