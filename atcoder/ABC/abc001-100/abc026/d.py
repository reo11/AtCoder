from math import pi, sin

a, b, c = map(int, input().split())


def f(t):
    return a * t + b * sin(c * t * pi)


l = 0
r = 200

while (r - l) > 10 ** (-10):
    mid = (r + l) / 2
    if f(mid) <= 100:
        l = mid
    else:
        r = mid
print(l)
