import sys
from collections import defaultdict, deque

INF = float("inf")
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

h, w = map(int, input().split())
a = []
enemies = []
start = [-1, -1]
goal = [-1, -1]
enemy_flag = set([">", "v", "<", "^"])
block_flag = set([">", "v", "<", "^", "#"])

for i in range(h):
    ai = list(input())
    for j in range(w):
        if ai[j] in enemy_flag:
            enemies.append([ai[j], i, j])
        elif ai[j] == "S":
            start = [i, j]
        elif ai[j] == "G":
            goal = [i, j]
    a.append(ai)


# 視線を#で埋めた後適当にBFSする
# 視線を#で埋める
# 敵の数が多い時に計算量が多くなりすぎる
# O(HW + E) くらいにしたい
block_list = defaultdict(lambda: set())
for aij, i, j in enemies:
    dxy = [0, 0]
    if aij == "<":
        dxy = [0, -1]
    elif aij == ">":
        dxy = [0, 1]
    elif aij == "^":
        dxy = [-1, 0]
    else:
        dxy = [1, 0]
    block_list[i].add(j)
    while True:
        i += dxy[0]
        j += dxy[1]
        if i < 0 or i >= h or j < 0 or j >= w:
            break
        if a[i][j] in block_flag:
            break
        block_list[i].add(j)

for i, js in block_list.items():
    for j in js:
        a[i][j] = "#"

# BFS O(HW)
visited = defaultdict(lambda: defaultdict(lambda: False))
# cost = defaultdict(lambda: defaultdict(lambda: INF))
que = deque([[0, start]])
visited[start[0]][start[1]] = True
while que:
    # print(que)
    dist, now = que.popleft()
    if now == goal:
        print(dist)
        exit()
    visited[now[0]][now[1]] = True

    i, j = now
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        ni = i + di
        nj = j + dj
        if ni < 0 or ni >= h or nj < 0 or nj >= w:
            continue
        if visited[ni][nj]:
            continue
        if a[ni][nj] == "#":
            continue
        que.append([dist + 1, [ni, nj]])
        visited[ni][nj] = True
# print(a)
print(-1)
