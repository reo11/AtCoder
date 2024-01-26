import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n = int(input())
p = list(map(int, input().split()))

parents = defaultdict(lambda: -1)

for i, pi in enumerate(p, start=2):
    parents[i] = pi


def solve(i, depth=0):
    if parents[i] == -1:
        return depth
    else:
        return solve(parents[i]) + 1


print(solve(n))
