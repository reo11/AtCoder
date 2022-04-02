# 繰り返し二乗法
def rep_sqr(base: int, k: int, mod: int = 10 ** 9 + 7) -> int:
    ans = 1
    while k > 0:
        if k & 1:
            ans = ans * base % mod
        base = base * base % mod
        k >>= 1
    return ans


n, m, p = map(int, input().split())
print(rep_sqr(n, p, m))
