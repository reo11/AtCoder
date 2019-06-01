import sys
from sys import stdin
sys.setrecursionlimit(20000000)

class Solve:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.hist = [[0] * w for i in range(h)]
        self.board = []

    def dfs(self, x, y):
        # 移動先が範囲内かどうか
        if x < 0 or self.w - 1 < x:
            return False
        if y < 0 or self.h - 1 < y:
            return False
        # 塀かどうか
        if self.board[y][x] == "#":
            return False
        # 訪れたことがあるか
        if self.hist[y][x] != 0:
            return False
        # 訪れたことを記録
        self.hist[y][x] = 1
        # ゴールならTrueを返して終わり
        if self.board[y][x] == "g":
            return True
        if (self.dfs(x + 1, y) or self.dfs(x - 1, y) or self.dfs(x, y + 1) or self.dfs(x, y - 1)):
            return True
        return False


h, w = map(int, input().split())
ans = Solve(h, w)
ans.board = [[i for i in list(str(stdin.readline().rstrip()))] for i in range(h)]

s_x = 0
s_y = 0
for i in range(h):
    for j in range(w):
        if ans.board[i][j] == "s":
            s_x = j
            s_y = i
            break
if ans.dfs(s_x, s_y):
    print("Yes")
else:
    print("No")
