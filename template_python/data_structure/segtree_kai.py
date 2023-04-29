from typing import List


def gcd(a: int, b: int) -> int:
    # 最大公約数
    # (12, 18) -> 6
    while b:
        a, b = b, a % b
    return a


class SegTree:
    def __init__(self, n: int, mode: str = "min") -> None:
        self.n = n
        self.mode = mode
        unit_elements = {"min": 2 ** 31 - 1, "max": -10 ** 13, "sum": 0, "mul": 1, "gcd": 0}
        self.e = unit_elements[self.mode]  # 単位元
        self.lv = (self.n - 1).bit_length()
        self.tree_size = 2 ** self.lv  # n以上の最小の2のべき乗数
        self.tree_value = [self.e] * (2 * self.tree_size)
        self.tree_lazy = [None] * (2 * self.tree_size)

    def __str__(self) -> str:
        if self.tree_size > 2 ** 4:
            return "Segtree size too big"
        out = ""
        i = 0; j = 0; count = 1
        while i < self.tree_size - 1:
            if self.tree_value[i] == self.e:
                s = "-"
            else:
                s = str(self.tree_value[i])
            s = s.center((self.tree_size * 2) // count, " ")
            out += s; i += 1; j += 1
            if j == count:
                count *= 2
                j = 0
                out += "\n"
        return out

    def _op(self, a: int, b: int):
        if self.mode == "min":
            return min(a, b)
        elif self.mode == "max":
            return max(a, b)
        elif self.mode == "sum":
            return a + b
        elif self.mode == "mul":
            return a * b
        elif self.mode == "gcd":
            return gcd(a, b)

        raise "no method defined"

    def gindex(self, l, r):
        L = (l + self.tree_size) >> 1; R = (r + self.tree_size) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range((self.n - 1).bit_length()):
            if rc <= i:
                yield R
            if L < R and lc <= i:
                yield L
            L >>= 1; R >>= 1

    def propagates(self, *ids):
        # 遅延評価
        for i in reversed(ids):
            v = self.tree_lazy[i - 1]
            if v is None:
                continue
            self.tree_lazy[2 * i - 1] = self.tree_value[2 * i - 1] = self.tree_lazy[2 * i] = self.tree_value[2 * i] = v
            self.tree_lazy[i - 1] = None

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
            self.tree_value[i] = self._op(self.tree_value[2 * i + 1], self.tree_value[2 * i + 2])

    def update(self, pos: int, value: int) -> None:
        # 更新
        self.update_range(l=pos, r=pos+1, value=value)

    def update_range(self, l: int, r: int, value: int) -> None:
        # 区間更新[l, r)
        *ids, = self.gindex(l, r)
        self.propagates(*ids)
        L = self.tree_size + l; R = self.tree_size + r
        while L < R:
            if R & 1:
                R -= 1
                self.tree_value[R - 1] = value
                self.tree_lazy[R - 1] = value
            if L & 1:
                self.tree_value[L - 1] = value
                self.tree_lazy[L - 1] = value
                L += 1
            L >>= 1; R >>= 1
        for i in ids:
            self.tree_value[i - 1] = self._op(self.tree_value[2 * i - 1], self.tree_value[2 * i])

    def query(self, l: int, r: int) -> int:
        self.propagates(*self.gindex(l, r))
        L = self.tree_size + l; R = self.tree_size + r

        s = self.e
        while L < R:
            if R & 1:
                R -= 1
                s = self._op(s, self.tree_value[R-1])
            if L & 1:
                s = self._op(s, self.tree_value[L-1])
                L += 1
            L >>= 1; R >>= 1
        return s
