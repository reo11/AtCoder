n = int(input())
a = list(map(int, input().split()))

ans = 0
pre = -1
for i in range(n):
    if pre > a[i]:
        ans += (pre - a[i])
    else:
        pre = a[i]
print(ans)
