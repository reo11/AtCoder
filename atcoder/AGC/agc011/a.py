import sys

input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n, c, k = map(int, input().split())
t = [int(input()) for _ in range(n)]
t.sort()

l = deque([])
cnt = 0
for i in range(n):
    if len(l) > 0:
        if l[0] + k < t[i]:
            cnt += 1
            l = deque([])
    l.append(t[i])

    if len(l) >= c:
        cnt += 1
        l = deque([])
if len(l) > 0:
    cnt += 1
print(cnt)
