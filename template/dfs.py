# pypyだと通らない
# pythonだと通る
import sys
sys.setrecursionlimit(20000000)


class DepthFirsSearch:
    def __init__(self, h, w, board, s_xy, g_xy):
        self.h, self.w = h, w
        self.board = board
        self.hist = [[False] * w for i in range(h)]
        self.s_xy = s_xy
        self.g_xy = g_xy
    def dfs(self, x, y, wall = "#"):
        # 移動先が範囲内かどうか
        if x < 0 or self.w - 1 < x or y < 0 or self.h - 1 < y:
            return False
        # 訪れたことがあるか
        if self.hist[y][x]:
            return False
        # 訪れたことを記録
        self.hist[y][x] = True
        # 塀かどうか
        if self.board[y][x] == wall:
            return False
        # ゴールならTrueを返して終わり
        if (x, y) == self.g_xy:
            return True
        if (self.dfs(x + 1, y) or self.dfs(x - 1, y) or self.dfs(x, y + 1) or self.dfs(x, y - 1)):
            return True
        return False

h, w = map(int, input().split())

board = [[i for i in list(str(input()))] for i in range(h)]

s_xy = (0, 0)
g_xy = (0, 0)
for i in range(h):
    for j in range(w):
        if board[i][j] == "s":
            s_xy = (j, i)
        if board[i][j] == "g":
            g_xy = (j, i)

DFS = DepthFirsSearch(h, w, board, s_xy, g_xy)

if DFS.dfs(s_xy[0], s_xy[1]):
    print("Yes")
else:
    print("No")
