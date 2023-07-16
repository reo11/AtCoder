import math

n = int(input())
cnt = 0
for i in range(1, n):
    for j in range(1, math.ceil(n / i) + 1):
        if i * j < n:
            cnt += 1

print(cnt)
