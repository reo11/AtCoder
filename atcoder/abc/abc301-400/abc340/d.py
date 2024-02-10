import heapq

INF = float('inf')
n = int(input())

abx = []

for i in range(n - 1):
    a, b, x = map(int, input().split())
    abx.append([a, b, x])

costs = [INF for _ in range(n + 1)]
costs[1] = 0
visited = [False for _ in range(n + 1)]

# ダイクストラ

q = [[0, 1]]

while q:
    cost, y = heapq.heappop(q)
    if visited[y]:
        continue
    visited[y] = True
    if y == n:
        break
    y_idx = y - 1
    a, b, x = abx[y_idx]
    # i + 1
    costs[y + 1] = min(costs[y + 1], costs[y] + a)
    heapq.heappush(q, [costs[y + 1], y + 1])
    costs[x] = min(costs[x], costs[y] + b)
    heapq.heappush(q, [costs[x], x])

print(costs[n])