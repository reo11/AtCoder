import sys
input = sys.stdin.buffer.readline
from collections import deque

n = int(input())
edges = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

def get_dists(f):
    dists = [0 for _ in range(n)]
    q = deque()
    q.append((f, -1, 0))
    while len(q) > 0:
        num, f_num, dist = q.popleft()
        for node in edges[num]:
            if node == f_num:
                continue
            else:
                dists[node] = dist + 1
                q.append((node, num, dist+1))
    return dists

dist_1 = get_dists(0)
dist_n = get_dists(n-1)

ans = 0
for i in range(n):
    if dist_1[i] <= dist_n[i]:
        ans += 1

fennec = ans
snuke = n - fennec
if fennec > snuke:
    print("Fennec")
else:
    print("Snuke")
