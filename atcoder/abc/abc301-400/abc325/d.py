import heapq
from collections import deque
n = int(input())
td = []

for _ in range(n):
    ti, di = map(int, input().split())
    td.append([ti, ti + di])
td.sort()
td = deque(td)

que = []
heapq.heapify(que)
current_time = 0
ans = 0
while True:
    # current_timeに処理可能なものをqueに入れる
    while td:
        if td[0][0] <= current_time:
            ti, endat = td.popleft()
            heapq.heappush(que, endat)
        else:
            break

    while que:
        endat = heapq.heappop(que)
        if endat < current_time:
            continue
        ans += 1
        current_time += 1
        while td:
            if td[0][0] <= current_time:
                ti, endat = td.popleft()
                heapq.heappush(que, endat)
            else:
                break

    if td:
        current_time = max(current_time, td[0][0])
    else:
        break

print(ans)