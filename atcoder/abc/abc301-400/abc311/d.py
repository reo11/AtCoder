import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

from collections import defaultdict

n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]

started_from = [[False for _ in range(m)] for _ in range(n)]
start = (1, 1)
q = deque([start])
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while q:
    x, y = q.popleft()
    if started_from[x][y]:
        continue
    started_from[x][y] = True
    s[x][y] = "!"

    # 4方向に進む
    for dx, dy in dxy:
        for i in range(1, 200):
            nx = x + dx * i
            ny = y + dy * i
            if s[nx][ny] == "#":
                pre_x = x + dx * (i - 1)
                pre_y = y + dy * (i - 1)
                if s[pre_x][pre_y] != "#" and not started_from[pre_x][pre_y]:
                    q.append((pre_x, pre_y))
                break
            elif s[nx][ny] == ".":
                s[nx][ny] = "!"
            if started_from[nx][ny]:
                break

# print(s)
ans = 0
for i in range(n):
    for j in range(m):
        if s[i][j] == "!":
            ans += 1
print(ans)
