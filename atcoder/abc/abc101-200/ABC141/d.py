import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))

q = []

for v in a:
    heapq.heappush(q, -v)

for i in range(m):
    v = heapq.heappop(q)
    v = (-v) // 2
    heapq.heappush(q, -v)

ans = 0
for i in range(len(q)):
    ans -= q[i]

print(ans)
