from collections import defaultdict, deque

h, w = map(int, input().split())
g = [list(input()) for _ in range(h)]
visited = [[False] * w for _ in range(h)]


def out(x, y):
    if x < 0 or x >= w or y < 0 or y >= h:
        return True
    else:
        return False


ans = (-1, -1)
queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    if visited[y][x]:
        break
    visited[y][x] = True
    next_x, next_y = x, y
    if g[y][x] == "U":
        next_x, next_y = x, y - 1
    elif g[y][x] == "D":
        next_x, next_y = x, y + 1
    elif g[y][x] == "L":
        next_x, next_y = x - 1, y
    else:
        next_x, next_y = x + 1, y

    if out(next_x, next_y):
        ans = (x + 1, y + 1)
        break
    queue.append((next_x, next_y))

if ans == (-1, -1):
    print(-1)
else:
    print(ans[1], ans[0])
