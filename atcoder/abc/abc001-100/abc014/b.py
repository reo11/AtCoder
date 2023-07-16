n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if 2 ** i & x:
        ans += a[i]
print(ans)
