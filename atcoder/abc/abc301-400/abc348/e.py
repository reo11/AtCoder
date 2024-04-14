import sys
import pypyjit
from collections import defaultdict
pypyjit.set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n = int(input())
ab = []
edges = defaultdict(lambda: [])
for _ in range(n - 1):
    a, b = map(int, input().split())
    ab.append((a, b))
    edges[a].append(b)
    edges[b].append(a)
c = list(map(int, input().split()))

# 全方位木DP?
# ある頂点を根としたときの和を求める

dp = [0 for _ in range(n + 1)]
# 吸い上げ
def dfs(v):
    res = 0
    for u in edges[v]:
        res += dfs(u, v)
    return res



