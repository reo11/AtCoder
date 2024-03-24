from collections import defaultdict
from functools import lru_cache

n = int(input())
s = list(input())
t = list(input())

# 二分探索っぽい雰囲気は感じる
# sのx文字目以降のcの数を記録しおく
INF = float("inf")

@lru_cache(maxsize=None)
def fmt(c):
    return ord(c) - ord("a")

s_count = [[0 for _ in range(26)] for _ in range(len(s) + 1)]

for i in reversed(range(len(s))):
    s_count[i][fmt(s[i])] += 1
    for j in range(26):
        s_count[i][j] += s_count[i + 1][j]

def check(t, x):
    # tのそれぞれの文字をx回繰り返す場合に必要なsの数
    # これがnを上回るか否かで判定
    need_count = 0
    pre_idx = len(s)
    for ti in t:
        if s_count[0][fmt(ti)] == 0:
            return INF
        # 最低限必要なsの数
        ti_x = x
        need_count_i = 0
        # 1つ前の残り、必要な分の残りを考える必要がある
        if pre_idx < len(s) - 1:
            if ti_x - s_count[pre_idx + 1][fmt(ti)] > 0:
                # 残っているが、それだけでは足りないパターン
                ti_x -= s_count[pre_idx + 1][fmt(ti)]
                need_count_i += ti_x // s_count[0][fmt(ti)]
                if ti_x % s_count[0][fmt(ti)] != 0:
                    need_count_i += 1
                ti_x -= s_count[0][fmt(ti)] * max(need_count_i - 1, 0)
                l = 0
                r = len(s)

                while r - l > 1:
                    m = (l + r) // 2
                    if s_count[0][fmt(ti)] - s_count[m][fmt(ti)] < ti_x:
                        r = m
                    else:
                        l = m
                pre_idx = l
            else:
                # 残っていて、それだけで足りるパターン
                l = pre_idx + 1
                r = len(s)
                while r - l > 1:
                    m = (l + r) // 2
                    if s_count[pre_idx + 1][fmt(ti)] - s_count[m][fmt(ti)] < ti_x:
                        r = m
                    else:
                        l = m
                # print(t, x, l, r, ti)
                pre_idx = l
        else:
            # 前回のやつは使い切ってるパターン
            need_count_i += ti_x // s_count[0][fmt(ti)]
            if ti_x % s_count[0][fmt(ti)] != 0:
                need_count_i += 1
            ti_x -= s_count[0][fmt(ti)] * max(need_count_i - 1, 0)
            l = 0
            r = len(s)

            while r - l > 1:
                m = (l + r) // 2
                if s_count[0][fmt(ti)] - s_count[m][fmt(ti)] < ti_x:
                    r = m
                else:
                    l = m
            pre_idx = l
        need_count += need_count_i
        print(ti, x, need_count, need_count_i, pre_idx, s_count[pre_idx][fmt(ti)])
    return need_count

def solve(n, s, t):
    # 二分探索
    l = 0
    r = 10 ** 13
    while r - l > 1:
        m = (l + r) // 2
        num = check(t, m)
        print(num > n, num, t, m)
        if num > n:
            r = m
        else:
            l = m
    return l

print(solve(n, s, t))

# sを繰り返す部分考えてなかった〜hoge~