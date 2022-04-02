from collections import defaultdict
from functools import reduce
from operator import mul

dic = defaultdict(int)
MOD = 998244353


def cmb(n, r, mod):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under % mod


n = int(input())
d = list(map(int, input().split()))
max_d = max(d)

fac = [1] * (max_d + 1)
bi_fac = [1] * (max_d + 1)

for i in range(1, max_d + 1):
    fac[i] = fac[i - 1] * i
    fac[i] %= MOD
    bi_fac[i] = bi_fac[i - 1] * 2
    bi_fac[i] %= MOD

if d[0] != 0:
    print(0)
    exit()

for i in d:
    dic[i] += 1
if dic[0] > 1:
    print(0)
    exit()

ans = 1
for i in range(1, max_d + 1):
    if dic[i] > 2 * dic[i - 1]:
        print(0)
        exit()
    else:
        ans *= cmb(dic[i - 1] * 2, dic[i], MOD)
        ans %= MOD
print(ans)
