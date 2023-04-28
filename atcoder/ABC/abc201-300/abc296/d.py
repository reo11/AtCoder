import math

def solve():
    ans = float("inf")
    n, m = map(int, input().split())
    for a in range(1, math.ceil(math.sqrt(m)) + 1):
        b = math.ceil(1.0 * m / a)
        if a <= n and b <= n:
            ans = min(ans, a * b)
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)


solve()
