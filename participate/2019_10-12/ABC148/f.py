import sys
import queue
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(20000000)

ans = 0
n, u, v = map(int, input().split())
u -= 1; v -= 1
ab = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    ab[a-1].append(b-1)
    ab[b-1].append(a-1)

path_u = [0] * n
path_v = [0] * n

# u
checked = [False] * n
checked[u] = True
q = queue.Queue()
q.put((u, 0))
while not q.empty():
    cur, count = q.get()
    path_u[cur] = count
    for i in ab[cur]:
        if not checked[i]:
            q.put((i, count+1))
            checked[i] = True

# v
checked = [False] * n
checked[v] = True
q = queue.Queue()
q.put((v, 0))
while not q.empty():
    cur, count = q.get()
    path_v[cur] = count
    for i in ab[cur]:
        if not checked[i]:
            q.put((i, count+1))
            checked[i] = True

ans = 0
for u_, v_ in zip(path_u, path_v):
    if u_ < v_:
        ans = max(ans, v_ - 1)
# print(path_u, path_v)
print(ans)
