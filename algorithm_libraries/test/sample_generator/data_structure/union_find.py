import random
from typing import List

# https://judge.yosupo.jp/problem/unionfind


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
    # 1 <= n <= 2 * 10**5
    # 1 <= q <= 2 * 10**5
    # t_i in {0, 1}
    # 0 <= u_i, v_i < N

    sample_size = 10

    n = random.randint(1, 2 * 10 ** 5)
    q = random.randint(1, 2 * 10 ** 5)
    out = [f"{n} {q}"]
    ans = []
    for _ in range(q):
        t = random.randint(0, 1)
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        out.append(f"{t} {u} {v}")
    print("\n".join(out))
