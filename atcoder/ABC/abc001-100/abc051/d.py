import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 12
edges = defaultdict(lambda: defaultdict(lambda: INF))
n, m = map(int, input().split())
for i in range(m):
    a, b, c = map(int, input().split())
    edges[a - 1][b - 1] = (c, i)
    edges[b - 1][a - 1] = (c, i)


def dijkstra(s, n, w, cost):
    # 始点sから各頂点への最短距離
    # n:頂点数,　w:辺の数, cost[u][v] : 辺uvのコスト(存在しないときはinf)
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0
    que = [[0, s]]  # (dist, node_num)
    prev = {}
    heapify(que)
    while len(que) > 0:
        u_dist, u = heappop(que)
        # まだ使われてない頂点の中から最小の距離のものを探す
        for v in cost[u].keys():
            alt = d[u] + cost[u][v][0]
            edge_num = cost[u][v][1]
            if d[v] > alt:
                prev[v] = (u, edge_num)
                d[v] = alt
                heappush(que, [alt, v])
    cnt = defaultdict(int)
    for goal in range(s, n):
        if goal == s:
            continue
        u = goal
        while u != s:
            cnt[prev[u][1]] += 1
            u = prev[u][0]
    return cnt


ans = set()
cnt_paths = defaultdict(int)
for start in range(n - 1):
    cnt = dijkstra(start, n, m, edges)
    for k, v in cnt.items():
        cnt_paths[k] += v
    ans = ans | set(cnt_paths.keys())
print(m - len(ans))
