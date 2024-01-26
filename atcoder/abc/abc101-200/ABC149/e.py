import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

left = 0
right = 10**12
while right - left > 1:
    mid = (left + right) // 2
    cnt = 0
    for i in range(n):
        cnt += bisect.bisect_left(a, mid - a[i])
    print(mid, cnt)
    if cnt >= m:
        right = mid
    else:
        left = mid
print(left, right)
# wakaran
