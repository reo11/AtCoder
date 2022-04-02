class UnionFind:
    def __init__(self, n):
        self.tree = [-1] * n

    # xとyの属する集合を併合
    def union(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return
        self.tree[b] = a

    # 木の根を求める
    def root(self, a):
        if self.tree[a] < 0:
            return a
        else:
            res = self.root(self.tree[a])
            self.tree[a] = res
            return res

    # xとyが同じ集合に属するか否か
    def same(self, a, b):
        return self.root(a) == self.root(b)


import sys

input = sys.stdin.readline

n, q = map(int, input().split())
uf = UnionFind(n)
ans = []
for i in range(q):
    p, a, b = map(int, input().split())
    a -= 1
    b -= 1
    if p == 0:
        uf.union(a, b)
    else:
        if uf.same(a, b):
            ans.append("Yes")
        else:
            ans.append("No")
print("\n".join(ans))
