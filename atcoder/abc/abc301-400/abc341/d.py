import math

n, m, k = map(int, input().split())
nm = math.lcm(n, m)


# x以下の数のnの倍数 + mの倍数 - lcm nmの倍数の数
def calc(x):
    v1 = x // n
    v2 = x // m
    v3 = x // nm
    return v1 + v2 - 2 * v3


l = 0
r = 10 ** 19

while r - l > 1:
    mid = (l + r) // 2
    if calc(mid) < k:
        l = mid
    else:
        r = mid

print(r)