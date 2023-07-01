import heapq
from collections import defaultdict
from sys import stdin

input = stdin.readline

n, m, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in [0] * m]
ph = [list(map(int, input().split())) for _ in [0] * k]
edges = defaultdict(list)
for a, b in ab:
    edges[a].append([b, 1])
    edges[b].append([a, 1])
for p, h in ph:
    edges[n + 1].append([p, n - h])
    edges[p].append([n + 1, n - h])

# 頂点n+1から距離n以下の点を列挙
ans = []
visited = defaultdict(lambda: False)
q = []
heapq.heapify(q)
heapq.heappush(q, [0, n + 1])

while len(q) > 0:
    cost, edge = heapq.heappop(q)
    visited[edge] = True
    # print(cost, edge)
    if cost <= n:
        ans.append(edge)
    for next_edge, next_cost in edges[edge]:
        if visited[next_edge]:
            continue
        visited[next_edge] = True
        heapq.heappush(q, [cost + next_cost, next_edge])

ans = list(set(ans) - set([n + 1]))
ans = sorted(ans)
print(len(ans))
print(*ans, sep=" ")
