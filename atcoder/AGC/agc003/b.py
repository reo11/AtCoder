n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))

ans = 0
for i in range(n):
    if a[i] > 1:
        ans += a[i] // 2
        a[i] = a[i] % 2
    if i < n - 1 and a[i] == 1 and a[i + 1] >= 1:
        a[i] = 0
        a[i + 1] -= 1
        ans += 1
print(ans)
