from collections import defaultdict
from math import sqrt

INF = float("inf")


def prim(n, ignore_set, cost):
    mincost = [float("inf")] * n
    used = [False] * n
    mincost[0] = 0
    res = 0

    while True:
        v = -1
        for i in range(n):
            if i in ignore_set:
                continue
            if (not used[i]) and (v == -1 or mincost[i] < mincost[v]):
                v = i
        if v == -1:
            break
        used[v] = True
        res += mincost[v]
        for i in range(n):
            mincost[i] = min(mincost[i], cost[v][i])
    return res


n, m = map(int, input().split())
big_xyc = [tuple(map(int, input().split())) for _ in range(n)]
small_xyc = [tuple(map(int, input().split())) for _ in range(m)]


def dist(inp1, inp2):
    x1, y1, c1 = inp1
    x2, y2, c2 = inp2
    base_dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if c1 == c2:
        return base_dist
    else:
        return 10 * base_dist


cost = defaultdict(lambda: defaultdict(lambda: INF))
for i in range(n):
    xyc_i = big_xyc[i]
    for j in range(n):
        if i == j:
            continue
        xyc_j = big_xyc[j]
        dist_ij = dist(xyc_i, xyc_j)
        cost[i][j] = dist_ij
        cost[j][i] = dist_ij

# 小さい方は全探索
ans = INF
for i in range(2 ** m):
    ignore_set = set()
    for j in range(m):
        if i >> j & 1:
            xyc_j = small_xyc[j]
            for k in range(n + m):
                if k < n:
                    xyc_k = big_xyc[k]
                else:
                    if k - n == j:
                        continue
                    xyc_k = small_xyc[k - n]
                cost[k][n + j] = dist(xyc_j, xyc_k)
                cost[n + j][k] = dist(xyc_j, xyc_k)
        else:
            ignore_set.add(n + j)
            for k in range(n + m):
                cost[k][n + j] = INF
                cost[n + j][k] = INF
        ans = min(ans, prim(n + m, ignore_set, cost))

print(ans)
