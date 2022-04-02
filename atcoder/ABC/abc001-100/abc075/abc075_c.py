import sys

sys.setrecursionlimit(20000000)


def dfs(num):
    global visited, edge, has_edge
    for next_num in edge[num]:
        if visited[next_num]:
            continue
        if has_edge[num][next_num]:
            visited[next_num] = 1
            dfs(next_num)


n, m = map(int, input().split())
edge = [[] for _ in range(n + 1)]
has_edge = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
ab = []
for i in range(m):
    a, b = map(int, input().split())
    ab.append([a, b])
    edge[a].append(b)
    edge[b].append(a)
    has_edge[a][b] = 1
    has_edge[b][a] = 1

count = 0
for a, b in ab:
    visited = [0 for _ in range(n + 1)]
    visited[1] = 1
    has_edge[a][b] = 0
    has_edge[b][a] = 0
    dfs(1)
    if sum(visited) != n:
        count += 1
    has_edge[a][b] = 1
    has_edge[b][a] = 1
print(count)
