from collections import defaultdict, deque
import itertools
INF = float("inf")

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


n, m, k = map(int, input().split())
uf = UnionFind(n)

uvw = []

for _ in range(m):
    u, v, w = map(int, input().split())
    uvw.append((u, v, w))

ans = INF
for used_path in itertools.combinations(uvw, n - 1):
    uf = UnionFind(n)
    cost = 0
    flag = True
    path_count = 0
    for u, v, w in used_path:
        if uf.same(u, v):
            flag = False
            break
        uf.union(u, v)
        cost += w
        cost %= k

    if flag:
        ans = min(ans, cost)
print(ans)