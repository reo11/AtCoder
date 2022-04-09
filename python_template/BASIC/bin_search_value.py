def sample_f(m: int) -> bool:
    return m < 10


# めぐる式二分探索
# https://qiita.com/drken/items/97e37dd6143e33a64c8c
"""
- leftは常にTrue
- rightは常にFalse
- right - left = 1になるまで狭める
"""


def bin_search_value(range_min: int, range_max: int) -> int:
    # f(x)が真になるものの最小と最大
    left = range_min - 1
    right = range_max + 1
    while right - left > 1:
        mid = left + (right - left) // 2
        # FIXME: 任意の判定式にする
        if sample_f(mid):
            right = mid
        else:
            left = mid
    return left
