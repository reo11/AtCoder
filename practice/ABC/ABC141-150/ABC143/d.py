import bisect

n = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0

for i in range(n):
    for j in range(i, n):
        a = l[i]
        b = l[j]
        left = bisect.bisect_left(l, abs(a-b))
        right = bisect.bisect_left(l, (a+b))
        ans += right - left
        print(left, right)
print(ans)
