import sys
input = sys.stdin.readline

import heapq

n, m = map(int, input().split())
ab = []

for i in range(n):
    a, b = map(int, input().split())
    ab.append([a, -b])
ab.sort()

l = []

idx = 0
ans = 0
for i in range(1, m+1):
    while idx < n and ab[idx][0] <= i:
        heapq.heappush(l, ab[idx][1])
        idx += 1
    if len(l) > 0:
        ans -= heapq.heappop(l)

print(ans)
