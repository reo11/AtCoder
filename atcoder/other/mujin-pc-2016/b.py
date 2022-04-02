from math import pi

l = list(map(int, input().split()))
max_r = sum(l)
min_r = max(0, max(l) - (sum(l) - max(l)))


def area(r):
    return r * r * pi


print(area(max_r) - area(min_r))
