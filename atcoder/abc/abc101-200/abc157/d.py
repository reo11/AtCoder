import sys

input = sys.stdin.readline
from collections import defaultdict

n, m, k = map(int, input().split())


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

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
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())


friend_uf = UnionFind(n)

count_friend = [0 for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    count_friend[a - 1] += 1
    count_friend[b - 1] += 1
    friend_uf.union(a - 1, b - 1)

ans = [0 for _ in range(n)]
for i in range(1, n + 1):
    ans[i - 1] = friend_uf.size(i - 1) - count_friend[i - 1] - 1

for i in range(k):
    c, d = map(int, input().split())
    if friend_uf.same(c - 1, d - 1):
        ans[c - 1] -= 1
        ans[d - 1] -= 1

out = []
for i in range(n):
    out.append(str(max(ans[i], 0)))

print(" ".join(out))
