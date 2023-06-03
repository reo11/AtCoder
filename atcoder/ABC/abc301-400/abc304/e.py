import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()


n, m = map(int, input().split())
uv = []
for _ in range(m):
    u, v = map(int, input().split())
    uv.append([u, v])
k = int(input())
xy = []
for _ in range(k):
    x, y = map(int, input().split())
    xy.append([x, y])
q = int(input())
pq = []
for _ in range(q):
    p, q = map(int, input().split())
    pq.append([p, q])
ans = [] # Yes or No

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

uf = UnionFind(n)
for u, v in uv:
    uf.union(u, v)
bad_set = set()
for x, y in xy:
    group_x = uf.find(x)
    group_y = uf.find(y)
    bad_set.add(f"{group_x}_{group_y}")
    bad_set.add(f"{group_y}_{group_x}")

for p, q in pq:
    group_p = uf.find(p)
    group_q = uf.find(q)
    if f"{group_p}_{group_q}" in bad_set:
        ans.append("No")
    else:
        ans.append("Yes")
print(*ans, sep="\n")