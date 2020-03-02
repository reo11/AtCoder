def f(m):
    global a, b, x
    return m * a + b * len(str(m)) > x

def bin_search(range_min, range_max):
    left = range_min - 1
    right = range_max + 1
    while left < right - 1:
        m = left + (right - left) // 2
        if f(m):
            right = m
        else:
            left = m
    return left

a, b, x = map(int, input().split())
print(bin_search(1, 10**9))
