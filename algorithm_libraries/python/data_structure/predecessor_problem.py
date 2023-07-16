from typing import List


class SegTree:
    def __init__(self, n: int, mode: str = "min") -> None:
        self.mode = mode
        unit_elements = {
            "min": 10 ** 13,
            "max": -(10 ** 13),
        }
        self.e = unit_elements[self.mode]  # 単位元
        self.tree_size = 2 ** (n - 1).bit_length()  # n以上の最小の2のべき乗数
        self.tree_value = [self.e] * 2 * self.tree_size

    def _op(self, a: int, b: int):
        if self.mode == "min":
            return min(a, b)
        elif self.mode == "max":
            return max(a, b)
        raise "no method defined"

    def init(self, init_val: List[int]) -> None:
        # 初期値が指定されている場合
        # logNの処理をまとめて実行するので、随時追加するのに比べてO(logN)程度高速
        # updateを使った初期化: O(NlogN)
        # initを使った初期化: O(N + logN)
        # set_val
        for i in range(len(init_val)):
            self.tree_value[i + self.tree_size - 1] = init_val[i]
        # built
        for i in range(self.tree_size - 2, -1, -1):
            self.tree_value[i] = self._op(
                self.tree_value[2 * i + 1], self.tree_value[2 * i + 2]
            )

    def update(self, pos: int, value: int) -> None:
        pos += self.tree_size - 1
        self.tree_value[pos] = value
        while pos:
            pos = (pos - 1) // 2
            self.tree_value[pos] = self._op(
                self.tree_value[pos * 2 + 1], self.tree_value[pos * 2 + 2]
            )

    def query(self, l: int, r: int) -> int:
        r += 1
        if r <= l:
            return self.e
        l += self.tree_size - 1
        r += self.tree_size - 2
        res = self.e
        while r - l > 1:
            if l & 1 == 0:
                res = self._op(res, self.tree_value[l])
            if r & 1 == 1:
                res = self._op(res, self.tree_value[r])
                r -= 1
            l = l // 2
            r = (r - 1) // 2
        if l == r:
            res = self._op(res, self.tree_value[l])
        else:
            res = self._op(self._op(res, self.tree_value[l]), self.tree_value[r])
        return res


class PredecessorProblem:
    def __init__(self, n: int):
        self.n = n
        self.tree_set = set()
        self.segtree_min = SegTree(n=n + 1, mode="min")
        self.segtree_max = SegTree(n=n + 1, mode="max")

    def add(self, k: int) -> None:
        if k not in self.tree_set:
            self.tree_set.add(k)
            self.segtree_min.update(k, k)
            self.segtree_max.update(k, k)

    def delete(self, k: int) -> None:
        if k in self.tree_set:
            self.tree_set.discard(k)
            self.segtree_min.update(k, self.segtree_min.e)
            self.segtree_max.update(k, self.segtree_max.e)

    def include(self, k: int) -> bool:
        if k in self.tree_set:
            return True
        else:
            return False

    def get_gt(self, k: int) -> int:
        min_value = self.segtree_min.query(k, self.n - 1)
        if min_value == self.segtree_min.e:
            return -1
        else:
            return min_value

    def get_lt(self, k: int) -> int:
        max_value = self.segtree_max.query(0, k)
        if max_value == self.segtree_max.e:
            return -1
        else:
            return max_value


if __name__ == "__main__":
    n, q = map(int, input().split())
    t = list(input())
    pp = PredecessorProblem(n)

    # 初期化
    for i, t_i in enumerate(t):
        if t_i == "1":
            pp.add(i)
    ans = []
    for _ in [0] * q:
        c, k = map(int, input().split())
        if c == 0:
            pp.add(k)
        elif c == 1:
            pp.delete(k)
        elif c == 2:
            if pp.include(k):
                ans.append(1)
            else:
                ans.append(0)
        elif c == 3:
            # k以上の最小の値
            ans.append(pp.get_gt(k))
        else:
            # k以下の最大の値
            ans.append(pp.get_lt(k))
    print(*ans, sep="\n")
