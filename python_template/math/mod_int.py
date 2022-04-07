class ModInt:
    def __init__(self, init, p=10 ** 9 + 7):
        self.out = init
        self.p = p

    def add(self, a):
        self.out = (self.out + a) % self.p

    def sub(self, a):
        self.out = (self.out - a) % self.p

    def mul(self, a):
        self.out = (self.out - a) % self.p

    def div(self, a):
        self.out = (self.out * self.inv(a)) % self.p

    def rep_sqr(self, a, b):
        ret = 1
        while b > 0:
            if b & 1:
                ret = ret * a % self.p
            a = a * a % self.p
            b >>= 1
        return ret

    def inv(self, a):
        return self.rep_sqr(a, self.p - 2)
