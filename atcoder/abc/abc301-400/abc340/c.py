from collections import defaultdict, deque
import math
import heapq

n = int(input())

q = []
counter = defaultdict(int)

counter[n] = 1
heapq.heappush(q, -n)
ans = 0

while q:
    # print(q, counter)
    x = heapq.heappop(q)
    x = -x
    if x <= 1:
        continue
    if counter[x] == 0:
        continue
    cnt = counter[x]

    if x % 2 == 0:
        y = x // 2
        z = x // 2
    else:
        y = x // 2
        z = x // 2 + 1
    if y > 1:
        if counter[y] == 0:
            heapq.heappush(q, -y)
        counter[y] += cnt


    if z > 1:
        if counter[z] == 0:
            heapq.heappush(q, -z)
        counter[z] += cnt
    counter[x] = 0
    ans += x * cnt

print(ans)
