n = int(input())
a = list(map(int, input().split()))
a.insert(0, 0)
dp = [0] * (n+1)

# 前からその時の最大を更新していく

dp[0] = 1000
dp[1] = 1000
for start in range(1, n):
    for end in range(start+1, n+1):
        if a[end] - a[start] > 0:
            cnt = dp[start] // a[start]
            money = dp[start] + (a[end] - a[start]) * cnt
            dp[end] = max(dp[end], money)
        else:
            dp[end] = max(dp[end], dp[start])
print(dp[-1])