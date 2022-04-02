import queue

q = queue.Queue()

r, c = map(int, input().split())
sy, sx = map(int, input().split())
sy -= 1
sx -= 1
gy, gx = map(int, input().split())
gy -= 1
gx -= 1

board = [[i for i in list(str(input()))] for i in range(r)]
hist = [[False] * c for i in range(r)]

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
        ans = step - 1
        break
    for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if not (0 <= x + i <= c - 1) or not (0 <= y + j <= r - 1):
            continue
        if board[y + j][x + i] == "#":
            continue
        if hist[y + j][x + i]:
            continue
        hist[y + j][x + i] = True
        q.put((x + i, y + j))
        next_count += 1
print(ans)
