from collections import defaultdict
from math import gcd

n = int(input())
a = list(map(int, input().split()))

class SegTree:
    def __init__(self, n: int, mode: str = "min") -> None:
        self.mode = mode
        unit_elements = {
            "min": 10**13,
            "max": -(10**13),
            "sum": 0,
            "mul": 1,
            "gcd": 0,
        }
        self.e = unit_elements[self.mode]  # 単位元
        self.tree_size = 2 ** (n - 1).bit_length()  # n以上の最小の2のべき乗数
        self.tree_value = [self.e] * 2 * self.tree_size

    def __str__(self) -> str:
        if self.tree_size > 2**4:
            return "Segtree size too big"
        out = ""
        i = 0
        j = 0
        count = 1
        while i < self.tree_size - 1:
            if self.tree_value[i] == self.e:
                s = "-"
            else:
                s = str(self.tree_value[i])
            s = s.center((self.tree_size * 2) // count, " ")
            out += s
            i += 1
            j += 1
            if j == count:
                count *= 2
                j = 0
                out += "\n"
        return out

    def _op(self, a: int, b: int) -> int:
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

# 予め座標圧縮 + セグ木

pos_num = defaultdict(lambda: len(pos_num))

for ai in sorted(a):
    pos_num[ai]

sum_tree = SegTree(n + 1, mode="sum")
counter_tree = SegTree(n + 1, mode="sum")
ans = 0
for ai in a:
    idx = pos_num[ai]

    # それまでの数値とあれこれする
    ans += counter_tree.query(0, idx) * ai - sum_tree.query(0, idx)
    num = sum_tree.query(idx, idx)
    sum_tree.update(idx, num + ai)
    cnt = counter_tree.query(idx, idx)
    counter_tree.update(idx, cnt + 1)
print(ans)
