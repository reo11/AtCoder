from typing import List

n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))
a_length = []
a_pre = 0

# 切れ目間の距離
for a_i in a + [l]:
    a_length.append(a_i - a_pre)
    a_pre = a_i

# 全てのピースが長さlength以上になるように切れるか
def solve(a: List[int], k: int, length: int) -> bool:
    cur_length = 0
    count = 0

    for a_i in a:
        cur_length += a_i
        if cur_length >= length:
            count += 1
            cur_length = 0

    return count >= k + 1 # k + 1ピース以上になっているか

# めぐる式二分探索
# https://qiita.com/drken/items/97e37dd6143e33a64c8c
def bin_search_value(range_min, range_max):
    # f(x)が真になるものの最小と最大
    left = range_min - 1
    right = range_max + 1
    while right - left > 1:
        mid = left + (right - left) // 2
        if not solve(a_length, k, mid):
            right = mid
        else:
            left = mid
    return left

print(bin_search_value(0, l))
