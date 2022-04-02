import math


def dis(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


n = int(input())
x = [0] * n
y = [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())

ans = -(10 ** 9)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        d = dis(x[i], y[i], x[j], y[j])
        if d > ans:
            ans = d
print(ans)
