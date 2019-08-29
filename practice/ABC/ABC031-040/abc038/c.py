from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

n = int(input())
a = list(map(int, input().split()))

l = 0
r = -1

c_l = []

pre = -1
for i in range(n):
    if pre < a[i]:
        r += 1
    else:
        c_l.append(r-l+1)
        l = i
        r = i
    pre = a[i]
c_l.append(r-l+1)

def calc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        return int(cmb(n, 2))

ans = 0
for v in c_l:
    ans += calc(v)
print(ans + n)