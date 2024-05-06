from collections import defaultdict
n, m = map(int, input().split())
abc = []

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

groups = UnionFind(n + 1)
num = defaultdict(lambda: 0)

for _ in range(m):
    a, b, c = map(int, input().split())
    abc.append((a, b, c))
    groups.union(a, b)

group_nums = defaultdict(lambda: defaultdict(lambda: 0))
for a, b, c in abc:
    group_id = groups.find(a)
    if group_nums[group_id][a] != 0:
        group_nums[group_id][b] = group_nums[group_id][a] - c
    else:
        group_nums[group_id][a] = group_nums[group_id][b] + c

candidates = defaultdict(lambda: [])

group_orders = defaultdict(lambda: [])
for group_id, nums in group_nums.items():
    min_value = min(nums.values())
    sorted_nums = list(sorted([[k, v - min_value] for k, v in nums.items()], key=lambda x: x[1]))
    max_num = sorted_nums[-1][1]
    for base_num in range(1, n + 1 - max_num):
        pattern = []
        for pos, value in sorted_nums:
            pattern.append((pos, value + base_num))
        candidates[group_id].append(pattern)

sets = [set() for _ in range(n + 1)]

for cand in candidates.values():
    for c in cand:
        for pos, value in c:
            sets[pos].add(value)
print(sets)

ans = []
for ss in sets[1:]:
    if len(ss) == 1:
        ans.append(list(ss)[0])
    else:
        ans.append(-1)
print(*ans, sep=" ")
