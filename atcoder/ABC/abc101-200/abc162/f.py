# dpでいけそう
n = int(input())
a = list(map(int, input().split()))
INF = 10**16

ans = -INF

a = [0, 0, 0, 0] + a
dp = [[-INF for _ in range(n+4)] for _ in range(3)]
dp[0][2] = 0
for i in range(4, len(a)):
    dp[2][i] = max(dp[2][i], dp[1][i-3] + a[i], dp[0][i-4] + a[i], dp[2][i-2] + a[i])
    dp[1][i] = max(dp[1][i], dp[0][i-3] + a[i], dp[1][i-2] + a[i])
    dp[0][i] = max(dp[0][i], dp[0][i-2] + a[i])
if n % 2 == 1:
    ans = max(ans, dp[0][n])
    ans = max(ans, dp[1][n+2])
    ans = max(ans, dp[2][n+3])
else:
    ans = max(ans, dp[0][n+2])
    ans = max(ans, dp[1][n+3])
# print(dp)
print(ans)