n, m, x = map(int, input().split())
ca = [list(map(int, input().split())) for i in range(n)]
INF = 10**12


def calc_cost(l):
    ret = 0
    rikai = [0 for _ in range(m)]
    for i in range(len(l)):
        c = l[i][0]
        ret += c
        a = l[i][1:]
        for j in range(m):
            rikai[j] += a[j]

    for i in range(m):
        if rikai[i] < x:
            ret = INF
    return ret


ans = INF
for i in range(2**n):
    l = []
    for j in range(n):
        if i >> j & 1:
            l.append(ca[j])
    ans = min(ans, calc_cost(l))
if ans == INF:
    print(-1)
else:
    print(ans)
