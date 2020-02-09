# 桁DP
n = int(input())
k = int(input())

def solve(num, k_):
    # 左から桁DP
    # dp[i-th number][is_max][how many not 0]
    n = len(str(num)) + 1
    dp = [[[0 for _ in range(k_+2)] for _ in range(2)] for _ in range(n)]
    dp[0][0][0] = 1

    for i in range(n-1):
        D = int(str(num)[i])
        for j in range(2):
            for k in range(k_+1):
                for d in range(10 if j else D+1):
                    if d == 0:
                        dp[i+1][j or (d < D)][k] += dp[i][j][k]
                    else:
                        dp[i+1][j or (d < D)][k+1] += dp[i][j][k]
    return dp[-1][0][k_] + dp[-1][1][k_]

print(solve(n, k))