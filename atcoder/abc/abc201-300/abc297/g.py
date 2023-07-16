import bisect
import functools
import operator


@functools.lru_cache(maxsize=None)
def dp(right):
    if right < l:
        return False
    if right == l:
        return a[right] <= right - l

    res = False
    for j in range(right - l + 1):
        if a[right - j] <= j and not dp(right - j - 1):
            res = True
            break

    return res


n, l, r = map(int, input().split())
a = list(map(int, input().split()))

# 座標圧縮
b = sorted(set(a))
a = [bisect.bisect_left(b, x) for x in a]
l = bisect.bisect_left(b, l)
r = bisect.bisect_right(b, r) - 1

# 出力
print("First" if dp(r) else "Second")
