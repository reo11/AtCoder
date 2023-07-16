import bisect
import time
from typing import List

n, k = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)
takahashi = 0
aoki = 0
count = n
status = 0

while count > 0:
    i = bisect.bisect_right(a, count) - 1
    # time.sleep(2)
    minus_count = a[i]
    if i <= 0:
        if count < a[0]:
            break
        else:
            minus_count = a[i]

    # いっぺんに処理
    c = count // minus_count
    # print(count, i, c, minus_count)

    if c % 2:
        if status == 0:
            takahashi += (c // 2 + 1) * minus_count
            aoki += (c // 2) * minus_count
            status = 1
        else:
            takahashi += (c // 2) * minus_count
            aoki += (c // 2 + 1) * minus_count
            status = 0
    else:
        takahashi += (c // 2) * minus_count
        aoki += (c // 2) * minus_count

    count -= c * minus_count
    # print(takahashi)
print(takahashi)
