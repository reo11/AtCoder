from collections import deque

n, k = map(int, input().split())
a = list(map(int, input().split()))

queue = deque(a)

capacity = k
count = 0
while queue:
    if capacity >= queue[0]:
        capacity -= queue.popleft()
    else:
        capacity = k
        count += 1

if capacity < k:
    count += 1

print(count)