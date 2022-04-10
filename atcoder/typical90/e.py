MOD = 10 ** 9 + 7

n, b, k = map(int, input().split())
c = list(map(int, input().split()))

# 桁DP
# dp[上から何桁目][bで割った余り] = 通り数

dp = [[0 for _ in range(b)] for _ in range(n + 1)]
dp[0][0] = 1

for keta_i in range(1, n + 1):
    for c_j in c:
        amari_c = c_j * 10 ** (n + 1 - keta_i) % b
        for amari_j in range(b):
            amari_jc = (amari_j + amari_c) % b
            dp[keta_i][amari_jc] += dp[keta_i - 1][amari_j]
            dp[keta_i][amari_jc] %= MOD
print(dp)
print(dp[n][0])
