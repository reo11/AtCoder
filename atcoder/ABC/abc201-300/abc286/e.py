import sys
from collections import defaultdict
from heapq import heapify, heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
s = [list(input()) for _ in range(n)]
edges = defaultdict(lambda: [])
for i in range(n):
    for j in range(n):
        if s[i][j] == "Y":
            edges[i].append(j)
q = int(input())
uv = [list(map(int, input().split())) for _ in range(q)]
uv = [[x - 1, y - 1] for x, y in uv]

# ダイクストラで距離と価値を埋めていく

def dijkstra(x):
    # dictで返す
    res = defaultdict(lambda: [float("inf"), 0, -1])
    hq = [[0, a[x], x]]
    heapify(hq)
    while hq:
        dist, value, current_num = heappop(hq)
        # 良い場合は更新
        if res[current_num][0] < dist:
            continue
        if res[current_num][0] == dist and res[current_num][1] >= value:
            continue
        res[current_num] = [dist, value]

        for next_num in edges[current_num]:
            # 既に登録されているものより悪い場合は入れない
            if res[next_num][0] < dist + 1:
                continue
            if res[next_num][0] == dist + 1 and res[next_num][1] >= value + a[next_num]:
                continue
            heappush(hq, [dist + 1, value + a[next_num], next_num])
    return res

ans = dict()
for i in range(n):
    ans[i] = dijkstra(i)

for u, v in uv:
    if ans[u][v][0] == float("inf"):
        print("Impossible")
    else:
        print(f"{ans[u][v][0]} {ans[u][v][1]}")