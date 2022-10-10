from typing import Dict, List

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

MERGIN = 3000
HALF = MERGIN // 2

n = int(input())
uf = UnionFind(n=MERGIN*MERGIN)

xy_list = []
xy = [[False for _ in range(MERGIN)] for _ in range(MERGIN)]
for _ in range(n):
    x, y = map(int, input().split())
    xy[y + HALF][x + HALF] = True
    xy_list.append([x + HALF, y + HALF])

dx_list = [-1, -1, 0, 0, 1, 1]
dy_list = [-1, 0, -1, 1, 0, 1]

ans = 0
for v in xy_list:
    x = v[0]
    y = v[1]
    ans += 1
    for dx, dy in zip(dx_list, dy_list):
        if xy[y + dy][x + dx]:
            if not uf.same((y + dy) * MERGIN + (x + dx), y * MERGIN + x):
                uf.union((y + dy) * MERGIN + (x + dx), y * MERGIN + x)
                ans -= 1
print(ans)

