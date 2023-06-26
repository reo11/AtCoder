MOD = 998244353
n, m = map(int, input().split())

# dp[i][j] = i番目までの商品で隣同士が別の整数を持つ場合の数
# j: 0の場合はi番目の数が1番目と同じ場合の数
# j: 1の場合はi番目の数が1番目と異なる場合の数

dp = [[0] * 2 for _ in range(n + 1)]
dp[1][0] = m % MOD
dp[1][1] = 0

for i in range(2, n + 1):
    # 1と同じ場合
    # 1つ前は1と異なる必要がある
    dp[i][0] = dp[i - 1][1]
    # 1と異なる場合
    # 1つ前と異なり、1とも異なる必要がある
    dp[i][1] = dp[i - 1][0] * (m - 1) + dp[i - 1][1] * (m - 2)

    for j in range(2):
        dp[i][j] %= MOD

print(dp[-1][1])