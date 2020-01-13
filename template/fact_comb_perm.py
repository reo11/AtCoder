from math import factorial


class Facts():
    def __init__(self, max_num=10**5, p=10**9 + 7):
        self.p = p
        self.max_num = max_num
        self.fact = [1] * (self.max_num + 1)
        for i in range(1, self.max_num + 1):
            self.fact[i] = self.fact[i-1] * i
            self.fact[i] %= self.p

    def comb(self, n, k):
        """ nCk mod p を求める """
        """ 計算量 O(log(p)) """
        """ n! / (n-k)! / k! mod p """
        """ フェルマーの小定理 a^(-1) ≡ a^(p-2) """
        """ n! * k!^(p-2) * (n-k)!^(p-2) mod p """
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
        """ nPk mod p を求める """
        """ 計算量 O(b - a)? """
        """ n! / (n-k)! mod p """
        """ n! * (n-k)!^(p-2) mod p """
        if n < 0 or k < 0 or n < k:
            return 0
        if n == 0 or k == 0:
            return 1
        a = self.fact[n]
        b = self.fact[n-k]
        return (a * self.power_func(b, self.p-2)) % self.p
