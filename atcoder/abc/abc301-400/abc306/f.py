import sys
from collections import defaultdict
from typing import List

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = []
all = []
for _ in range(n):
    a_i = list(map(int, input().split()))
    a.append(a_i)
    for j in a_i:
        all.append(j)
all.sort()
indexes = defaultdict(lambda: -1)
for i, all_i in enumerate(all, start=1):
    indexes[all_i] = i

for i in range(n):
    for j in range(m):
        a[i][j] = indexes[a[i][j]]
    a[i] = sorted(a[i])


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


seg_tree = SegTree((n * m) + 1, mode="sum")
seg_tree.init([1] * ((n * m) + 1))
seg_tree.update(0, 0)
# print(a)
ans = 0
for i in range(n):
    update_list = []
    for j in range(m):
        ans += seg_tree.query(0, a[i][j] - 1) + 1
        update_list.append(a[i][j])
    for a_i in update_list:
        seg_tree.update(a_i, 0)
print(ans)
