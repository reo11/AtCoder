# pypyだと通らない
# pythonだと通る
import sys

sys.setrecursionlimit(20000000)

h, w = map(int, input().split())

board = [[i for i in list(str(input()))] for i in range(h)]
hist = [[False] * w for i in range(h)]
s_x = 0
s_y = 0
for i in range(h):
    for j in range(w):
        if board[i][j] == "s":
            s_x = j
            s_y = i
            break


def dfs(x, y):
    # 移動先が範囲内かどうか
    if x < 0 or w - 1 < x or y < 0 or h - 1 < y:
        return False
    # 訪れたことがあるか
    if hist[y][x]:
        return False
    # 訪れたことを記録
    hist[y][x] = True
    # 塀かどうか
    if board[y][x] == "#":
        return False
    # ゴールならTrueを返して終わり
    if board[y][x] == "g":
        return True
    if dfs(x + 1, y) or dfs(x - 1, y) or dfs(x, y + 1) or dfs(x, y - 1):
        return True
    return False


if dfs(s_x, s_y):
    print("Yes")
else:
    print("No")
