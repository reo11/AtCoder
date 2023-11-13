import itertools
import math
s = []
for _ in range(9):
    si = list(input())
    s.append(si)
ans = 0

def dist(xy1, xy2):
    return math.sqrt((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2)

def check(xy):
    xy1 = xy[0]
    xy2 = xy[1]
    xy3 = xy[2]
    xy4 =
    if xy1 == xy2 or xy1 == xy3 or xy2 == xy3:
        return False
    dist1 = dist(xy1, xy2)
    dist2 = dist(xy2, xy3)
    dist3 = dist(xy3, xy1)
    if dist1 != dist2 or dist1 != dist3:
        return False
    return True

ans = 0
for p in itertools.product(range(9), repeat=6):
    xy = []
    for i in range(3):
        xy.append([p[i], p[i+3]])
    ans += check(xy)
    print(ans)

print(ans)