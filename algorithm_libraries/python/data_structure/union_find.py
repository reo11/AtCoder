from typing import List


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

    def unite(self, x: int, y: int) -> None:
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


if __name__ == "__main__":
    N, Q = map(int, input().split())
    uf = UnionFind(N + 1)
    for i in range(Q):
        T, U, V = map(int, input().split())
        if T == 0:
            uf.unite(U, V)
        else:
            if uf.same(U, V):
                print(1)
            else:
                print(0)
