GETA = 10 ** 18
x, a, d, n = map(int, input().split())
if d < 0:
    min_value = a + d * (n - 1)
    a = min_value
    d = -d

x += GETA
a += GETA

min_value = a
max_value = a + d * (n - 1)

if x >= max_value:
    print(abs(x - max_value))
elif x <= min_value:
    print(abs(min_value - x))
else:
    y = x - a
    print(min(y % d, d - (y % d)))
