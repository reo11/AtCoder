class FLT:
    """
    フェルマーの小定理
    a^(-1) = a^(m-2) mod p
    """

    def __init__(self, mod: int = 10**9 + 7) -> None:
        self.mod = mod

    def rep_sqr(self, base: int, k: int) -> int:
        ans = 1
        while k > 0:
            if k & 1:
                ans = ans * base % self.mod
            base = base * base % self.mod
            k >>= 1
        return ans

    def inv(self, a: int) -> int:
        """逆元を取る"""
        return self.rep_sqr(a, self.mod - 2)
