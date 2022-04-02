from heapq import heapify, heappop, heappush


def dijkstra(s, n, w, cost, create_path=False, goal=None):
    # 始点sから各頂点への最短距離
    # n:頂点数,　w:辺の数, cost[u][v] : 辺uvのコスト(存在しないときはinf)
    d = [float("inf")] * n
    d[s] = 0
    que = [[0, s]]  # (dist, node_num)
    if create_path:
        prev = {}
    heapify(que)
    while len(que) > 0:
        u_dist, u = heappop(que)
        # まだ使われてない頂点の中から最小の距離のものを探す
        for v in edges[u].keys():
            alt = d[u] + cost[u][v]
            if d[v] > alt:
                if create_path:
                    prev[v] = u
                d[v] = alt
                heappush(que, [alt, v])
    if create_path and goal:
        u = goal
        path = [u]
        while u != s:
            path.append(prev[u])
            u = prev[u]
        return path
    return d
