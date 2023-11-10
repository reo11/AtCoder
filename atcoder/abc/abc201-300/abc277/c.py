from collections import deque, defaultdict
n = int(input())
ab = []
path = defaultdict(lambda: [])
for _ in range(n):
    a, b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)


queue = deque([1])
visited = defaultdict(lambda: False)
ans = 1
while queue:
    v = queue.popleft()
    ans = max(ans, v)
    if visited[v]:
        continue
    visited[v] = True
    for nv in path[v]:
        if visited[nv]:
            continue
        queue.append(nv)

print(ans)
