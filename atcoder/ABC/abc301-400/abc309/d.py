import sys
from collections import deque, defaultdict
input = lambda: sys.stdin.readline().rstrip()

n1, n2, m = map(int, input().split())
ab = []
edges = defaultdict(lambda: [])

for _ in [0]*m:
    a, b = map(int, input().split())
    ab.append((a, b))
for a, b in ab:
    edges[a].append(b)
    edges[b].append(a)


# bfsで1からとn1+n2からの距離を求めて、その最大値の和+1が答え

start = 1
dist = [float("inf")] * (n1 + n2 + 1)
dist[start] = 0
q = deque([[start, 0]])
visited = defaultdict(lambda: False)
while q:
    # print(q)
    current_node, cost = q.popleft()
    visited[current_node] = True
    for next_node in edges[current_node]:
        if visited[next_node]:
            continue
        if dist[next_node] > dist[current_node] + 1:
            dist[next_node] = dist[current_node] + 1
            visited[next_node] = True
            q.append([next_node, cost + 1])

start = n1 + n2
dist[start] = 0
q = deque([[start, 0]])
while q:
    # print(q)
    current_node, cost = q.popleft()
    visited[current_node] = True
    for next_node in edges[current_node]:
        if visited[next_node]:
            continue
        if dist[next_node] > dist[current_node] + 1:
            dist[next_node] = dist[current_node] + 1
            visited[next_node] = True
            q.append([next_node, cost + 1])

count = [0, 0]
for i in range(1, n1 + 1):
    count[0] = max(count[0], dist[i])
for i in range(n1 + 1, n1 + n2 + 1):
    count[1] = max(count[1], dist[i])
print(sum(count) + 1)


