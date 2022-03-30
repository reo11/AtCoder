# 通せねぇ...
import queue

q = queue.Queue()

h, w = map(int, input().split())

board = [[i for i in list(str(input()))] for i in range(h)]
hist = [[False] * w for i in range(h)]

step = 0
count = 0
next_count = 0

for y in range(h):
    for x in range(w):
        if board[y][x] == "#":
            q.put((y, x))
            count += 1
            hist[y][x] = True

while not q.empty():
    y, x = q.get()
    if 0 <= y - 1 and not hist[y - 1][x]:
        if board[y - 1][x] == ".":
            board[y - 1][x] = "#"
            q.put((y - 1, x))
            hist[y - 1][x] = True
            next_count += 1
    if y + 1 < h and not hist[y + 1][x]:
        if board[y + 1][x] == ".":
            board[y + 1][x] = "#"
            q.put((y + 1, x))
            hist[y + 1][x] = True
            next_count += 1
    if 0 <= x - 1 and not hist[y][x - 1]:
        if board[y][x - 1] == ".":
            board[y][x - 1] = "#"
            q.put((y, x - 1))
            hist[y][x - 1] = True
            next_count += 1
    if x + 1 < w and not hist[y][x + 1]:
        if board[y][x + 1] == ".":
            board[y][x + 1] = "#"
            q.put((y, x + 1))
            hist[y][x + 1] = True
            next_count += 1
    count -= 1
    if count == 0:
        step += 1
        count = next_count
        next_count = 0
print(step - 1)
