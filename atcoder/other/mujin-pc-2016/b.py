from math import pi

l_ = list(map(int, input().split()))
max_r = sum(l_)
min_r = max(0, max(l_) - (sum(l_) - max(l_)))


def area(r):
    return r * r * pi


print(area(max_r) - area(min_r))
