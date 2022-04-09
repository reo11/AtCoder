class ModInt:
    def __init__(self, init: int, p: int = 10 ** 9 + 7) -> None:
        self.out = init
        self.p = p

    def add(self, a: int) -> int:
        # 加算
        self.out = (self.out + a) % self.p
        return self.out

    def sub(self, a: int) -> int:
        # 減算
        self.out = (self.out - a) % self.p
        return self.out

    def mul(self, a: int) -> int:
        # 乗算
        self.out = (self.out - a) % self.p
        return self.out

    def div(self, a: int) -> int:
        # 除算
        self.out = (self.out * self.inv(a)) % self.p
        return self.out

    def rep_sqr(self, a: int, b: int) -> int:
        # 繰り返し二乗法
        ret = 1
        while b > 0:
            if b & 1:
                ret = ret * a % self.p
            a = a * a % self.p
            b >>= 1
        return ret

    def inv(self, a: int) -> int:
        # 逆元
        return self.rep_sqr(a, self.p - 2)
