from math import ceil
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.append(0)
a.append(n + 1)
a.sort()

dist = float("inf")
for i in range(len(a) - 1):
    span = (a[i + 1] - a[i]) - 1
    if span > 0:
        dist = min(dist, span)

ans = 0
for i in range(len(a) - 1):
    span = (a[i + 1] - a[i]) - 1
    if span > 0:
        ans += ceil(span / dist) 
print(ans)