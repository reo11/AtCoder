from math import factorial


class Facts():
    """
    階乗のメモ化
    組み合わせ数、順列数の計算を高速に行う
    前処理でO(max_num)
    max_num >= 10^6 あたりから厳しい
    """
    def __init__(self, max_num=10**5, p=10**9 + 7):
        self.p = p
        self.max_num = max_num
        self.fact = [1] * (self.max_num + 1)
        for i in range(1, self.max_num + 1):
            self.fact[i] = self.fact[i-1] * i
            self.fact[i] %= self.p

    def comb(self, n, k):
        """
        メモ化した物を使って nCk mod p を求める
        逆元の計算にO(log(p))
        """
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a = self.fact[n]
        b = self.fact[k]
        c = self.fact[n-k]
        return (a*self.power_func(b, self.p-2) *
                self.power_func(c, self.p-2)) % self.p

    def comb_base(self, n, k):
        """
        nCk mod p を求める (計算量的にmax(n, k) < 10^7くらいまでは使える)
        O(max(n, k))
        """

        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a, b = 1, 1
        for i in range(k):
            a *= (n-i)
            a %= MOD
        for i in range(k):
            b *= (k-i)
            b %= MOD
        return (a*self.power_func(b, self.p-2)) % self.p

    def perm(self, n, k):
        """
        nPk mod p を求める
        逆元の計算にO(log(p))
        """
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a = self.fact[n]
        b = self.fact[n-k]
        return (a * self.power_func(b, self.p-2)) % self.p


    def power_func(self, a, b):
        """
        a^b mod p　を繰り返し二乗法で求める
        O(log(b))
        """
        ans = 1
        while b > 0:
            if b & 1:
                ans = ans * a % self.p
            a = a * a % self.p
            b >>= 1
        return ans
