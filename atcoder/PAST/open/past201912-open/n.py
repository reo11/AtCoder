import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
INF = float("inf")
n, w, c = map(int, input().split())

que = [(0, 1, 0)]
for i in range(n):
    l, r, p = map(int, input().split())
    # (x, start:1/end:0, price)
    que.append((r, 0, -p))
    que.append((max(l-c+1, 0), 1, p))
que.sort()
que = deque(que)
ans = INF
cur_x = [0, 0]
while len(que) > 0:
    cur_x[0] = que[0][0]
    if cur_x[0] > w - c:
        break
    while len(que) > 0:
        if que[0][0] != cur_x[0]:
            break
        _, _, cost = que.popleft()
        cur_x[1] += cost
    ans = min(ans, cur_x[1])
print(ans)