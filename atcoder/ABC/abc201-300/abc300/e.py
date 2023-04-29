
from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
MOD = 998244353
class ModInt:
    def __init__(self, x, p=MOD):
        self.mod = p
        self.x = x % self.mod

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x)
            if isinstance(other, ModInt)
            else ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x)
            if isinstance(other, ModInt)
            else ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x)
            if isinstance(other, ModInt)
            else ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(self.x * pow(other.x, self.mod - 2, self.mod))
            if isinstance(other, ModInt)
            else ModInt(self.x * pow(other, self.mod - 2, self.mod))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, self.mod))
            if isinstance(other, ModInt)
            else ModInt(pow(self.x, other, self.mod))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x)
            if isinstance(other, ModInt)
            else ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(other.x * pow(self.x, self.mod - 2, self.mod))
            if isinstance(other, ModInt)
            else ModInt(other * pow(self.x, self.mod - 2, self.mod))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, self.mod))
            if isinstance(other, ModInt)
            else ModInt(pow(other, self.x, self.mod))
        )

N = int(input())

n_tmp = N
counter = defaultdict(int)
# 2, 3, 5でnを割り切れるか

while n_tmp % 2 == 0 and n_tmp > 0:
    counter[2] += 1
    n_tmp //= 2

while n_tmp % 3 == 0 and n_tmp > 0:
    counter[3] += 1
    n_tmp //= 3

while n_tmp % 5 == 0 and n_tmp > 0:
    counter[5] += 1
    n_tmp //= 5

if n_tmp != 1:
    print(0)
    exit()

memo = defaultdict(lambda: -1)
def dp(i):
    if i >= N:
        if i == N:
            return 1
        else:
            return 0
    if memo[i] != -1:
        return memo[i]
    res = ModInt(0)
    for j in range(2, 7):
        res = res + dp(j * i)
    res = res / 5
    memo[i] = res
    return res

print(dp(1))
# print(counter)