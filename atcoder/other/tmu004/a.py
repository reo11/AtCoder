import heapq

n, k = map(int, input().split())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append([a, b])
heapq.heapify(ab)

count = 0
t = 0
for _ in range(k):
    a, b = ab[0]
    heapq.heappop(ab)
    t += a
    a += b
    heapq.heappush(ab, [a, b])
print(t)
