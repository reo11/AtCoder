import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
edges = defaultdict(lambda: [])

for i in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

k = int(input())
pd = []
for i in range(k):
    p, d = map(int, input().split())
    pd.append([p, d])

# 最短距離メモ
dist_list = defaultdict(lambda: defaultdict(lambda: []))

def bfs(n, start):
    visited = [False] * n
    visited[start] = True
    dist = [float('inf')] * n

    dist[start] = 0
    dist_list[start][0].append(start)
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in edges[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[node] + 1
                dist_list[start][dist[node] + 1].append(neighbor)
                queue.append(neighbor)

for i in range(1, n + 1):
    # i からjまでの最短
    bfs(n + 1, i)

# 1回白で塗って、2回目で正しいかチェックする
colors = defaultdict(lambda: 1)
for i in range(1, n + 1):
    colors[i] = 1

for i in range(k):
    p = pd[i][0]
    d = pd[i][1]
    # 処理の数はN以下
    for dist in range(d):
        for node in dist_list[p][dist]:
            colors[node] = 0

flag = True
for i in range(k):
    p = pd[i][0]
    d = pd[i][1]
    c = set()
    for node in dist_list[p][d]:
        c.add(colors[node])
    if 1 not in c:
        flag = False

if flag:
    print("Yes")
    print(*[str(x[1]) for x in sorted(colors.items())], sep="")
else:
    print("No")