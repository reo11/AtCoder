import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
edges = defaultdict(lambda: set())
visited = [False for _ in range(n + m + 1)]
for i in range(1, n + 1):
    a = int(input())
    s_i = list(map(int, input().split()))
    for c in s_i:
        edges[n + c].add(i)
        edges[i].add(n + c)

# 超頂点を追加する
# BFS
ans = -1
q = deque([])
q.append([0, n + 1])
visited[n + 1] = True

while len(q) > 0:
    cost, current_edge = q.popleft()
    visited[current_edge] = True
    if current_edge == n + m:
        ans = cost // 2 - 1
        break
    for next_edge in edges[current_edge]:
        if visited[next_edge]:
            continue
        q.append([cost + 1, next_edge])
        visited[next_edge] = True
print(ans)
