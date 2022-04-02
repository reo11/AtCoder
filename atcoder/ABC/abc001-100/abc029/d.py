n = int(input())
n_str = str(n)
L = len(n_str)

dp = [[[0 for _ in range(L + 1)] for _ in range(2)] for _ in range(L + 1)]
# dp[i桁目][確実にn以下か][1をk個含む] = i桁目までで1をk個含む数
dp[0][0][0] = 1
# dp[0][1][0] = 0
for i in range(L):
    D = int(n_str[i])
    for j in range(2):
        for k in range(i + 1):
            for d in range(10 if j else D + 1):
                dp[i + 1][j or d < D][k + (d == 1)] += dp[i][j][k]


ans = 0
for i in range(1, L + 1):
    ans += dp[L][0][i] * i
    ans += dp[L][1][i] * i

print(ans)
