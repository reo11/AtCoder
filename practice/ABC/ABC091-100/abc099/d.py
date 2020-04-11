from itertools import permutations
from collections import defaultdict
n, C = map(int, input().split())
d = [list(map(int, input().split())) for i in range(C)]
c = [list(map(int, input().split())) for i in range(n)]

counts = [defaultdict(int) for _ in range(3)]
for i in range(n):
    for j in range(n):
        counts[(i+j+2) % 3][c[i][j]-1] += 1

def calc_cost(dic, color):
    cost = 0
    for k, v in dic.items():
        cost += d[k][color] * v
    return cost

INF = 10**9
cost = INF
for colors in permutations(range(C), 3):
    tmp_cost = 0
    for i in range(3):
        tmp_cost += calc_cost(counts[i], colors[i])
    cost = min(cost, tmp_cost)
print(cost)