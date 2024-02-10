from math import gcd
from typing import List

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 区間加算ができるデータ構造を使う

class BIT:
    # https://tjkendev.github.io/procon-library/python/range_query/rsq_raq_bit.html
    def __init__(self, N):
        self.N = N
        self.data0 = [0]*(N+1)
        self.data1 = [0]*(N+1)

    def _add(self, data, k, x):
        while k <= self.N:
            data[k] += x
            k += k & -k

    def add(self, l, r, x):
        self._add(self.data0, l, -x*(l-1))
        self._add(self.data0, r, x*(r-1))
        self._add(self.data1, l, x)
        self._add(self.data1, r, -x)

    # 区間[l, r)の和を求める
    def _get(self, data, k):
        s = 0
        while k:
            s += data[k]
            k -= k & -k
        return s

    def query(self, l, r):
        return self._get(self.data1, r-1) * (r-1) + self._get(self.data0, r-1) - self._get(self.data1, l-1) * (l-1) - self._get(self.data0, l-1)

tree = BIT(n)
for i in range(1, n + 1):
    tree.add(i, i + 1, a[i - 1])

def display_tree(tree):
    res = []
    for i in range(1, n + 1):
        res.append(tree.query(i, i + 1))
    print(*res, sep=" ")

# display_tree(tree)

for bi in b:
    # biに入ってる値を配る
    bi += 1
    cnt = tree.query(bi, bi + 1)
    tree.add(bi, bi + 1, -cnt)
    x = cnt // n
    y = cnt % n

    # 周回する分
    tree.add(1, n + 1, x)

    if bi == n:
        l1 = 1
    else:
        l1 = bi + 1
    if l1 + y > n:
        r1 = n
        l2 = 1
        r2 = y - (r1 - l1 + 1)
        tree.add(l1, r1 + 1, 1)
        tree.add(l2, r2 + 1, 1)
    else:
        r1 = l1 + y
        tree.add(l1, r1, 1)
    # display_tree(tree)
ans = []

for i in range(1, n + 1):
    ans.append(tree.query(i, i + 1))
print(*ans, sep=" ")

