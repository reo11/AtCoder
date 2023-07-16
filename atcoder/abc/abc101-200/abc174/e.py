import math
from typing import List

n, k = map(int, input().split())
a = list(map(int, input().split()))


def slice_count(default_l: int, result_l: float) -> int:
    if result_l == 0:
        return math.inf
    else:
        return max(math.ceil(1.0 * default_l / result_l) - 1, 0)


def slice_count_all(a: List[int], result_l: float) -> int:
    count = 0
    for a_i in a:
        count += slice_count(a_i, result_l)
    return count


result_l = max(a)

i = result_l / 2.0
while i > 0.000001:
    cut_count = slice_count_all(a, result_l)
    if cut_count > k:
        result_l = result_l + i
    else:
        result_l = result_l - i
    i /= 2.0

if slice_count_all(a, math.floor(result_l)) == k:
    result_l = math.floor(result_l)
else:
    result_l = math.ceil(result_l)

print(result_l)
