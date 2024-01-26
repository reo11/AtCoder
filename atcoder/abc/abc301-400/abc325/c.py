import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
DXY = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

h, w = map(int, input().split())
s = []
process_list = []
for i in range(h):
    si = list(input())
    s.append(si)
    for j in range(w):
        if si[j] == "#":
            process_list.append((i, j))
visited = [[False for _ in range(w)] for _ in range(h)]

ans = 0
for i, j in process_list:
    if visited[i][j]:
        continue
    visited[i][j] = True
    ans += 1
    que = deque([[i, j]])
    while que:
        i, j = que.popleft()
        for dx, dy in DXY:
            if 0 <= i + dx < h and 0 <= j + dy < w:
                if visited[i + dx][j + dy]:
                    continue
                visited[i + dx][j + dy] = True
                if s[i + dx][j + dy] == "#":
                    s[i + dx][j + dy] = "."
                    que.append([i + dx, j + dy])

print(ans)
