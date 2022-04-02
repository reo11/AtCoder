n, a, b = map(int, input().split())
p = 10 ** 9 + 7

MOD = 10 ** 9 + 7
from math import factorial


class Facts:
    # 階乗のメモ化
    # 組み合わせ数、順列数の計算を高速に行う
    def __init__(self, max_num=(2 * 10 ** 5) + 1, p=10 ** 9 + 7):
        self.p = p
        self.max_num = max_num
        self.fact = [1] * (self.max_num + 1)
        for i in range(1, self.max_num + 1):
            self.fact[i] = self.fact[i - 1] * i
            self.fact[i] %= self.p

    def comb(self, n, k):
        # nCk mod p を求める
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a = n
        for i in range(1, k):
            a *= n - i
            a %= MOD

        b = k
        for i in range(1, k):
            b *= k - i
            b %= MOD

        return (a * self.power_func(b, self.p - 2)) % self.p

    def power_func(self, a, b):
        # a^b mod p　を繰り返し二乗法で求める
        if b == 0:
            return 1
        if b % 2 == 0:
            d = self.power_func(a, b // 2)
            return d * d % self.p
        if b % 2 == 1:
            return (a * self.power_func(a, b - 1)) % self.p


class FLT:
    # フェルマーの小定理
    # a^(-1) = a^(m-2) mod p
    def __init__(self, mod=10 ** 9 + 7):
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
        return self.rep_sqr(a, self.mod - 2)


fact = Facts()
flt = FLT()
a_comb = fact.comb(n, a)
b_comb = fact.comb(n, b)

ans = (flt.rep_sqr(2, n) - 1 - a_comb - b_comb) % MOD
print(ans)
