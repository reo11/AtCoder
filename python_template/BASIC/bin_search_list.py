import bisect


# 試作中
def bin_search_list(a, min_v, max_v):
    # a is sorted
    left = bisect.bisect_left(a, min_v)
    right = bisect.bisect_left(a, max_v)
    size = right - left + 1
    return size
