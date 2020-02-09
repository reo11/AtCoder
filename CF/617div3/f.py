class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weight = [0] * (n+1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        if self.find(x) != self.find(y):
            return "?"
        return self.weight[x] - self.weight[y]


n, q = map(int, input().split())

tree = WeightedUnionFind(n)

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        x, y, z = query[1:4]
        tree.union(x, y, z)
    else:
        x, y = query[1:3]
        ans = tree.diff(x, y)
        print(ans)

n = int(input())

for i in range(n-1):
