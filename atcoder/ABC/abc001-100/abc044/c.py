n, a = map(int, input().split())
x = list(map(int, input().split()))
x_max = max(x)
dp = [[[0 for _ in range(n * x_max + 1)] for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n * x_max + 1):
            if i == 0 and j == 0 and k == 0:
                dp[i][j][k] = 1
            elif i >= 1 and k < x[i - 1]:
                dp[i][j][k] = dp[i - 1][j][k]
            elif i >= 1 and j >= 1 and k >= x[i - 1]:
                dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k - x[i - 1]]
            else:
                dp[i][j][k] = 0
ans = 0
for k in range(1, n + 1):
    if k * a <= n * x_max:
        ans += dp[n][k][k * a]
print(ans)
