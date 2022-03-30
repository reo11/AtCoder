import numpy as np
import math
n, k, m = map(int, input().split())
a = list(map(int, input().split()))

a_sum = np.sum(a)
target = m * n

if a_sum >= target:
    print(0)
else:
    ans = target - a_sum
    if ans <= k:
        print(ans)
    else:
        print(-1)
