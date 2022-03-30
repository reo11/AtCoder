import heapq
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

q = []

for i in range(n):
    heapq.heappush(q, [-b[i], i])
count = 0
while len(q) > 0:
    idx = heapq.heappop(q)[1]
    p_idx = idx - 1
    n_idx = idx + 1
    if p_idx == -1:
        p_idx = n-1
    if n_idx == n:
        n_idx = 0
    count += 1
    b[idx] -= (b[p_idx] + b[n_idx])
    if b[idx] == a[idx]:
        continue
    if b[idx] < 0:
        print(-1)
        exit()
    else:
        heapq.heappush(q, [-b[idx], idx])
print(count)
