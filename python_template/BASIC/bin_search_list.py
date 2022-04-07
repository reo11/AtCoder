import bisect
from typing import List


# 試作中
def bin_search_list(a: List[int], min_v: int, max_v: int) -> int:
    # a is sorted
    left = bisect.bisect_left(a, min_v)
    right = bisect.bisect_left(a, max_v)
    size = right - left + 1
    return size
