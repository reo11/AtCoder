import math


def solve():
    ans = 10 ** 13
    n, m = map(int, input().split())
    for a in range(1, math.ceil(math.sqrt(m)) + 1):
        b = math.ceil(1.0 * m / a)
        if a <= n and b <= n:
            ans = min(ans, a * b)
    if ans < 10 ** 13:
        print(ans)
    else:
        print(-1)


solve()
