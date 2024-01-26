import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, s, t = map(int, input().split())
uv = []
edges = defaultdict(lambda: [])
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges[u - 1].append(v - 1)
    edges[v - 1].append(u - 1)


ans = [-1 for _ in range(n)]
# 最短経路に含まれるパスを求める
# DFS
path = deque()
q = deque()
q.append([s - 1, 1])
visited = defaultdict(lambda: False)
visited[s - 1] = True
while q:
    v, dist = q.popleft()
    while len(path) >= dist:
        path.pop()
    path.append(v)
    if v == t - 1:
        break
    for v_i in edges[v]:
        if visited[v_i]:
            continue
        q.appendleft([v_i, dist + 1])
        visited[v_i] = True

# 太い幹を起点にそこからの距離を求める
q = deque()
visited = defaultdict(lambda: False)
for v in path:
    ans[v] = 1
    q.append([v, 1])
    visited[v] = True

while q:
    v, dist = q.popleft()
    for v_i in edges[v]:
        if visited[v_i]:
            continue
        ans[v_i] = dist + 1
        q.append([v_i, dist + 1])
        visited[v_i] = True

print(*ans, sep="\n")
