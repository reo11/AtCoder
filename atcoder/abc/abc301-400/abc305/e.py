import heapq
import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

MAX_N = 3 * 10**5

n, m, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in [0] * m]
ph = [list(map(int, input().split())) for _ in [0] * k]
edges = defaultdict(list)
for a, b in ab:
    edges[a].append([b, 1])
    edges[b].append([a, 1])
for p, h in ph:
    edges[n + 1].append([p, MAX_N - h])

# 頂点n+1から距離n以下の点を列挙
ans = set()
visited = defaultdict(lambda: False)
visited_count = 0
min_costs = defaultdict(lambda: float("inf"))
q = []
heapq.heapify(q)
heapq.heappush(q, (0, n + 1))

while q:
    # print(q)
    cost, edge = heapq.heappop(q)
    visited[edge] = True
    min_costs[edge] = min(min_costs[edge], cost)
    # print(cost, edge)
    if cost <= MAX_N and edge not in ans:
        ans.add(edge)
    else:
        continue
    for next_edge, next_cost in edges[edge]:
        if visited[next_edge]:
            continue
        if cost + next_cost > MAX_N:
            continue
        if cost + next_cost >= min_costs[next_edge]:
            continue
        else:
            min_costs[next_edge] = cost + next_cost
            heapq.heappush(q, (cost + next_cost, next_edge))

ans = list(set(ans) - set([n + 1]))
ans = sorted(ans)
print(len(ans))
print(*ans, sep=" ")
