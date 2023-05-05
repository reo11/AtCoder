n, k = map(int, input().split())
h = list(map(int, input().split()))
h = [0] + h
dp = [float("inf") for _ in range(n + 1)]
dp[1] = 0 # 足場1でスタート時のコストは0

for i in range(1, n):
    for j in range(1, k + 1):
        if i + j < n + 1:
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i] - h[i + j]))
print(dp[n])