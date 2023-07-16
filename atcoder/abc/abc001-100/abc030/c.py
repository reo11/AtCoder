import bisect

n, m = map(int, input().split())
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

t = 0
count = 0
for i in range(10 ** 5 + 1):
    a_idx = bisect.bisect_left(a, t)
    if a_idx >= n:
        break
    t = a[a_idx] + x
    b_idx = bisect.bisect_left(b, t)
    if b_idx >= m:
        break
    t = b[b_idx] + y
    count += 1
print(count)
