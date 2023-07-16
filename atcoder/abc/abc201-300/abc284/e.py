import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
MAX = 10 ** 6

n, m = map(int, input().split())
edges = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

# DFS
ans = 0


def dfs(current_path, current_edge):
    global ans
    # print(current_path)
    ans += 1
    if ans >= MAX:
        print(MAX)
        exit()
    for next_edge in edges[current_edge]:
        if next_edge in current_path:
            continue
        dfs(current_path | {next_edge}, next_edge)


dfs(set([1]), 1)
print(ans)
