# AGC064B
import sys
from collections import defaultdict, deque
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

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

n, m = map(int, input().split())
edges = defaultdict(lambda: defaultdict(lambda: []))
flags = defaultdict(lambda: False)
abc = []
used = defaultdict(lambda: False)
uf = UnionFind(n)
for i in range(m):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    abc.append((a - 1, b - 1, c))
s = list(input())

for i, (a, b, c) in enumerate(abc, start=1):
    edges[a][c].append([i, b])
    edges[b][c].append([i, a])
    # 両端が指定された色の場合は、その色の辺は必ず採用する
    if s[a] == s[b] and not uf.same(a, b) and s[a] == c:
        used[i] = True
        flags[a] = True
        flags[b] = True
        uf.union(a, b)

# 条件が満たされている頂点から順に処理する
process_list = deque([])
for i in range(n):
    if flags[i]:
        process_list.append(i)

# 条件を満たしていない頂点から条件を満たしている頂点へ辺を張る
# 張れない場合は、その頂点は条件を満たしていない頂点としてリストの末尾に追加する
# 張れない頂点がループしたり、そもそも辺の候補に条件を満たすものがない場合はNo

while len(process_list) > 0:
    count = 0
    next_process_list = deque([])
    for current_node in process_list:
        for c in ["R", "B"]:
            for i, next_node in edges[current_node][c]:
                if s[next_node] != c:
                    continue
                if used[i]:
                    continue
                if uf.same(current_node, next_node):
                    continue
                if flags[next_node]:
                    continue
                used[i] = True
                flags[next_node] = True
                uf.union(current_node, next_node)
                count += 1
                next_process_list.append(next_node)
    process_list = next_process_list
    if count == 0:
        break

# 条件は全て満たされているはずなので、残りの辺を適当に採用する
for i in range(1, m + 1):
    a, b, c = abc[i - 1]
    if used[i]:
        continue
    if not uf.same(a, b):
        used[i] = True
        uf.union(a, b)

ng_flag = False
# 全ての頂点が条件を満たしているかチェック
for i in range(n):
    if not flags[i]:
        ng_flag = True
        break

ans = []
for i in range(1, m + 1):
    if used[i]:
        ans.append(str(i))
if len(ans) == n - 1 and not ng_flag:
    print("Yes")
    print(*ans, sep=" ")
else:
    print("No")