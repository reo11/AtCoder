import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)
MOD = 998244353
n, m = map(int, input().split())

def rep_pow(a: int, k: int, p: int = 10 ** 9 + 7) -> int:
    ans = 1
    while k > 0:
        if k & 1:
            ans = ans * a % p
        a = a * a % p
        k >>= 1
    return ans

class ModInt:
    def __init__(self, x, p=998244353):
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

class Facts:
    # O(max_num)
    def __init__(self, max_num: int = 10 ** 5, p: int = 10 ** 9 + 7) -> None:
        self.p = p
        self.max_num = max_num
        self.fact = [1] * (self.max_num + 1)
        for i in range(1, self.max_num + 1):
            self.fact[i] = self.fact[i - 1] * i
            self.fact[i] %= self.p

    def comb(self, n: int, k: int) -> int:
        # nCk mod p with memo
        # O(log(p))
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a = self.fact[n]
        b = self.fact[k]
        c = self.fact[n - k]
        return (
            a * self.power_func(b, self.p - 2) * self.power_func(c, self.p - 2)
        ) % self.p

    def comb_base(self, n: int, k: int) -> int:
        # nCk mod p w/o memo
        # O(min(n, k)) ?
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a, b = 1, 1
        for i in range(k):
            a *= n - i
            a %= MOD
        for i in range(k):
            b *= k - i
            b %= MOD
        return (a * self.power_func(b, self.p - 2)) % self.p

    def perm(self, n: int, k: int) -> int:
        # nPk mod p
        # O(log(p))
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a = self.fact[n]
        b = self.fact[n - k]
        return (a * self.power_func(b, self.p - 2)) % self.p

    def power_func(self, a: int, b: int) -> int:
        # a^b mod p
        # O(log(b))
        ans = 1
        while b > 0:
            if b & 1:
                ans = ans * a % self.p
            a = a * a % self.p
            b >>= 1
        return ans

facts = Facts(10 ** 6 + 1, MOD)

def sterling_dfs(n: int, m: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}

    if (n, m) in memo:
        return memo[(n, m)]

    if n < m:
        return 0
    if n == m:
        return 1
    if m == 0:
        return 0

    memo[(n, m)] = (n - 1) * sterling(n - 1, m, memo) + sterling(n - 1, m - 1, memo)
    return memo[(n, m)]

def sterling(n, k):
    # n個の区別できるものをk個の区別できないものに分割する場合の数
    # O(klogn)
    ret = 0
    for i in range(k):
        if ((k - i) % 2 == 0):
            ret = ret + facts.comb(k, i) * facts.power_func(i, n) % MOD
            ret %= MOD
        else:
            ret = ret + (MOD - facts.comb(k, i) * facts.power_func(i, n) % MOD)
            ret %= MOD
    ret *= facts.power_func(facts.fact[k], MOD - 2)
    ret %= MOD
    return ret

def bell(n, k):
    if k > n:
        k = n
    jsum = [0] * (k + 2)
    for j in range(0, k + 1):
        add = facts.power_func(j, MOD - 2)
        if (j % 2 == 0):
            jsum[j+1] = jsum[j] + add
        else:
            jsum[j+1] = jsum[j] - add
    res = 0
    for i in range(0, k + 1):
        res += (facts.power_func(i, n) % MOD) * \
            facts.power_func(i, MOD - 2) * jsum[k - i + 1]

    return res % MOD

def solve1(n, m):
    if n == 1:
        return m
    count = (m - 1) * bell(n - 1, m - 1)
    count %= MOD
    count -= (m - 2) * bell(n - 2, m - 2)
    return count % MOD

def solve2(n, m):
    ans = 1
    tmp_v = 0
    for i in range(n):
        if i == 0:
            ans *= m
        elif i == n - 2:
            # 前の人と違うもの
            ans *= m - 1
        elif i < n - 2:
            ans *= m - 1
        ans %= MOD
    # 最初と最後が同じものを省く
    ans += tmp_v
    ans %= MOD
    return ans
print(solve2(n, m))