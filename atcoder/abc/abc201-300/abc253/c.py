from collections import defaultdict
import heapq

q = int(input())
min_values = []
max_values = []
counter = defaultdict(int)
ans = []

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        counter[x] += 1
        heapq.heappush(min_values, x)
        heapq.heappush(max_values, -x)
    elif query[0] == 2:
        x, c = query[1], query[2]
        counter[x] = max(0, counter[x] - c)
    else:
        min_v = min_values[0]
        while counter[min_v] == 0:
            heapq.heappop(min_values)
            min_v = min_values[0]
        max_v = -max_values[0]
        while counter[max_v] == 0:
            heapq.heappop(max_values)
            max_v = -max_values[0]
        ans.append(max_v - min_v)
print(*ans, sep="\n")