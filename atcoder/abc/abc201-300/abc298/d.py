import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


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


MOD = 998244353
q = int(input())

s = deque([1])
ans = []
ten_multi = [0 for _ in range((6 * (10**5)) + 1)]
ten = 1
for i in range(len(ten_multi)):
    ten_multi[i] = ten
    ten = (ten * 10) % MOD

ans_mod = ModInt(1)
for _ in range(q):
    query = input()
    if query[0] == "1":
        # 末尾に数字xを追加
        _, x = map(int, query.split())
        s.append(x)
        # 前の値を10倍して、xを足している
        ans_mod = ans_mod * 10 + x
    elif query[0] == "2":
        # 先頭の数字を削除
        x = s.popleft()
        # 前の値からx * 10 ** nを引いている
        sub = x * ten_multi[len(s)]
        ans_mod = ans_mod - sub
    else:
        # 10進数表記のMOD
        ans.append(str(ans_mod))
print("\n".join(ans))
