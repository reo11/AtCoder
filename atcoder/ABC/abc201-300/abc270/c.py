from collections import deque
from collections import defaultdict
import sys
sys.setrecursionlimit(10000000)

input = sys.stdin.readline
n, x, y = map(int, input().split())

edges = defaultdict(lambda: [])
visited = [False for _ in range(n+1)]

for i in range(n-1):
    u_i, v_i = map(int, input().split())
    edges[u_i].append(v_i)
    edges[v_i].append(u_i)


q = deque()
q.append(x)

def dfs(current_edge, pre_edge):
    if current_edge == y:
        return True
    for next_edge in edges[current_edge]:
        if next_edge == pre_edge:
            continue
        q.append(next_edge)
        if dfs(next_edge, current_edge):
            return True
        q.pop()
    return False

dfs(x, -1)
print(*q)