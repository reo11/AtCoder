n, t = map(int, input().split())

a = []
count = t
for _ in range(n):
    a.append(int(input()))

for i in range(1, n):
    if a[i] - a[i-1] < t:
        count += a[i] - a[i-1]
    else:
        count += t
print(count)
