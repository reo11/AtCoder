import sys
from collections import defaultdict
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


input = sys.stdin.readline

n = int(input())
d = defaultdict(lambda: 0)

for i in range(n):
    s = list(str(input()).rstrip())
    s.sort()
    s = "".join(s)
    d[s] += 1   

ans = 0
for key in d.keys():
    if d[key] >= 2:
        ans += cmb(d[key], 2)
print(int(ans))