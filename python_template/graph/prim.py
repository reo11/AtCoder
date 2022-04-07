# https://juppy.hatenablog.com/entry/2018/11/03/%E8%9F%BB%E6%9C%AC_python_%E6%9C%80%E5%B0%8F%E5%85%A8%E5%9F%9F%E6%9C%A8%E5%95%8F%E9%A1%8C%EF%BC%91%EF%BC%88%E3%83%97%E3%83%AA%E3%83%A0%E6%B3%95%EF%BC%89_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0
def prim(n, ignore_set, cost):
    mincost = [float("inf")] * n
    used = [False] * n
    mincost[0] = 0
    res = 0

    while True:
        v = -1
        for i in range(n):
            if i in ignore_set:
                continue
            if (not used[i]) and (v == -1 or mincost[i] < mincost[v]):
                v = i
        if v == -1:
            break
        used[v] = True
        res += mincost[v]
        for i in range(n):
            mincost[i] = min(mincost[i], cost[v][i])
    return res
