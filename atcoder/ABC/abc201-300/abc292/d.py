from collections import defaultdict
n, m = map(int, input().split())

# UnionFind木を辺の情報を保持して更新すれば行ける

class UnionFind():
    def __init__(self, n):
        self.n = (n + 1)
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
        return ''.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

tree = UnionFind(n)
uv = []
edges = defaultdict(int)
for _ in range(m):
    u, v = map(int, input().split())
    tree.union(u, v)
    edges[tree.find(u)] += 1

flag = True
for i in range(1, n + 1):
    p_size = tree.size(i)
    e_size = edges[tree.find(i)]
    if p_size != e_size:
        flag = False

print(['No', 'Yes'][flag])
