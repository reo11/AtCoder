from collections import deque
from time import time
from bisect import bisect_left, bisect_right
INF = float('inf')

start_at = time()
n, k = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)

ans = 0
def calc_score(x):
    score = 0
    n = len(x)
    for i in range(n - 1):
        score += (x[i + 1] - x[i]) % k
        # print(x[i + 1], x[i], score)
    return score

cumsum = [0] * (n)
for i in range(n - 1):
    cumsum[i + 1] = cumsum[i] + (a[i + 1] - a[i]) % k

for start_idx in range(n):
    ansi = cumsum[-1] - cumsum[start_idx]
    if start_idx > 1:
        ansi += cumsum[start_idx - 1]
    if start_idx > 0:
        ansi += (a[0] - a[-1]) % k
    # print(start_idx, ansi, cumsum[-1] - cumsum[start_idx], cumsum[start_idx])
    ans = max(ans, ansi)

print(ans)

