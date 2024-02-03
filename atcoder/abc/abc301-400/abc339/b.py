h, w, n = map(int, input().split())

board = [["." for _ in range(w)] for _ in range(h)]

dxy = [[0, -1], [1, 0], [0, 1], [-1, 0]]

pos = [0, 0]
status = 0
for i in range(n):
    if board[pos[1]][pos[0]] == ".":
        board[pos[1]][pos[0]] = "#"
        status = (status + 1) % 4
    else:
        board[pos[1]][pos[0]] = "."
        status = (status - 1) % 4
    next_x = pos[0] + dxy[status][0]
    next_y = pos[1] + dxy[status][1]
    pos = [next_x % w, next_y % h]
    # display_board(board)

ans = []
for i in range(h):
    ans.append("".join(board[i]))
print("\n".join(ans))