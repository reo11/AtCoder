import sys
from typing import List

input = sys.stdin.readline

n, k = map(int, input().split())
s = input()

# sのうちn - (k - 1)の要素から
# 辞書順で最も小さいものの内
# 最も左側にあるものを選択していくを繰り返す
# セグ木でlからrのうち文字cが出現する最も左側の座標をlogNで取得出来ればよい
# O(KlogN)の計算量で実装可能（アルファベット数は26で固定なので含めず）
# 無限で初期化して、最小を保持するセグ木を実装する

def gcd(a: int, b: int) -> int:
    # 最大公約数
    # (12, 18) -> 6
    while b:
        a, b = b, a % b
    return a


class SegTree:
    def __init__(self, n: int, mode: str = "min") -> None:
        self.mode = mode
        unit_elements = {"min": 10 ** 13, "max": -10 ** 13, "sum": 0, "mul": 1, "gcd": 0}
        self.e = unit_elements[self.mode]  # 単位元
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
            self.tree_value[i] = self._op(self.tree_value[2 * i + 1], self.tree_value[2 * i + 2])

    def update(self, pos: int, value: int) -> None:
        pos += self.tree_size - 1
        self.tree_value[pos] = value
        while pos:
            pos = (pos - 1) // 2
            self.tree_value[pos] = self._op(self.tree_value[pos * 2 + 1], self.tree_value[pos * 2 + 2])

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

seg_tree = [SegTree(n=n, mode="min") for _ in range(26)]
alphabets = [chr(ord('a') + i) for i in range(26)]
for c_i, c in enumerate(alphabets):
    for i in range(n):
        if s[i] == c:
            seg_tree[c_i].update(i, i)
    # print(seg_tree[c_i])

l = 0
r = (n - 1) - (k - 1)
ans = []

for i in range(k):
    for c_i, c in enumerate(alphabets):
        num = seg_tree[c_i].query(l, r)
        if num < seg_tree[c_i].e:
            ans.append(c)
            break
    l = num + 1
    r += 1
print("".join(ans))