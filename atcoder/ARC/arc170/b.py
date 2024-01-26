import heapq
from collections import defaultdict, deque

n = int(input())
a = list(map(int, input().split()))

ap_set = defaultdict(lambda: defaultdict(lambda: -1))
for i in range(1, 11):
    for di in range(6):
        x = i
        y = i + di
        z = i + (2 * di)
        if z <= 10:
            ap_set[x][z] = y
            ap_set[z][x] = y

counter = defaultdict(lambda: [0])

for i in range(n):
    ai = a[i]
    for j in range(1, 11):
        if ai == j:
            counter[j].append(counter[j][-1] + 1)
        else:
            counter[j].append(counter[j][-1])

lr_list = []
for i in range(n - 2):
    x = a[i]
    for k in range(i + 2, n):
        z = a[k]
        y = ap_set[x][z]
        if y == -1:
            continue
        y_count = counter[y][k] - counter[y][i + 1]
        if y_count > 0:
            # print(i, k, x, y, z)
            lr_list.append((i, k))
            break

if len(lr_list) == 0:
    print(0)
    exit()

processed_nums = set()
queue = []
heapq.heapify(queue)
for i, (l, r) in enumerate(lr_list):
    heapq.heappush(queue, (r, l))

ans = 0
# print(lr_list)
for i in range(n - 2):
    while len(queue) > 0 and queue[0][1] < i:
        heapq.heappop(queue)
    if len(queue) == 0:
        break
    r, l = queue[0]
    ans += n - r

print(ans)
