import sys
from typing import Dict, List
from collections import defaultdict

sys.setrecursionlimit(20000000)
input = lambda: sys.stdin.readline().rstrip()

class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int) -> int:
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int) -> int:
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def members(self, x: int) -> List[int]:
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self) -> List[int]:
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self) -> int:
        return len(self.roots())

    def all_group_members(self) -> Dict[int, List[int]]:
        return {r: self.members(r) for r in self.roots()}

    def __str__(self) -> str:
        return "\n".join("{}: {}".format(r, self.members(r)) for r in self.roots())

tree = UnionFind(n=200001)
n, m, e = map(int, input().split())

uv = []
for _ in range(e):
    u, v = map(int, input().split())
    uv.append([u, v])
q = int(input())
x = []
for _ in range(q):
    x.append(int(input()))
x_set = set(x)

ans = [0]
for i, (u, v) in enumerate(uv, start=1):
    if i not in x_set:
        tree.union(x=u, y=v)

status = defaultdict(lambda: {"has_electricity": False, "city_count": 0})
for i in range(1, n + 1):
    status[tree.find(x=i)]["city_count"] += 1
for i in range(n + 1, n + m + 1):
    status[tree.find(x=i)]["has_electricity"] = True

for group_id, d in status.items():
    if d["has_electricity"]:
        ans[0] += d["city_count"]

for x_i in reversed(x):
    u, v = uv[x_i - 1]
    u_group_id = tree.find(u)
    u_group_size = status[u_group_id]["city_count"]
    u_has_electricity = status[u_group_id]["has_electricity"]
    v_group_id = tree.find(v)
    v_group_size = status[v_group_id]["city_count"]
    v_has_electricity = status[v_group_id]["has_electricity"]

    tree.union(x=u, y=v)
    if u_group_id == v_group_id:
        ans.append(ans[-1])
        continue

    new_group_id = tree.find(u)
    if u_has_electricity and not v_has_electricity:
        ans.append(ans[-1] + v_group_size)
    elif not u_has_electricity and v_has_electricity:
        ans.append(ans[-1] + u_group_size)
    else:
        ans.append(ans[-1])

    status.pop(u_group_id)
    status.pop(v_group_id)
    status[new_group_id]["has_electricity"] = u_has_electricity or v_has_electricity
    status[new_group_id]["city_count"] = u_group_size + v_group_size

print("\n".join(list(map(str, reversed(ans[:-1])))))
