from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))
a = sorted(a)

ans = 0

for i in range(n):
    ai = a[i]
    ans += ai * (n - 1)
    idx = bisect_left(a, 10**8 - ai)
    if idx <= i:
        idx += 1
    ans -= (10**8//2) * (n - idx)

print(ans)