from collections import defaultdict

n, m = map(int, input().split())
ab = []
for _ in range(m):
    a, b = map(int, input().split())
    ab.append((a - 1, b - 1))

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

uf_tree = UnionFind(n=n)

for a, b in ab:
    uf_tree.union(a, b)

group_counts = defaultdict(int)

for i in range(n):
    group = uf_tree.find(i)
    group_counts[group] += 1

path_count = defaultdict(int)
for a, _ in ab:
    group = uf_tree.find(a)
    path_count[group] += 1

ans = 0
for group in group_counts.keys():
    ans += group_counts[group] * (group_counts[group] - 1) // 2
    ans -= path_count[group]

print(ans)
