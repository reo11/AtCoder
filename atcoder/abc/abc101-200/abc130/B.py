n, x = map(int, input().split())
l = list(int(i) for i in input().split())

count = 1
d = 0
for i in range(n):
    d += l[i]
    if d <= x:
        count += 1
print(count)
