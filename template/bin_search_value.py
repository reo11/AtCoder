def f(m):
    global a, b, x
    return m * a + b * len(str(m)) > x

def bin_search_value(range_min, range_max):
    # f(x)が真になるものの最小と最大
    left = range_min - 1
    right = range_max + 1
    while left < right - 1:
        m = left + (right - left) // 2
        if f(m):
            right = m
        else:
            left = m
    size = right - left + 1
    return left
