def gcd(a: int, b: int) -> int:
    # 最大公約数
    # (12, 18) -> 6
    while b:
        a, b = b, a % b
    return a


a, b, c = map(int, input().split())

g = gcd(gcd(a, b), c)

ans = 0
for i in [a, b, c]:
    ans += i // g - 1
print(ans)
