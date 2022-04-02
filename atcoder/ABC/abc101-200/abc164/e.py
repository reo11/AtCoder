import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush

input = sys.stdin.readline

INF = 10 ** 19
n, m, s = map(int, input().split())
edges = defaultdict(lambda: defaultdict(lambda: [INF, INF]))
cd = []
max_a = 0

for i in range(m):
    u, v, a, b = map(int, input().split())
    max_a = max(max_a, a)
    edges[u - 1][v - 1] = [a, b]
    edges[v - 1][u - 1] = [a, b]

for i in range(n):
    c, d = map(int, input().split())
    cd.append([c, d])

# 解答ACする
# Dijakstraの状態を(頂点、所持している銀貨の枚数, cost)で持つ
SIZE = max_a * n + 1
# SIZE = 2550
if s > SIZE:
    s = SIZE
nodes = [[INF for _ in range(SIZE + 1)] for _ in range(n)]
nodes[0][s] = 0


def dijakstra():
    goals = set({0})
    que = [(0, 0, s)]
    heapify(que)
    while 10 ** 6 > len(que) > 0:
        if len(goals) >= n:
            break
        cost, num, silver = heappop(que)
        if num not in goals:
            goals.add(num)
        c, d = cd[num]
        s_tmp = min(SIZE, silver + c)
        if silver < SIZE and s_tmp != silver:
            if nodes[num][s_tmp] > cost + d:
                heappush(que, (cost + d, num, s_tmp))
                nodes[num][s_tmp] = min(nodes[num][s_tmp], cost + d)
        for v in edges[num].keys():
            a, b = edges[num][v]
            if silver >= a:
                if nodes[v][silver - a] > cost + b:
                    heappush(que, (cost + b, v, silver - a))
                    nodes[v][silver - a] = min(nodes[v][silver - a], cost + b)


dijakstra()
for i in range(1, n):
    print(min(nodes[i]))
