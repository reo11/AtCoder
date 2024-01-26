import itertools
import math

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
# coding: utf-8


def circumcenter(x1, y1, x2, y2, x3, y3):
    # length of each side squared and area of the triangle
    a2 = (x2 - x3) ** 2 + (y2 - y3) ** 2
    b2 = (x1 - x3) ** 2 + (y1 - y3) ** 2
    c2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
    area = ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2

    # is_triangle
    if area == 0:
        ab = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        bc = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        ca = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        m = max(ab, bc, ca)
        if m == ab:
            return (
                (x1 - x2) / 2,
                (y1 - y2) / 2,
                math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2),
            )
        elif m == bc:
            return (
                (x2 - x3) / 2,
                (y2 - y3) / 2,
                math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2),
            )
        else:
            return (
                (x3 - x1) / 2,
                (y3 - y1) / 2,
                math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2),
            )

    # circumcenter coordinate and radius
    x = (
        a2 * (b2 + c2 - a2) * x1 + b2 * (c2 + a2 - b2) * x2 + c2 * (a2 + b2 - c2) * x3
    ) / (16 * area * area)
    y = (
        a2 * (b2 + c2 - a2) * y1 + b2 * (c2 + a2 - b2) * y2 + c2 * (a2 + b2 - c2) * y3
    ) / (16 * area * area)
    r = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)

    # return the equation
    return x, y, r


ans = 10**15
if n > 2:
    for a, b, c in itertools.combinations(range(n), 3):
        cx, cy, cr = circumcenter(
            xy[a][0], xy[a][1], xy[b][0], xy[b][1], xy[c][0], xy[c][1]
        )
        # check
        rr = cr**2
        flag = True
        for i in range(n):
            x, y = xy[i]
            if (cx - x) ** 2 + (cy - y) ** 2 > rr:
                flag = False
                break
        if flag:
            ans = min(ans, cr)
else:
    ans = math.sqrt((xy[0][0] - xy[1][0]) ** 2 + (xy[0][1] - xy[1][1]) ** 2) / 2
print(ans)
