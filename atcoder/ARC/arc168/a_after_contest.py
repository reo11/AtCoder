n = int(input())
s = list(input())

class BIT:
    def __init__(self, n):
        self.size=n
        self.tree = [0] * (n+1)
    
    def add(self, i,x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def sum(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

def InversionNumberByBIT(A):
    ans = 0
    Bit = BIT(max(len(A) + 1, max(A) + 1))
    for i in range(len(A)):
        ans += i - Bit.sum(A[i])
        Bit.add(A[i], 1)
    return ans

x = [1]

for si in s:
    if si == "<":
        x.append(x[-1] + 10 ** 9)
    else:
        x.append(x[-1] - 1)

x_set = sorted(list(set(x)))
# 座標圧縮
x_dict = {}
for i, xi in enumerate(x_set, start=1):
    x_dict[xi] = i

for i in range(len(x)):
    x[i] = x_dict[x[i]]

print(InversionNumberByBIT(x))