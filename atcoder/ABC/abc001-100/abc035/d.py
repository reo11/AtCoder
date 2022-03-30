import sys
from collections import defaultdict
from heapq import heappush, heappop, heapify
input = sys.stdin.buffer.readline

n, m, t = map(int, input().split())
A = list(map(int, input().split()))
abc = [list(map(int, input().split())) for _ in range(m)]
edges = defaultdict(lambda: defaultdict(lambda: 10**10))
for i in range(m):
    a, b, c = abc[i]
    a -= 1
    b -= 1
    edges[a][b] = c

# 行き：ダイクストラで最短距離を求める
# 帰り：
# 各都市に滞在できる時間から利益を計算する

def dijkstra(s, n, w, cost, create_path=False, goal=None):
    #始点sから各頂点への最短距離
    #n:頂点数,　w:辺の数, cost[u][v] : 辺uvのコスト(存在しないときはinf)
    d = [float("inf")] * n
    used = [False] * n
    d[0] = 0
    que = [[0, 0]] # (dist, node_num)
    if create_path:
        prev = {}
    heapify(que)
    while len(que) > 0:
        u_dist, u = heappop(que)
        #まだ使われてない頂点の中から最小の距離のものを探す
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

d1 = dijkstra(0, n, m, edges)

edges = defaultdict(lambda: defaultdict(lambda: 10**10))
for i in range(m):
    a, b, c = abc[i]
    a -= 1
    b -= 1
    edges[b][a] = c

d2 = dijkstra(0, n, m, edges)

ans = 0
for i in range(n):
    add = (t - d1[i] - d2[i]) * A[i]
    ans = max(ans, add)

print(ans)