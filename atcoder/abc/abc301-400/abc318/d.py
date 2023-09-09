import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

from collections import defaultdict
INF = float('inf')

n = int(input())
costs = defaultdict(lambda: defaultdict(lambda: -INF))
for i in range(1, n):
    di = list(map(int, input().split()))
    for j, j_num in enumerate(range(i + 1, n + 1)):
        costs[i][j_num] = di[j]
        costs[j_num][i] = di[j]

def pair_combinations(lst):
    if len(lst) < 2:
        return []
    elif len(lst) == 2:
        return [[lst]]
    else:
        pairs = []
        for i in range(1, len(lst)):
            first = lst[0]
            second = lst[i]
            rest = lst[1:i] + lst[i + 1:]
            for c in pair_combinations(rest):
                pairs.append([[first, second]] + c)
        return pairs

ans = -INF
if n % 2 == 0:
    for pairs in pair_combinations(list(range(1, n + 1))):
        cost = 0
        for p1, p2 in pairs:
            cost += costs[p1][p2]
        ans = max(ans, cost)
else:
    # どれかを使わない
    for i in range(1, n + 1):
        l = list(range(1, n + 1))
        l.pop(i - 1)
        for pairs in pair_combinations(l):
            cost = 0
            for p1, p2 in pairs:
                cost += costs[p1][p2]
            ans = max(ans, cost)
print(ans)
