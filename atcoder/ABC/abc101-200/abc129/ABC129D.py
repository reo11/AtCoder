h, w = map(int, input().split())

s = [input() for i in range(h)]

board_w = [[0 for _ in range(w)] for _ in range(h)]
board_h = [[0 for _ in range(w)] for _ in range(h)]

# 右、左、上、下の順に走査
for i in range(h):
    cnt_continue = 0
    for j in range(w):
        if s[i][j] == "#":
            cnt_continue = 0
        else:
            cnt_continue += 1
            board_w[i][j] = cnt_continue

    for j in reversed(range(w - 1)):
        if board_w[i][j] == 0:
            continue
        board_w[i][j] = max(board_w[i][j], board_w[i][j + 1])

for i in range(w):
    cnt_continue = 0
    for j in range(h):
        if s[j][i] == "#":
            cnt_continue = 0
        else:
            cnt_continue += 1
            board_h[j][i] = cnt_continue

    for j in reversed(range(h - 1)):
        if board_h[j][i] == 0:
            continue
        board_h[j][i] = max(board_h[j][i], board_h[j + 1][i])


ans = 0

for i in range(h):
    for j in range(w):
        v = board_w[i][j] + board_h[i][j] - 1
        ans = max(ans, v)

print(ans)
