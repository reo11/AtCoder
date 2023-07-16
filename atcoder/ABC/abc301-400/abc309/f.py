import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


class SegTree:
    def __init__(self, n: int) -> None:
        self.e = float("inf")  # 単位元
        self.tree_size = 2 ** (n - 1).bit_length()  # n以上の最小の2のべき乗数
        self.tree_value = [self.e] * 2 * self.tree_size

    def _op(self, a: int, b: int):
        return min(a, b)

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


n = int(input())
hwd = []
values = set()
for _ in [0] * n:
    h, w, d = map(int, input().split())
    h, w, d = sorted([h, w, d])
    # h, w, dを入れ替えた6パターンを用意してListに入れる
    values.add(w)
    hwd.append([h, w, d])

# 座標圧縮して10**9を10**5に収める
values = sorted(values)
compresser = defaultdict(lambda: 0)
for i, c in enumerate(values, start=1):
    compresser[c] = i
max_value = len(values)

# hash化
nums = set()
search_lists = defaultdict(lambda: [])
for h, w, d in hwd:
    search_lists[h].append([compresser[w], d])
    nums.add(h)
nums = sorted(nums)

# セグ木で判定する
# 区間最小と1点更新ができれば良い
segtree = SegTree(n=max_value + 1)
flag = False
for h in nums:
    # hが小さいものから見ているので、hを比較する必要はない
    for w, d in search_lists[h]:
        # wより小さいiの区間の最小値がdより小さいかを確認
        l = 0
        r = w - 1
        min_d = segtree.query(l, r)
        if min_d < d:
            flag = True
            break
    if flag:
        break
    # 一点更新をvsに対して一斉に行う
    for w, d in search_lists[h]:
        if segtree.query(w, w) > d:
            segtree.update(w, d)
# print(hwd)
if flag:
    print("Yes")
else:
    print("No")
