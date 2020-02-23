n, m, p = map(int, input().split())

def rep_sqr(base, k, mod=10**9+7):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return (rep_sqr(base, k / 2, mod) ** 2) % mod
    else:
        return (rep_sqr(base, k - 1, mod) * base) % mod

print(rep_sqr(n, p, m))