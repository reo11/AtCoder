from typing import Dict, List
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

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


h, w = map(int, input().split())
q = int(input())
queries = []
for _ in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

# UnionFindで各頂点を繋ぐ
def point_num(i, j):
    return (i * w + j)

def in_board(i, j):
    return 0 <= i and i < h and 0 <= j and j < w

tree = UnionFind(n = h * w)
red = [[False for _ in range(w)] for _ in range(h)]
ans = []
for query in queries:
    if query[0] == 1:
        r = query[1] - 1
        c = query[2] - 1
        red[r][c] = True
        for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            if in_board(r + dr, c + dc):
                if red[r + dr][c + dc]:
                    tree.union(point_num(r, c), point_num(r + dr, c + dc))
    else:
        ra = query[1] - 1
        ca = query[2] - 1
        rb = query[3] - 1
        cb = query[4] - 1
        # print(point_num(ra, ca), point_num(rb, cb))
        # print(tree.find(point_num(ra, ca)))
        if red[ra][ca] and red[rb][cb]:
            if tree.same(point_num(ra, ca), point_num(rb, cb)) and tree.find(point_num(ra, ca)) != -1:
                ans.append("Yes")
            elif ra == rb and ca == cb:
                ans.append("Yes")
            else:
                ans.append("No")
        else:
            ans.append("No")
# print(tree)
print(*ans, sep="\n")
