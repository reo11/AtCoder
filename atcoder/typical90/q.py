import sys
from collections import defaultdict
from typing import List
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(20000000)

n, m = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(m)]

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
            "min": 10 ** 13,
            "max": -(10 ** 13),
            "sum": 0,
            "mul": 1,
            "gcd": 0,
        }
        self.e = unit_elements[self.mode]  # 単位元
        self.tree_size = 2 ** (n - 1).bit_length()  # n以上の最小の2のべき乗数
        self.tree_value = [self.e] * 2 * self.tree_size

    def __str__(self) -> str:
        if self.tree_size > 2 ** 4:
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
        self.tree_value[pos] += value
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



def solve1(n, m, lr):
    ans = 0
    for s in range(m):
        for t in range(s + 1, m):
            if (lr[s][0] < lr[t][0] and lr[t][0] < lr[s][1] and lr[s][1] < lr[t][1]) or \
                (lr[t][0] < lr[s][0] and lr[s][0] < lr[t][1] and lr[t][1] < lr[s][1]):
                ans += 1
    return ans

def solve2(n, m, lr):
    ans = m * (m - 1) // 2
    # pattern1
    counter = defaultdict(int)
    for s in range(m):
        counter[lr[s][0]] += 1
        counter[lr[s][1]] += 1
    for s in range(1, n + 1):
        if counter[s] > 1:
            ans -= (counter[s] * (counter[s] - 1)) // 2
    # pattern2
    # 累積和
    count = [0 for _ in range(n + 1)]
    cumsum = [0 for _ in range(n + 1)]
    for s in range(m):
        count[lr[s][1]] += 1
    for i in range(1, len(cumsum)):
        cumsum[i] = cumsum[i - 1] + count[i]
    for s in range(m):
        ans -= cumsum[lr[s][0] - 1]
    # pattern3
    count_l = [0 for _ in range(n + 1)]
    stock = []
    pre_r = -1
    lr.sort(key=lambda x: x[1])
    for l, r in lr:
        if pre_r == r:
            stock.append(l)
        else:
            while stock:
                v = stock.pop()
                count_l[v] += 1
            stock.append(l)
        for i in range(l + 1, r):
            ans -= count_l[i]
        pre_r = r
    return ans

def solve3(n, m, lr):
    ans = m * (m - 1) // 2
    # pattern1
    counter = defaultdict(int)
    for s in range(m):
        counter[lr[s][0]] += 1
        counter[lr[s][1]] += 1
    for s in range(1, n + 1):
        if counter[s] > 1:
            ans -= (counter[s] * (counter[s] - 1)) // 2
    # pattern2
    # 累積和
    count = [0 for _ in range(n + 1)]
    cumsum = [0 for _ in range(n + 1)]
    for s in range(m):
        count[lr[s][1]] += 1
    for i in range(1, len(cumsum)):
        cumsum[i] = cumsum[i - 1] + count[i]
    for s in range(m):
        ans -= cumsum[lr[s][0] - 1]
    # pattern3
    segtree = SegTree(n, mode="sum")
    stock = []
    pre_r = -1
    lr.sort(key=lambda x: x[1])
    for l, r in lr:
        if pre_r == r:
            stock.append(l)
        else:
            while stock:
                v = stock.pop()
                segtree.update(v, 1)
            stock.append(l)
        ans -= segtree.query(l + 1, r - 1)
        pre_r = r
    return ans

print(solve3(n, m, lr))