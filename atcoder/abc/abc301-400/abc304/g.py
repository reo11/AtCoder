n = int(input())
a = list(map(int, input().split()))

# n個の要素の過半数をmにできるかどうか
# 二分探索


def is_ok(m):
    return True


l = 0
r = 10 ** 12
while r - l > 1:
    m = (l + r) // 2
    if is_ok(m):
        r = m
    else:
        l = m
print(l)
