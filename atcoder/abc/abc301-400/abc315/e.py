import sys
from collections import defaultdict

import pypyjit

pypyjit.set_param("max_unroll_recursion=-1")
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n = int(input())
cp = []
for _ in range(n):
    cpi = list(map(int, input().split()))
    c = cpi[0]
    if c == 0:
        cp.append([0, []])
    else:
        p = cpi[1:]
        cp.append([c, p])


# 深さ優先しながら埋めてく, 順番も記録しておく
ans = []
set_ans = set()
visited = defaultdict(lambda: False)


def dfs(i):
    if visited[i]:
        return
    visited[i] = True
    for pi in cp[i - 1][1]:
        if visited[pi]:
            continue
        else:
            dfs(pi)
    if i not in set_ans:
        ans.append(i)
        set_ans.add(i)


dfs(1)
print(*ans[:-1], sep=" ")
