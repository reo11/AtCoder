INF = float("inf")
n, k = map(int, input().split())
a = list(map(int, input().split()))
xy = []
for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))

def dist(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

dists = [INF for _ in range(n)]
for i in range(n):
    xi, yi = xy[i]
    for ai in a:
        dists[i] = min(dists[i], dist(xi, yi, xy[ai - 1][0], xy[ai - 1][1]))

ans = 0
for di in dists:
    ans = max(ans, di)
print(ans)
