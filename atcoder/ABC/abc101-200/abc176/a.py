from math import ceil
n, x, t = map(int, input().split())

ans = ceil(n / x) * t
print(ans)