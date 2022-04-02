import sys
from heapq import heapify, heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

n, m = map(int, input().split())
edges = defaultdict(lambda: defaultdict(lambda: float("inf")))
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1][b - 1] = 1
    edges[b - 1][a - 1] = 1


def dijkstra(s, n, cost):
    d = [float("inf")] * n
    d[s] = 0
    que = [[0, s]]
    prev = {}
    heapify(que)
    while len(que) > 0:
        u_dist, u = heappop(que)
        # まだ使われてない頂点の中から最小の距離のものを探す
        for v in edges[u].keys():
            alt = d[u] + cost[u][v]
            if d[v] > alt:
                prev[v] = u
                d[v] = alt
                heappush(que, [alt, v])
    return d, prev


_, prev = dijkstra(0, n, edges)
ans = []
ans.append("Yes")
for i in range(1, n):
    ans.append(str(prev[i] + 1))
print("\n".join(ans))
