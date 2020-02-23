n, k = map(int, input().split())
MOD = 10**9 + 7

from math import factorial
class Facts():
    """
    階乗のメモ化
    組み合わせ数、順列数の計算を高速に行う
    """
    def __init__(self, max_num=2*10**5, p=10**9 + 7):
        self.p = p
        self.max_num = max_num
        self.fact = [1] * (self.max_num + 1)
        self.ifact = [1] * (self.max_num + 1)
        for i in range(1, self.max_num + 1):
            self.fact[i] = self.fact[i-1] * i
            self.fact[i] %= self.p
            self.ifact[i] = self.power_func(self.fact[i], self.p-2)

    def comb(self, n, k):
        """ nCk mod p を求める """
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a = self.fact[n]
        return (a*self.ifact[k] * self.ifact[n-k]) % self.p


    def power_func(self, a, b):
        """ a^b mod p　を繰り返し二乗法で求める """
        if b == 0:
            return 1
        if b % 2 == 0:
            d = self.power_func(a, b//2)
            return d*d % self.p
        if b % 2 == 1:
            return (a*self.power_func(a, b-1)) % self.p

facts = Facts()

ans = 0
for i in range(min(n, k+1)):
    ans += (facts.comb(n, i) * facts.comb(n-1, i)) % MOD
    ans %= MOD
print(ans)