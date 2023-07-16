import sys
from collections import defaultdict
from math import gcd

input = sys.stdin.readline
MOD = 10 ** 9 + 7
MAX = 2 * (10 ** 5) + 1
sqr = [1 for _ in range(MAX)]
for i in range(1, MAX):
    sqr[i] = sqr[i - 1] * 2
    sqr[i] %= MOD


class FLT:
    def __init__(self, mod=10 ** 9 + 7):
        self.mod = mod

    def rep_sqr(self, base, k):
        ans = 1
        while k > 0:
            if k & 1:
                ans = ans * base % self.mod
            base = base * base % self.mod
            k >>= 1
        return ans

    def inv(self, a):
        """ 逆元を取る """
        return self.rep_sqr(a, self.mod - 2)


n = int(input())
d = defaultdict(lambda: 0)
ans = 1
flt = FLT()
cnt_0 = 0
for i in range(n):
    a, b = map(int, input().split())
    g = gcd(a, b)
    a //= g
    b //= g
    if a == 0 and b == 0:
        cnt_0 += 1
        continue
    if a == 0:
        tmp1 = "b_0"
    else:
        tmp1 = format(-b / a, ".14f").rstrip("0").rstrip(".")
    cnt = d[tmp1]
    if cnt <= 0:
        ans *= 2
    else:
        ans *= flt.inv(sqr[cnt])
        ans *= sqr[cnt] + 1
    ans %= MOD
    if b == 0:
        d["b_0"] += 1
    else:
        tmp2 = format(a / b, ".14f").rstrip("0").rstrip(".")
        d[tmp2] += 1
# print(d)
print(ans - 1 + cnt_0)
