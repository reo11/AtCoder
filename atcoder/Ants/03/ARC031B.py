# 全てのマスについて埋め立てを行い、繋がってるか確かめる
# 全てのマス 10 * 10 = 100
# 再帰の深さ 4**10?

init_board = [[i for i in list(str(input()))] for i in range(10)]
board = [x[:] for x in init_board]
hist = [[False] * 10 for _ in range(10)]
count = 0
count_o = 0
for row in board:
    for i in row:
        if i == "o":
            count_o += 1


def dfs(x, y):
    if not (0 <= x <= 9) or not (0 <= y <= 9):
        return 0
    if hist[y][x]:
        return 0
    hist[y][x] = True
    if board[y][x] == "x":
        return 0
    global count
    if board[y][x] == "o":
        count += 1
    (dfs(x + 1, y), dfs(x - 1, y), dfs(x, y + 1), dfs(x, y - 1))


ans = False
for i in range(10):
    for j in range(10):
        count = 0
        if init_board[i][j] == "x":
            board = [x[:] for x in init_board]
            hist = [[False] * 10 for _ in range(10)]
            board[i][j] = "o"
            dfs(j, i)
            if count == count_o + 1:
                ans = True
        else:
            continue
        if ans:
            break
    if ans:
        break

if ans:
    print("YES")
else:
    print("NO")
