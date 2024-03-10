from heapq import heappop, heappush, heapify
from collections import defaultdict

n = int(input())
p = []
for _ in range(n):
    p.append(list(map(int, input().split())))
r = []
for _ in range(n):
    r.append(list(map(int, input().split())))
d = []
for _ in range(n - 1):
    d.append(list(map(int, input().split())))

# それまで通ったルートのうち最も金銭効率が良いものを記録しながらdp?的なことをする

min_cost = defaultdict(lambda: defaultdict(lambda: (float("inf"), 0)))
queue = [(0, 0, 0, 0, 0)] # (cost, i, j, 現在の所持金, 通ったルートのうち最も大きいPij)
min_cost[0][0] = (0, 0)
heapify(queue)

while queue:
    total_cost, i, j, money, max_p = heappop(queue)
    if min_cost[i][j][0] < total_cost and max_p <= min_cost[i][j][1]:
        # すでに最小コストが更新されている
        continue
    min_cost[i][j] = (total_cost, max_p)
    max_p = max(max_p, p[i][j])
    if i == n - 1 and j == n - 1:
        print(total_cost)
        exit()

    for pattern in ["right", "down"]:
        # 右移動
        if pattern == "right" and j < n - 1:
            money_cost = r[i][j]
        elif pattern == "down" and i < n - 1:
            money_cost = d[i][j]
        else:
            continue
        cost = 0
        if money < money_cost:
            # 働く
            need = (money_cost - money)
            cost += need // max_p
            if need % max_p > 0:
                cost += 1

        new_total_cost = total_cost + cost + 1
        new_money = (money - money_cost) + (cost * max_p)
        if pattern == "right":
            if new_total_cost < min_cost[i][j + 1][0] or max_p > min_cost[i][j + 1][1]:
                heappush(queue, (new_total_cost, i, j + 1, new_money, max_p))
        elif pattern == "down":
            if new_total_cost < min_cost[i + 1][j][0] or max_p > min_cost[i + 1][j][1]:
                heappush(queue, (new_total_cost, i + 1, j, new_money, max_p))
