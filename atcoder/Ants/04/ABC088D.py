import queue

q = queue.Queue()

h, w = map(int, input().split())
sx, sy = 0, 0
gx, gy = w - 1, h - 1
board = [[i for i in list(str(input()))] for i in range(h)]
hist = [[False] * w for i in range(h)]

q.put((sx, sy))
step = 0
count = 1
next_count = 1
ans = 0
while not q.empty():
    x, y = q.get()
    count -= 1
    if count == 0:
        step += 1
        count = next_count
        next_count = 0
    if x == gx and y == gy:
        ans = step
        break
    for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if not(0 <= x+i <= w - 1) or not(0 <= y+j <= h - 1):
            continue
        if board[y+j][x+i] == "#":
            continue
        if hist[y+j][x+i]:
            continue
        hist[y+j][x+i] = True
        q.put((x+i, y+j))
        next_count += 1
count_black = 0
for y in range(h):
    for x in range(w):
        if board[y][x] == "#":
            count_black += 1

if ans == 0:
    print("-1")
else:
    print(h * w - ans - count_black)
