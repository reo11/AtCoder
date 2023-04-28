from typing import List

class SegTree:
    def __init__(self, n: int, e: int) -> None:
        self.e = e  # 単位元
        self.tree_size = 2 ** (n - 1).bit_length()  # n以上の最小の2のべき乗数
        self.tree_value = [self.e] * 2 * self.tree_size

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

    def op(self, a: int, b: int):
        return min(a, b)

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
            self.tree_value[i] = self.op(self.tree_value[2 * i + 1], self.tree_value[2 * i + 2])

    def update(self, pos: int, value: int) -> None:
        pos += self.tree_size - 1
        self.tree_value[pos] = value
        while pos:
            pos = (pos - 1) // 2
            self.tree_value[pos] = self.op(self.tree_value[pos * 2 + 1], self.tree_value[pos * 2 + 2])

    def query(self, l: int, r: int) -> int:
        r += 1
        if r <= l:
            return self.e
        l += self.tree_size - 1
        r += self.tree_size - 2
        res = self.e
        while r - l > 1:
            if l & 1 == 0:
                res = self.op(res, self.tree_value[l])
            if r & 1 == 1:
                res = self.op(res, self.tree_value[r])
                r -= 1
            l = l // 2
            r = (r - 1) // 2
        if l == r:
            res = self.op(res, self.tree_value[l])
        else:
            res = self.op(self.op(res, self.tree_value[l]), self.tree_value[r])
        return res