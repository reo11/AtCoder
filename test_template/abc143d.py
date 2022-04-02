import bisect
from typing import List, Tuple


def bin_search_list(a: List[int], min_v: int, max_v: int) -> Tuple[int, int, int]:
    # a is sorted
    left = bisect.bisect_left(a, min_v)
    right = bisect.bisect_left(a, max_v)
    size = right - left + 1
    return left, right, size


n = int(input())
l_ = list(map(int, input().split()))
l_.sort()

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        a = l_[i]
        b = l_[j]
        left, right, size = bin_search_list(l_, max(a - b, b - a) + 1, a + b - 1)
        tmp = size
        if right >= n:
            tmp -= 1
        for k in [i, j]:
            if left <= k <= right:
                tmp -= 1
        ans = ans + max(tmp, 0)
print(ans // 3)
