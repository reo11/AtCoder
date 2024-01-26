import sys
from collections import defaultdict

import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
INF = float("inf")

h, w = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(h)]

# 連続して同じところを操作すると元に戻るので、最初だけ4つの選択肢、そのあとは3つの選択肢
# 左上、右上、左下、右下


def is_state_correct(X):
    for i in range(h):
        for j in range(w):
            if X[i][j] != i * w + j + 1:
                return False
    return True


def spin(pattern_num, X):
    # 　左上、右上、左下、右下
    tmp_X = [[0 for _ in range(w)] for _ in range(h)]
    dxy = [[0, 0], [0, 1], [1, 0], [1, 1]]
    x = dxy[pattern_num][0]
    y = dxy[pattern_num][1]
    for i in range(h - 1):
        for j in range(w - 1):
            tmp_X[i + x][j + y] = X[h - 2 - i + x][w - 2 - j + y]
    if y == 0:
        for i in range(h):
            tmp_X[i][w - 1] = X[i][w - 1]
    else:
        for i in range(h):
            tmp_X[i][0] = X[i][0]
    if x == 0:
        for j in range(w):
            tmp_X[h - 1][j] = X[h - 1][j]
    else:
        for j in range(w):
            tmp_X[0][j] = X[0][j]
    return tmp_X


def state_str(X):
    return "_".join(["_".join(map(str, x)) for x in X])


def display(X):
    return "\n".join([" ".join(map(str, x)) for x in X])


visited = defaultdict(lambda: INF)
visited[state_str(s)] = 0

ans = INF


def dfs(X, pre_pattern_num=-1, depth=1):
    for i in range(4):
        if i == pre_pattern_num:
            continue
        tmp_X = spin(i, X)
        state = state_str(tmp_X)
        if visited[state] < depth:
            continue
        visited[state] = depth
        if depth + 1 >= 21:
            continue
        dfs(tmp_X, i, depth + 1)


if is_state_correct(s):
    print(0)
    exit()

dfs(s)
state = "_".join([str(x + 1) for x in range(h * w)])
ans = visited[state]
if ans == INF:
    print(-1)
else:
    print(ans)
