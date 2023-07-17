import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
INF = 10 ** 9
d = defaultdict(lambda: defaultdict(lambda: -INF))

n = int(input())
for i in range(1, n):
    a = list(map(int, input().split()))
    for idx, v in enumerate(a, start=i + 1):
        d[i][idx] = v
        d[idx][i] = v


def check(group):
    res = 0
    for p1 in group:
        for p2 in group:
            if p1 == p2:
                continue
            res += d[p1][p2]
    return res // 2


def dfs(groups, depth):
    if depth == n + 1:
        res = 0
        for g in groups:
            res += check(g)
        return res
    else:
        return max(
            dfs([groups[0] + [depth], groups[1], groups[2]], depth + 1),
            dfs([groups[0], groups[1] + [depth], groups[2]], depth + 1),
            dfs([groups[0], groups[1], groups[2] + [depth]], depth + 1),
        )


print(dfs([[], [], []], 1))
