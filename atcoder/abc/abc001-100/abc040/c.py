n = int(input())
a = list(map(int, input().split()))
a.insert(0, 10**9)
dp = [0] * (n + 1)
dp[2] = abs(a[1] - a[2])
for i in range(3, n + 1):
    dp[i] = min(dp[i - 2] + abs(a[i] - a[i - 2]), dp[i - 1] + abs(a[i] - a[i - 1]))
print(dp[n])
