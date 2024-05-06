# コストが小さい方から全て採用して全域木を作る
n, m = map(int, input().split())
candidates = []
for _ in range(m):
    k, weight = map(int, input().split())
    a = list(map(int, input().split()))
    a = [x - 1 for x in a]
    candidates.append((weight, a))
candidates.sort()

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

tree = UnionFind(n)

cost_sum = 0
for weight, a in candidates:
    for i in range(1, len(a)):
        if not tree.same(a[i - 1], a[i]):
            cost_sum += weight
            tree.union(a[i - 1], a[i])
        else:
            continue

if tree.size(0) == n:
    print(cost_sum)
else:
    print(-1)
