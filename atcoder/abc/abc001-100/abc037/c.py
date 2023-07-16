n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
mul = 0
for i in range(n):
    if i < k:
        mul += 1
    if n - k < i:
        mul -= 1
    ans += a[i] * mul
print(ans)
