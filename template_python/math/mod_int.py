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
