import sys

sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
node = [[] for _ in range(n)]
node_num = [[] for _ in range(n)]
u = [0] * m
v = [0] * m
for i in range(m):
    u, v = map(int, input().split())
    node[u - 1].append(v - 1)
    node[v - 1].append(u - 1)
s, t = map(int, input().split())


def dfs(t, num):
    t += 1
    t %= 4
    if t in node_num[num]:
        return
    else:
        node_num.append(t)
    for n in node[num]:
        dfs(t, n)


dfs(0, t)

if 0 in node_num:
    print("true")
else:
    print("false")
