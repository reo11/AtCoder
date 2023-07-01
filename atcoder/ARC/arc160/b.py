import math

MOD = 998244353
t = int(input())


def solve_base(n):
    ans = []
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for z in range(1, n + 1):
                if x * y <= n and y * z <= n and z * x <= n:
                    ans.append(f"{x}_{y}_{z}")
    ans = set(ans)
    return len(ans) % MOD


def solve1(n):
    sqrt_n = math.floor(math.sqrt(n))
    sum1 = 0
    # 1 ~ sqrt_nまでのx, y, zの組み合わせ数
    sum1 += sqrt_n ** 3
    sum1 %= MOD
    # sqrt_n + 1 ~ nまでのx, y, zの組み合わせ数
    # sum1 -= 1
    s = 0
    for x in range(1, math.ceil(math.sqrt(n))):
        s += (math.floor(n / x) - math.floor(n / (x + 1))) * (x ** 2)
        s %= MOD
    sum1 += s * 3
    sum1 %= MOD
    return sum1


ans = []
ans_base = []
for _ in range(t):
    n = int(input())
    ans.append(solve1(n))
    # ans_base.append(solve_base(n))
print(*ans, sep=" ")
print(*ans_base, sep=" ")
