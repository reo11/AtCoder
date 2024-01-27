INF = float('inf')
n, m = map(int, input().split())
G = [[INF] * n for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    G[u - 1][v - 1] = w

def warshall_floyd(n, d):
    # 空間計算量: O(n^2)
    # 時間計算量: O(n^3)
    # よって、n <= 10^2程度が限界
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

G = warshall_floyd(n, G)

def solve_tsp_dp(n, g):
    # n: 頂点数
    # m: 辺数
    # g: グラフ
    # https://qiita.com/Ll_e_ki/items/fa475f5bb224ada9be97
    dp = [[INF] * n for _ in range(2**n)]
    # どこスタートでも良い
    for i in range(n):
        dp[2**i][i] = 0
    for S in range(2**n):
        for v in range(n):
            for u in range(n):
                if not (S >> u) & 1 and S != 0: # ①
                    continue
                if (S >> v) & 1 == 0:
                    if dp[S][u] + g[u][v] < dp[S | (1 << v)][v]:
                        dp[S | (1 << v)][v] = dp[S][u] + g[u][v]
    return min(dp[2**n - 1])

ans = solve_tsp_dp(n, G)
if ans == INF:
    print("No")
else:
    print(ans)
