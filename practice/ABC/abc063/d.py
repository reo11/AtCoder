from math import ceil
n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]

def can_beet(t):
    ans = False
    d = 0
    for v in h:
        sub = v - (b * t)
        if sub > 0:
            d += ceil(sub / (a - b))
    if d <= t:
        ans = True
    return ans

l = -1
r = 10 ** 9 + 1
while r - l > 1:
    mid = (r + l) // 2
    if can_beet(mid):
        r = mid
    else:
        l = mid
print(r)