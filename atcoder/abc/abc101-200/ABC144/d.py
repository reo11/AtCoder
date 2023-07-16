from math import atan, degrees

a, b, x = map(int, input().split())

if a * a * b / 2 >= x:
    ans = 90 - degrees(atan((2 * x) / (a * b * b)))
else:
    ans = degrees(atan((2 * ((a ** 2 * b) - x)) / (a ** 3)))
print(ans)
