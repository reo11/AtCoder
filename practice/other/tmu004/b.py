import heapq

n = int(input())
a = list(map(int, input().split()))

plus = [0] * (3 * n)
tmp = a[:n]
s = sum(tmp)
heapq.heapify(tmp)
for i in range(n, 2*n):
    plus[i-1] = s
    heapq.heappush(tmp, a[i])
    s += a[i]
    s -= tmp[0]
    heapq.heappop(tmp)
plus[2*n-1] = s

a = [-x for x in a][::-1]
minus = [0] * (3 * n)
tmp = a[:n]
s = sum(tmp)
heapq.heapify(tmp)
for i in range(n, 2*n):
    minus[i-1] = s
    heapq.heappush(tmp, a[i])
    s += a[i]
    s -= tmp[0]
    heapq.heappop(tmp)
minus[2*n-1] = s
minus = minus[::-1]
ans = plus[n-1] + minus[n]
for i in range(n-1, 2*n):
    ans = max(ans, plus[i] + minus[i+1])

print(ans)