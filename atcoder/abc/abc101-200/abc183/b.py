sx, sy, gx, gy = map(int, input().split())

gy = -gy
# y = a * x + b
a = (gy - sy) / (gx - sx)
b = sy - a * sx

print(-b / a)
