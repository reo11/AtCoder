from collections import deque
from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
a.sort()
a = deque(a)

ans = 0
while a:
    ai = a.popleft()
    l = bisect_left(a, ai)
    r = bisect_right(a, ai * 2)

for i in range(n):
    for j in range(i + 1, n):
        ans += a[j] // a[i]
print(ans)