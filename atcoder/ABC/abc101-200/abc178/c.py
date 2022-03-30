n = int(input())
MOD = 10**9+7
if n == 1:
    print(0)
else:
    ans = 1
    for i in range(n):
        ans *= 10
        ans %= MOD

    p1 = 1
    for i in range(n):
        p1 *= 8
        p1 %= MOD
    p2 = 1
    for i in range(n):
        p2 *= 9
        p2 %= MOD
    ans -= (-p1 + p2 + p2)
    ans %= MOD
    print(ans)
