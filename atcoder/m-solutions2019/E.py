import math

math.factorial(5)
mod = 10**6 + 3
q = int(input())
ans = ""
for i in range(q):
    x, d, n = map(int, input().split())
    ans = 1
    for i in range(n):
        ans *= (x + i * d) % mod
        print(ans)
