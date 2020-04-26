import sys
from collections import defaultdict
from math import ceil
input = sys.stdin.readline

INF = 10**12
n, m, s = map(int, input().split())
edges = defaultdict(lambda: defaultdict(lambda: [INF, INF]))
cd = []

for i in range(m):
    u, v, a, b = map(int, input().split())
    edges[u-1][v-1] = [a, b]
    edges[v-1][u-1] = [a, b]

for i in range(n):
    c, d = map(int, input().split())
    cd.append([c, d])

# dfsで今まで訪れた箇所をsetで持っておく
# 次に行く場所がそこにあれば行かない
# 経路上の換金できる最小の時間も持っておく
def dfs(cur_num, goal, route_set, time_trade, cost, silver):
    if cur_num == goal:
        return cost, time_trade, silver
    cnt = 0
    res = INF
    final_time_trade = []
    final_silver = -INF
    for next_num in edges[cur_num].keys():
        if next_num in route_set:
            continue
        cnt += 1
        tmp_cost = edges[cur_num][next_num][1]
        tmp_s = -edges[cur_num][next_num][0]
        if silver + tmp_s < 0:
            # 銀が足りない場合の処理
            min_time = [INF, 0]
            for c, d in time_trade:
                times = ceil(-(silver + tmp_s) / c)
                if times * d < min_time[0] or (times * d == min_time[0] and times*c > min_time[1]):
                    min_time = [times*d, times*c]
            tmp_cost += min_time[0]
            tmp_s += min_time[1]
        ret = dfs(next_num, goal, route_set | {next_num}, time_trade + [cd[next_num]], cost + tmp_cost, silver + tmp_s)
        if ret[0] < res:
            res = ret[0]
            final_time_trade = ret[1]
            final_silver = ret[2]

    if cnt == 0:
        return INF, [], -INF
    else:
        return res, final_time_trade, final_silver

plus_costs = [(0, [cd[0], s])]
for i in range(1, n):
    plus_costs.append(dfs(0, i, set(), [cd[0]],0 , s))

for i in range(1, n):
    ans = plus_costs[i][0]
    for j in range(1, n):
        for k in range(1, n):
            # j経由でiまで行く
            tmp_s = plus_costs[j][2]
            ret = dfs(j, k, set(), plus_costs[j][1], plus_costs[j][0], tmp_s)
            tmp_ans = ret[0]
            tmp_s = ret[2]
            ret2 = dfs(k, i, set(), ret[1], ret[0], tmp_s)
            tmp_ans = ret2[0]
            ans = min(ans, tmp_ans)
    print(ans)