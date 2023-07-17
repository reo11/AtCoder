# ダイクストラ
import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush

input = lambda: sys.stdin.readline().rstrip()
INF = float("inf")

n, m = map(int, input().split())
a = [[i for i in list(str(input()))] for i in range(n)]
# それぞれの数字がある座標などをメモ化
memo = defaultdict(lambda: [])
for i in range(n):
    for j, c in enumerate(a[i]):
        # (x, y)
        memo[c].append((j, i))

# パスの作成
route = ["S"] + list(map(str, range(1, 10))) + ["G"]
# 全ての数字が無いといけない
for r in route:
    if len(memo[r]) == 0:
        print(-1)
        exit()


def dijkstra(s, n):
    d = defaultdict(lambda: INF)
    d[f"{s[0]}_{s[1]}"] = 0
    que = [[0, (s[0], s[1]), 0]]
    heapify(que)
    while len(que) > 0:
        dist, (u_x, u_y), u = heappop(que)
        if u == 10:
            print(dist)
            exit()
            break
        v = u + 1
        for v_x, v_y in memo[route[v]]:
            alt = dist + abs(v_x - u_x) + abs(v_y - u_y)
            if d[f"{v_x}_{v_y}"] > alt:
                d[f"{v_x}_{v_y}"] = alt
                heappush(que, (alt, (v_x, v_y), v))
    return d


start = memo["S"][0]
d = dijkstra((start[0], start[1]), n * m)
