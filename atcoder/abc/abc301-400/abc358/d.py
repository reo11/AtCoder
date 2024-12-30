from bisect import bisect_left
from collections import deque
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
a = deque(a)
b = deque(b)

ans = 0

while len(a) > 0 and len(b) > 0:
    # 安いものから割り当てる
    if a[0] >= b[0]:
        x = a.popleft()
        b.popleft()
        ans += x
    else:
        a.popleft()

if len(b) > 0:
    print(-1)
else:
    print(ans)
