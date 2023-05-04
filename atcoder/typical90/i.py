# https://atcoder.jp/contests/typical90/submissions/40437360
import bisect
import cmath
import math

N = int(input())
P = []
for _ in range(N):
    x, y = map(int, input().split())
    P.append(complex(x, y))
ans = 0
for pz in P:
    q = []
    for p in P:
        if p != pz:
            q.append(math.degrees(180 + cmath.phase(p - pz)))
    q.sort()
    for d in q:
        dn = d + 180
        if dn > 360:
            dn -= 360
        p = bisect.bisect_left(q, dn)
        l = q[p - 1] - d
        if l < 0:
            l += 360
        if l > 360:
            l -= 360
        r = q[p] - d
        if r < 0:
            r += 360
        if r > 360:
            r -= 360
        ans = max(ans, min(l, 360 - l), min(r, 360 - r))
print(ans)
