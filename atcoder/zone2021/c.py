import math
import pprint
from collections import defaultdict
from itertools import combinations

MAX_VALUE = 2 * 10**9


def score(l1, l2, l3):
    # スコア計算
    maxes = [0 for _ in range(5)]
    for i in range(5):
        maxes[i] = max(maxes[i], l1[i], l2[i], l3[i])
    return min(maxes)


def check(s):
    # 判定
    m = 0
    for l in combinations(s, 3):
        l1 = l[0]
        l2 = l[1]
        l3 = l[2]
        m = max(m, score(l1, l2, l3))
    return m


def comp(l, x):
    # 圧縮
    s = defaultdict(lambda: 0)
    for status in l:
        s_i = ""
        for v in status:
            if v >= x:
                s_i += "1"
            else:
                s_i += "0"
        s[s_i] += 1
    res = []
    for k, v in s.items():
        r_i = []
        if v > 3:
            v = 3
        for c in list(k):
            r_i.append(int(c))
        for i in range(v):
            res.append(r_i)
    return res


def bin_search(lists, l, r):
    left = l - 1
    right = r + 1
    while right - left > 1:
        mid = left + (right - left) // 2
        cs = comp(lists, mid)
        c = check(cs)
        # print(left, mid, right, cs, c)
        if not c:
            right = mid
        else:
            left = mid
    return left


n = int(input())
l = []
for i in range(n):
    l_i = list(map(int, input().split()))
    l.append(l_i)

print(bin_search(l, 1, MAX_VALUE))
