def traveling_salesman_dp(positions):
    INF = float("inf")
    def cost(pos1, pos2):
        x1, y1, z1 = pos1
        x2, y2, z2 = pos2
        return abs(x1 - x2) + abs(y1 - y2) + max(0, z2 - z1)

    # bit_dp
    n = len(positions)
    dp = [[INF] * n for _ in range(1 << n)]
    dp[0][0] = 0
    for i in range(1 << n):
        for j in range(n):
            for k in range(n):
                if i & (1 << k) == 0:
                    dp[i | (1 << k)][k] = min(dp[i | (1 << k)][k], dp[i][j] + cost(positions[j], positions[k]))
    return dp[-1][0]