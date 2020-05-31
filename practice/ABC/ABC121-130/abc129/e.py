# 桁DP
# 二進数, 2進数
l = list(map(int, list(input())))
n = len(l) + 1
MOD = 10**9+7
dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]
dp1[0] = 1
for i in range(1, n):
    if l[i-1] == 1:
        dp1[i] = dp1[i-1] * 2
        dp2[i] = dp1[i-1] + dp2[i-1] * 3
    else:
        dp1[i] = dp1[i-1]
        dp2[i] = dp2[i-1] * 3
    dp1[i] %= MOD
    dp2[i] %= MOD
print((dp1[-1] + dp2[-1]) % MOD)