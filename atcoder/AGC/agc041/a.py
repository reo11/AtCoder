import math

n, a, b = map(int, input().split())

if abs(a - b) % 2 == 0:
    print(abs(a - b) // 2)
else:
    ans1 = abs(1 - (b - abs(1 - a) - 1)) // 2 + abs(1 - a) + 1
    ans2 = abs(n - (a + abs(n - b) + 1)) // 2 + abs(n - b) + 1
    print(min(ans1, ans2))
