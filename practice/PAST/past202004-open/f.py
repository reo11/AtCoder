from heapq import heapify, heappop, heappush
from collections import deque
n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort()
ab = deque(ab)
que = []

ans = []
money = 0
heapify(que)
for i in range(1, n+1):
    while len(ab) > 0:
        if i == ab[0][0]:
            _, b = ab.popleft()
            heappush(que, -b)
        else:
            break
    if len(que) > 0:
        b = heappop(que)
        money -= b
    ans.append(str(money))
print("\n".join(ans))
