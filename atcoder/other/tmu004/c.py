n = int(input())
d = [int(input()) for _ in range(n)]
d.sort()

v = 0
count = 0
for i in range(n):
    if v < d[i]:
        count += 1
        v = d[i]
print(count)
