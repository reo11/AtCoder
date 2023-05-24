from bisect import bisect_left

n = int(input())
a = [int(input()) for _ in range(n)]

INF = 10 ** 9
dp = [INF for _ in range(n)]
dp[0] = a[0]

for i in range(1, n):
    idx = bisect_left(dp, a[i])
    dp[idx] = a[i]

print(len(list(filter(lambda x: x != INF, dp))))
