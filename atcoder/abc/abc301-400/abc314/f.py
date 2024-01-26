import sys
from collections import defaultdict, deque

input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)


class ModInt:
    def __init__(self, x, p=998244353):
        self.mod = p
        self.x = x % self.mod

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x)
            if isinstance(other, ModInt)
            else ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x)
            if isinstance(other, ModInt)
            else ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x)
            if isinstance(other, ModInt)
            else ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(self.x * pow(other.x, self.mod - 2, self.mod))
            if isinstance(other, ModInt)
            else ModInt(self.x * pow(other, self.mod - 2, self.mod))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, self.mod))
            if isinstance(other, ModInt)
            else ModInt(pow(self.x, other, self.mod))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x)
            if isinstance(other, ModInt)
            else ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(other.x * pow(self.x, self.mod - 2, self.mod))
            if isinstance(other, ModInt)
            else ModInt(other * pow(self.x, self.mod - 2, self.mod))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, self.mod))
            if isinstance(other, ModInt)
            else ModInt(pow(other, self.x, self.mod))
        )


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


n = int(input())
pq = []

for _ in range(n - 1):
    p, q = map(int, input().split())
    pq.append((p - 1, q - 1))

uftree = UnionFind(n)

# 試合開始
# 有向グラフの木を構築して落としていくのが良さそう
edges = defaultdict(list)
points = defaultdict(lambda: ModInt(0))
parents = defaultdict(lambda: -1)


def find_parents(node):
    first_node = node
    path_node_list = [first_node]
    while parents[node] != -1:
        node = parents[node]
        path_node_list.append(node)
    for child_node in path_node_list:
        parents[child_node] = node
    return node


for edge_i, (p, q) in enumerate(pq, start=0):
    # pが先攻, qが後攻
    edge_num = n + edge_i
    team_a_num = uftree.size(p)
    team_b_num = uftree.size(q)
    team_a = ModInt(team_a_num) / ModInt(team_a_num + team_b_num)
    team_b = ModInt(team_b_num) / ModInt(team_a_num + team_b_num)
    parent_p = find_parents(p)
    parent_q = find_parents(q)
    points[parent_p] = team_a
    points[parent_q] = team_b
    edges[edge_num].append(parent_p)
    edges[edge_num].append(parent_q)
    parents[parent_p] = edge_num
    parents[parent_q] = edge_num
    # for i in uftree.members(p):
    #     ans[i] += team_a
    # for i in uftree.members(q):
    #     ans[i] += team_b
    uftree.union(p, q)

# dfsで木を辿って点数を数える
q = deque()
q.append(n + n - 2)
while q:
    now = q.popleft()
    for next in edges[now]:
        points[next] += points[now]
        q.append(next)
ans = []
for i in range(n):
    ans_i = points[i]
    ans.append(ans_i)
# print(edge_name)
# print(edges)
print(*ans, sep=" ")
