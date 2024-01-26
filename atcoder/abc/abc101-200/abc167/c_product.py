from itertools import product

n, m, x = map(int, input().split())
ca = [list(map(int, input().split())) for i in range(n)]
INF = 10**12

ans = INF
l = [0, 1]
for v in product(l, repeat=n):
    rikai = [0 for _ in range(m)]
    cost = 0
    for i in range(n):
        if v[i]:
            c = ca[i][0]
            a = ca[i][1:]
            cost += c
            for j in range(m):
                rikai[j] += a[j]
    f = True
    for i in range(m):
        if rikai[i] < x:
            f = False
    if f:
        ans = min(ans, cost)
if ans == INF:
    print(-1)
else:
    print(ans)
