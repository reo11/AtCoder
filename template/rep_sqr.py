n, mod, p = map(int, input().split())

# 繰り返し二乗法


def rep_sqr(base, k, mod):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return (rep_sqr(base, k / 2, mod) ** 2) % mod
    else:
        return (rep_sqr(base, k - 1, mod) * base) % mod


ans = rep_sqr(n, p, mod)

print(ans)
