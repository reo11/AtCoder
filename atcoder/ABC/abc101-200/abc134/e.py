from collections import deque
from bisect import bisect_left

n = int(input())
a = [int(input()) for _ in range(n)]

b = deque([])

for ai in a:
    if len(b) == 0:
        b.append(ai)
    else:
        if ai <= b[0]:
            b.appendleft(ai)
        else:
            idx = bisect_left(b, ai)
            b[idx-1] = ai

print(len(b))
