import sys
from collections import defaultdict, deque

input = sys.stdin.readline
sys.setrecursionlimit(20000000)

v, n = map(int, input().split())
es = [[int(x) for x in input().split()] for _ in range(n)]

outs = defaultdict(list)
ins = defaultdict(int)
for v1, v2 in es:
    outs[v1].append(v2)
    ins[v2] += 1

q = deque(v1 for v1 in range(v) if ins[v1] == 0)
res = []
while q:
    v1 = q.popleft()
    res.append(v1)
    for v2 in outs[v1]:
        ins[v2] -= 1
        if ins[v2] == 0:
            q.append(v2)


def dfs(n, l):
    global outs
    for out in outs[n]:
        if out in l:
            if len(l) < v:
                print(len(l))
                for i in sorted(l):
                    print(i)
                exit()
        else:
            dfs(out, l[:] + [out])


if len(res) == v + 1:
    pass
else:
    for i in range(1, v + 1):
        dfs(i, [])
print("-1")
