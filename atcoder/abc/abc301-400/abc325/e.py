import heapq
from collections import defaultdict
INF = float('inf')
n, a, b, c = map(int, input().split())
d = []

for i in range(n):
    di = list(map(int, input().split()))
    d.append(di)

from_one = [INF for _ in range(n)]
from_n = [INF for _ in range(n)]
# dijkstra(s, n) s:始点, n:頂点数
# 1からiまでの最短距離をfrom_one[i]に格納
# nからiまでの最短距離をfrom_n[i]に格納

que = [[0, 0]]
visited = defaultdict(lambda: False)
costs = [INF for _ in range(n)]
while que:
    cost, v = heapq.heappop(que)
    if visited[v]:
        continue
    visited[v] = True
    from_one[v] = min(from_one[v], cost)
    for w in range(n):
        if v == w:
            continue
        if visited[w]:
            continue
        if costs[w] < cost + d[v][w] * a:
            continue
        costs[w] = min(costs[w], cost + d[v][w] * a)
        heapq.heappush(que, [cost + d[v][w] * a, w])

que = [[0, n-1]]
visited = defaultdict(lambda: False)
costs = [INF for _ in range(n)]
while que:
    cost, v = heapq.heappop(que)
    if visited[v]:
        continue
    visited[v] = True
    from_n[v] = min(from_n[v], cost)
    for w in range(n):
        if v == w:
            continue
        if visited[w]:
            continue
        if costs[w] < cost + d[v][w] * a:
            continue
        costs[w] = min(costs[w], cost + d[v][w] * a)
        heapq.heappush(que, [cost + (d[v][w] * b + c), w])
ans = INF

for i in range(n):
    ans = min(ans, from_one[i] + from_n[i])
print(ans)