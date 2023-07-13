MOD = 998244353
n, x = map(int, input().split())

# dpっぽい
dp = [[[0 for _ in range(2)] for _ in range(n + 1)] for _ in range(n + 1)]
# dp[i][j][k]
# i番目までで、数字jを使っている: k=1, 使っていない: k=0, の場合の数

for i in range(1, n + 1):
    dp[0][i][0] = 1

# 貰うDP
for i in range(1, n + 1):
    min_pi = i - x
    max_pi = i + x
    for j in range(1, n + 1):
        if j <= min_pi or j >= max_pi:
            # 使えるjはそれまでの状態から遷移させる
            for k in range(1, n + 1):
                if j == k:
                    continue
                dp[i][j][1] += (dp[i - 1][k][0] + dp[i - 1][k][1])
            dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1]
        else:
            # 使えないjは飛ばす
            dp[i][j][0] = dp[i - 1][j][0]
            dp[i][j][1] = dp[i - 1][j][1]
        dp[i][j][0] %= MOD
        dp[i][j][1] %= MOD
print(dp)
ans = 0
for i in range(1, n + 1):
    ans += dp[-1][i][1]
    ans %= MOD
print(ans)