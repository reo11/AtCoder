from collections import defaultdict, deque


class UnionFind:
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
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())


n, m = map(int, input().split())
uf = UnionFind(n)
UNK = "undecidable"

relations = defaultdict(lambda: defaultdict(lambda: [UNK, UNK]))

for _ in range(m):
    a, b, x, y = map(int, input().split())
    a -= 1
    b -= 1
    relations[a][b] = [x, y]
    relations[b][a] = [-x, -y]
    uf.union(a, b)

ans = [UNK for _ in range(n)]
visited = [False for _ in range(n)]
queue = deque([[0, 0, 0]])
while queue:
    num, x, y = queue.popleft()
    visited[num] = True
    if uf.same(0, num):
        ans[num] = f"{x} {y}"
        for next_num, (next_x, next_y) in relations[num].items():
            if visited[next_num]:
                continue
            queue.append([next_num, x + next_x, y + next_y])
            visited[next_num] = True

print(*ans, sep="\n")
