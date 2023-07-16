import heapq
import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()

h, w, t = map(int, input().split())
a = [list(input()) for _ in range(h)]

s = [0, 0]
g = [0, 0]
o = []
for i in range(h):
    for j in range(w):
        if a[i][j] == "S":
            s = [i, j]
        if a[i][j] == "G":
            g = [i, j]
        if a[i][j] == "o":
            o.append([i, j])
target_list = [s] + o + [g]
target_list = [[i, x, y] for i, (x, y) in enumerate(target_list)]
dist = [[float("inf")] * len(target_list) for _ in range(len(target_list))]
# 幅優先探索で頂点間の距離を求める
for i, start_x, start_y in target_list:
    count = 0
    d = [[float("inf")] * w for _ in range(h)]
    q = [[0, start_x, start_y]]
    q = deque(q)
    while len(q) > 0:
        cost, current_i, current_j = q.popleft()
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            next_i = current_i + di
            next_j = current_j + dj
            if next_i < 0 or next_i >= h or next_j < 0 or next_j >= w:
                continue
            if a[next_i][next_j] == "#" or d[next_i][next_j] != float("inf"):
                continue
            d[next_i][next_j] = cost + 1
            q.append([cost + 1, next_i, next_j])
    for j, end_x, end_y in target_list:
        if i == j:
            continue
        dist[i][j] = d[end_x][end_y]
# print(dist)

if dist[0][-1] > t:
    print(-1)
    exit()

dp = [[float("inf") for _ in range(2 ** (len(o)))] for _ in range(len(o))]
for i in range(len(o)):
    dp[i][1 << i] = dist[0][i + 1]

# bitDP
# o * 2 ** o
ans = -1
for bit in range(2 ** (len(o))):
    bit_cnt = bin(bit).count("1")
    for i in range(len(o)):
        if dp[i][bit] == float("inf"):
            continue
        if dp[i][bit] + dist[i + 1][-1] <= t and bit_cnt > ans:
            ans = bit_cnt
        for j in range(len(o)):
            if dp[j][bit | (1 << j)] > dp[i][bit] + dist[i + 1][j + 1]:
                dp[j][bit | (1 << j)] = dp[i][bit] + dist[i + 1][j + 1]
# print(dp)
# print(dist)
print(ans)
