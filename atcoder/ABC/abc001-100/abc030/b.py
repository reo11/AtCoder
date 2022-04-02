n, m = map(int, input().split())

l = 360 * m / 60
s = 360 * n / 12 + 30 * m / 60
l %= 360
s %= 360
print(min(abs(l - s), abs((360 - l) + s), abs((360 - s) + l)))
