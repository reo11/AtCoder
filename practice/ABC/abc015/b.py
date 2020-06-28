from math import ceil
n = int(input())
a = list(map(int, input().split()))

size = 0
for i in range(n):
    if a[i] != 0:
        size += 1

print(ceil(sum(a) / size))

