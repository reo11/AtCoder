from collections import defaultdict
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

MOD = 998244353

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

class UnionFind():
    def __init__(self, n):
        self.n = n + 1
        self.parents = [-1] * (n + 1)

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def calc_num(y, x):
    return w * y + x

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
uf_tree = UnionFind(h*w)
ans = ModInt(0)
count_red = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            count_red += 1
        else:
            num = calc_num(i, j)
            for dx, dy in dxy:
                x = j + dx
                y = i + dy
                if 0 <= x < w and 0 <= y < h and s[y][x] == '#':
                    neighbor_num = calc_num(y, x)
                    if not uf_tree.same(num, neighbor_num):
                        uf_tree.union(num, neighbor_num)

v = 0
groups = set()
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            num = calc_num(i, j)
            groups.add(uf_tree.find(num))
base_group_count = len(groups)
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            num = calc_num(i, j)
            groups = set()
            for dx, dy in dxy:
                x = j + dx
                y = i + dy
                if 0 <= x < w and 0 <= y < h and s[y][x] == '#':
                    neighbor_num = calc_num(y, x)
                    groups.add(uf_tree.find(neighbor_num))
            if len(groups) == 1:
                ans += ModInt(base_group_count)
                v += base_group_count
            elif len(groups) == 0:
                ans += ModInt(base_group_count + 1)
                v += base_group_count + 1
            else:
                ans += ModInt(base_group_count - len(groups) + 1)
                v += base_group_count - len(groups) + 1

ans /= ModInt(count_red)
print(ans)

