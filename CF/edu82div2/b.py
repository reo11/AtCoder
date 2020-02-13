from math import ceil
t = int(input())
for i in range(t):
    # number of highway
    # good day
    # bad day g, b are repeated
    n, g, b = map(int, input().split())
    half_n = ceil(n/2)
    ans = 0
    if half_n > g:
        day = ceil(half_n / g) - 1
        ans = day * (g+b) + (half_n - (day * g))
    else:
        ans = half_n
    print(max(ans, n))