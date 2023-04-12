import math
x, y, a, b, c = map(int, input().split())

def solve(ta, tb, tc, x, y):
    # 縦長横長を試して、他は適当に埋める
    # 横長
    try:
        y1 = math.ceil(ta / x)
        x2 = math.ceil(tb / (y - y1))
        success1 = x * y1 >= ta and x2 * (y - y1) >= tb and (x - x2) * (y - y1) >= tc
    except:
        success1 = False

    # 縦長
    try:
        x1 = math.ceil(ta / y)
        y2 = math.ceil(tb / (x - x1))
        success2 = y * x1 >= ta and y2 * (x - x1) >= tb and (y - y2) * (x - x1) >= tc
    except:
        success2 = False

    # 縦3つ
    try:
        x1 = math.ceil(ta / y)
        x2 = math.ceil(tb / y)
        success3 = y * x1 >= ta and y * x2 >= tb and y * (x - (x1 + x2)) >= tc
    except:
        success3 = False

    # 横3つ
    try:
        y1 = math.ceil(ta / x)
        y2 = math.ceil(tb / x)
        success4 = y1 * x >= ta and y2 * x >= tb and (y - (y1 + y2)) * x >= tc
    except:
        success4 = False
    return success1 or success2 or success3 or success4

if solve(a, b, c, x, y) or solve(b, a, c, x, y) or solve(c, a, b, x, y):
    print("Yes")
else:
    print("No")