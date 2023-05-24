n = int(input())
h = list(map(int, input().split()))
h = [0] + h  # indexをずらす為に0を追加

dp = [float("inf") for _ in range(n + 1)]
dp[1] = 0  # 足場1でスタート時のコストは0
dp[2] = abs(h[2] - h[1])  # 足場2でスタート時のコストは足場1から足場2へのコスト

# 足場3~Nで2択が生まれる
for i in range(3, n + 1):
    pattern1 = dp[i - 1] + abs(h[i] - h[i - 1])
    pattern2 = dp[i - 2] + abs(h[i] - h[i - 2])
    dp[i] = min(pattern1, pattern2)

print(dp[n])
