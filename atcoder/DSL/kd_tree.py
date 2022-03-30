import sys
from bisect import bisect, bisect_right
from itertools import chain
input = sys.stdin.readline

n = int(input())
n0 = 2**n.bit_length()
data = [None]*(n0*2)
# セグメント木の構築
def init(k, l, r):
    if r - l == 1:
        data[k] = [ys[l]]
    else:
        le = 2*k+1; ri = 2*k+2
        init(le, l, (l+r)/2)
        init(ri, (l+r)/2, r)

        # 一個下の要素をmergeする
        # (heapq.mergeがあるけど、list化すると遅くなる)
        # --> list(heapq.merge(data[le], data[ri]))
        data[k] = sorted(chain(data[le], data[ri]))
# [a, b)において、x以下の要素を取得
def query(a, b, x, k, l, r):
    if b<=l or r<=a:
        return []
    if a<=l and r<=b:
        d = data[k]
        idx = bisect_right(d, x)
        return d[:idx]
    lc = query(a, b, x, 2*k+1, l, (l+r)/2)
    rc = query(a, b, x, 2*k+2, (l+r)/2, r)
    return lc + rc
def solve(a, b, x):
    return query(a, b, x, 0, 0, n)

ps = [list(map(int, input().split())) for i in range(n)]
ps.sort()
xs = [x-1 for (x, y) in ps]
ys = [(y-1, i) for i, (x, y) in enumerate(ps)]

init(0, 0, n)

q = input()
for i in range(q):
    sx, tx, sy, ty = map(int, input().split())
    # xで探索して、左端の要素(l_idx)と右端の要素(r_idx)を求める
    l_idx = bisect(xs, sx-1)
    r_idx = bisect_right(xs, tx)
    # xで絞った要素から、sy <= y <= tyとなる(x, y)を見つける
    T = set(i for y, i in solve(l_idx, r_idx, (ty, n)))
    S = set(i for y, i in solve(l_idx, r_idx, (sy-1, n)))
    ans = list(T-S)
    ans.sort()
    for e in ans:
        print(e)
    print()