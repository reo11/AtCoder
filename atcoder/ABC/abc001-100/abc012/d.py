n, m = map(int, input().split())

INF = 10 ** 9
edges = [[INF for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b, t = map(int, input().split())
    edges[a - 1][b - 1] = t
    edges[b - 1][a - 1] = t


def dijkstra(s, n, w, cost):
    # 始点sから各頂点への最短距離
    # n:頂点数,　w:辺の数, cost[u][v] : 辺uvのコスト(存在しないときはinf)
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0

    while True:
        v = -1
        # まだ使われてない頂点の中から最小の距離のものを探す
        for i in range(n):
            if (not used[i]) and (v == -1):
                v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
            break
        used[v] = True
        for j in range(n):
            d[j] = min(d[j], d[v] + cost[v][j])
    return d


ans = INF
for i in range(n):
    d = dijkstra(i, n, m, edges)
    ans = min(ans, max(d))
print(ans)
