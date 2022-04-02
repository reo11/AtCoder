import sys

input = sys.stdin.buffer.readline
sys.setrecursionlimit(20000000)
from collections import defaultdict

n = int(input())

abc = []
edges = defaultdict(lambda: [])
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])

q, k = map(int, input().split())

# k からの距離を求める
dist = [-1 for _ in range(n + 1)]
is_checked = [False for _ in range(n + 1)]


def dfs(num, cur_dist):
    global dist, is_checked
    for next_num, d in edges[num]:
        if not is_checked[next_num]:
            is_checked[next_num] = True
            dist[next_num] = cur_dist + d
            dfs(next_num, cur_dist + d)


dist[k] = 0
is_checked[k] = True
dfs(k, 0)

ans = []
for _ in range(q):
    x, y = map(int, input().split())
    ans.append(str(dist[x] + dist[y]))
print("\n".join(ans))
