MOD = 10 ** 9 + 7
n, k = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
dp[0][k] = 1

for i in range(1, n + 1):
    ai = a[i - 1]
    # 1個前の累積和を作る
    for j in range(1, k + 1):
        dp[i - 1][j] += dp[i - 1][j - 1]
        dp[i - 1][j] %= MOD
    for j in range(k + 1):
        # j: 残った飴の数
        max_idx = min(k, j + ai)
        va = dp[i - 1][max_idx]
        if j - 1 >= 0:
            vb = dp[i - 1][j - 1]
        else:
            vb = 0

        dp[i][j] = va - vb
        dp[i][j] %= MOD
print(dp[n][0])