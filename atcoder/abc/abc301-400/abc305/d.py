n = int(input())
a = list(map(int, input().split()))
q = int(input())
l_list = []
r_list = []
lr = []
for _ in range(q):
    l, r = map(int, input().split())
    l_list.append(l)
    r_list.append(r)
    lr.append([l, r])

# a, l, rをindexにしたセグ木を構築する

from typing import List


def gcd(a: int, b: int) -> int:
    # 最大公約数
    # (12, 18) -> 6
    while b:
        a, b = b, a % b
    return a


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


# 座標を圧縮する
idxs = set(a) | set(l_list) | set(r_list)
idxs = sorted(list(idxs))
dist_to_index = {idx: i + 1 for i, idx in enumerate(idxs)}
seg_tree = SegTree(len(idxs) + 1, mode="sum")

a_i = 1
pre_dist = 0
init_values = [0 for _ in range(len(idxs) + 1)]
for i, dist in enumerate(idxs):
    # print(a_i, dist, pre_dist)
    # 睡眠中の場合、前方に睡眠時間を入れる
    if a_i % 2 == 0:
        # print("update", dist_to_index[dist], dist - pre_dist)
        # seg_tree.update(dist_to_index[dist], dist - pre_dist)
        init_values[dist_to_index[dist]] = dist - pre_dist
    if dist == a[-1]:
        break
    if dist == a[a_i]:
        a_i += 1
    pre_dist = dist
# print(init_values)
seg_tree.init(init_values)
ans = []
for l, r in lr:
    ans.append(seg_tree.query(dist_to_index[l] + 1, dist_to_index[r]))
# print(idxs)
# print(seg_tree.tree_value)
print(*ans, sep="\n")
