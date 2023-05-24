import bisect
from typing import List


# 試作中
def bin_search_list(a: List[int], v: int) -> int:
    # a is sorted
    left = bisect.bisect_left(a, v)
    return left
