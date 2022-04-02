from math import sqrt

n, d = map(int, input().split())
xy = []


def dist(x, y):
    return sqrt(x ** 2 + y ** 2)


ans = 0
for _ in range(n):
    x, y = map(int, input().split())
    if dist(x, y) <= d:
        ans += 1
print(ans)
