import sys
from math import ceil
from collections import deque

input = sys.stdin.readline

n, d, a = map(int, input().split())
xh = [list(map(int, input().split())) for _ in range(n)]
xh.sort()
q = deque()
ans = 0
dam = 0
for i in range(n):
    # attack
    while len(q) > 0:
        if q[0][0] < xh[i][0]:
            dam -= q[0][1]
            q.popleft()
        else:
            break
    xh[i][1] -= dam
    if xh[i][1] > 0:
        a_num = ceil(xh[i][1] / a)
        xh[i][1] -= a_num * a
        ans += a_num
        dam += a_num * a
        q.append((xh[i][0] + 2*d, a_num * a))
print(ans)
