import sys
from math import sqrt
input = lambda: sys.stdin.readline().rstrip()

n, d = map(int, input().split())

ans = 0

def dist(x, y):
    return sqrt(x**2 + y**2)

for _ in range(n):
    x, y = map(int, input().split())
    if dist(x, y) <= d:
        ans += 1

print(ans)