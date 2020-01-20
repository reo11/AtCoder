class FLT:
    """
    フェルマーの小定理
    a^(-1) = a^(m-2) mod p
    """
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
        """ 逆元を取る """
        return self.rep_sqr(a, self.mod-2)
