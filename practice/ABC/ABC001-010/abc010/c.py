from math import sqrt
txa, tya, txb, tyb, t, v = map(int, input().split())
n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])

count = 0

def dis(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
for i in range(n):
    x, y = xy[i]
    if dis(txa, tya, x, y) + dis(txb, tyb, x, y) <= t*v:
        count += 1
if count > 0:
    print("YES")
else:
    print("NO")
