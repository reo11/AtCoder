MOD = 10**9+7
r1, c1, r2, c2 = map(int, input().split())
n = (2 * 10 ** 6) + 2
from math import factorial

class Facts():
    # 階乗のメモ化
    # 組み合わせ数、順列数の計算を高速に行う
    def __init__(self, max_num=10**5, p=10**9 + 7):
        self.p = p
        self.max_num = max_num
        self.fact = [1] * (self.max_num + 1)
        for i in range(1, self.max_num + 1):
            self.fact[i] = self.fact[i-1] * i
            self.fact[i] %= self.p

    def comb(self, n, k):
        # nCk mod p を求める
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a = self.fact[n]
        b = self.fact[k]
        c = self.fact[n-k]
        return (a*self.power_func(b, self.p-2) *
                self.power_func(c, self.p-2)) % self.p

    def perm(self, n, k):
        # nPk mod p を求める
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a = self.fact[n]
        b = self.fact[n-k]
        return (a * self.power_func(b, self.p-2)) % self.p


    def power_func(self, a, b):
        # a^b mod p　を繰り返し二乗法で求める
        if b == 0:
            return 1
        if b % 2 == 0:
            d = self.power_func(a, b//2)
            return d*d % self.p
        if b % 2 == 1:
            return (a*self.power_func(a, b-1)) % self.p

class FLT:
    #フェルマーの小定理
    # a^(-1) = a^(m-2) mod p
    def __init__(self, mod=10**9+7):
        self.mod = mod

    def rep_sqr(self, base, k):
        if k == 0:
            return 1
        elif k % 2 == 0:
            return (self.rep_sqr(base, k // 2) ** 2) % self.mod
        else:
            return (self.rep_sqr(base, k - 1) * base) % self.mod

    def inv(self, a):
        # 逆元を取る
        return self.rep_sqr(a, self.mod-2)

fact = Facts(n)

def f(x, y):
    return fact.comb(x+y, y)

def g(x, y):
    return f(x+1, y+1)

print((g(r2, c2) - g(r2, c1-1) - g(r1 - 1, c2) + g(r1 - 1, c1 - 1)) % MOD)

