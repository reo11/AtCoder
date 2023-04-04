# + - 二通り調べればよい
def solve(x, k, d):
    x = abs(x)
    straight = min(k, x // d)
    k -= straight
    x -= d * straight

    if k % 2:
        return abs(x - d)
    else:
        return x


x, k, d = map(int, input().split())
print(solve(x, k, d))
