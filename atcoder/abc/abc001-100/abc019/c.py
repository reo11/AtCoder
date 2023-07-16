n = int(input())
a = list(map(int, input().split()))
a.sort()
d = {}
count = 0
for i in range(n):
    while a[i] % 2 == 0:
        a[i] //= 2
    try:
        d[a[i]] += 1
    except Exception:
        d[a[i]] = 1
        count += 1
print(count)
