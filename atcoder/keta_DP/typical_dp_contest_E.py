MOD = 10 ** 9 + 7


def solve(num, mod):
    # 計算量O(Ld*10)
    # O(10,000,000)
    L = len(str(num))
    dp = [[[0 for _ in range(mod)] for _ in range(2)] for _ in range(L + 1)]
    dp[0][0][0] = 1
    for i in range(L):
        D = int(str(num)[i])
        for j in range(2):
            for k in range(mod):
                for d in range(10 if j else D + 1):
                    dp[i + 1][j or (d < D)][k] += dp[i][j][(k - d) % mod]
        print(dp[i + 1][1])

    return (dp[-1][1][0] + dp[-1][0][0]) % MOD


d, n = [int(input()) for _ in range(2)]

print(solve(n, d) - 1)
