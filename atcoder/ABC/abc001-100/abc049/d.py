import sys
from collections import defaultdict
input = sys.stdin.readline


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x_root = self.Find_Root(x)
        y_root = self.Find_Root(y)

        if(x_root == y_root):
            return
        # 違う木に属していた場合rankを見てくっつける方を決める
        if self.rank[x_root] >= self.rank[y_root]:
            self.rank[x_root] += self.rank[y_root]
            self.root[y_root] = x_root
        else:
            self.rank[y_root] += self.rank[x_root]
            self.root[x_root] = y_root

    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

n, k, l = map(int, input().split())
pq = [list(map(int, input().split())) for _ in range(k)]
rs = [list(map(int, input().split())) for _ in range(l)]

uf1 = UnionFind(n)
uf2 = UnionFind(n)

for i in range(k):
    uf1.Unite(pq[i][0], pq[i][1])

for i in range(l):
    uf2.Unite(rs[i][0], rs[i][1])

pairs = []
d = defaultdict(int)

for i in range(1, n+1):
    name = "{} {}".format(uf1.Find_Root(i), uf2.Find_Root(i))
    pairs.append(name)
    d[name] += 1

ans = []
for i in range(n):
    ans.append(d[pairs[i]])

print(*ans)


