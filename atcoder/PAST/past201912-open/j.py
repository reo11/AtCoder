# 分岐個所を全探索してそこからの3点に対する最短経路を求めれば良さそう
from heapq import heappush, heappop, heapify
from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()
INF = float("inf")
h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
edges = defaultdict(lambda: defaultdict(lambda: float("inf")))
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dijkstra(s):
    d = [[INF for _ in range(w)] for _ in range(h)]
    s_i, s_j = s
    d[s_j][s_i] = 0
    que = [[0, (s_i, s_j)]]
    heapify(que)
    while len(que) > 0:
        u_dist, u = heappop(que)
        u_i, u_j = u
        for dx, dy in dxy:
            v_i = u_i + dx
            v_j = u_j + dy
            if not(0 <= v_i <= w-1 and 0 <= v_j <= h-1):
                continue
            v = (v_i, v_j)
            alt = d[u_j][u_i] + a[v_j][v_i]
            if d[v_j][v_i] > alt:
                d[v_j][v_i] = alt
                heappush(que, [alt, v])
    return d

ans = INF
costs = [[], [], []]
costs[0] = dijkstra((w-1, 0))
costs[1] = dijkstra((0, h-1))
costs[2] = dijkstra((w-1, h-1))
for i in range(w):
    for j in range(h):
        cost = -2 * a[j][i]
        for k in range(3):
            cost += costs[k][j][i]
        ans = min(ans, cost)
print(ans)
