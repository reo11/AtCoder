n, l, r = map(int, input().split())
a = []

for i in range(n):
    a.append(i + 1)

ans = a[:l - 1] + a[l - 1:r][::-1] + a[r:]
print(*ans, sep=" ")