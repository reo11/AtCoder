from math import sqrt

INF = float("inf")

n, k = map(int, input().split())
sx, sy = map(int, input().split())
s = (sx, sy)
xy = []


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


for _ in range(n):
    x, y = map(int, input().split())
    xy.append((x, y))


dp = [INF] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for j in range(k):
        if i - j < 0:
            break
        dp[i] = min(
            dp[i],
            dp[i - j - 1]
            + dist(xy[i - j - 1][0], xy[i - j - 1][1], xy[i - 1][0], xy[i - 1][1]),
        )
