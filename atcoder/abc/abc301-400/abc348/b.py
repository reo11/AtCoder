n = int(input())
xyi = []

for i in range(n):
    x, y = map(int, input().split())
    xyi.append((x, y, i + 1))

def squared_distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

ans = []
for i in range(n):
    x1, y1, i1 = xyi[i]
    candidate = [-1, 0]
    for j in range(n):
        if i == j:
            continue
        x2, y2, i2 = xyi[j]
        disti = squared_distance(x1, y1, x2, y2)
        if candidate[1] < disti:
            candidate = [i2, disti]
    ans.append(candidate[0])

print(*ans, sep="\n")