import bisect

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans = 0
for i in range(n):
    ai = a[i]
    j = bisect.bisect_left(a, ai + m)
    ans = max(ans, j - i)
print(ans)
