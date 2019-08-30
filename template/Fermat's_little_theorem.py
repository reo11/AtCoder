# フェルマーの小定理
def rep_sqr(base, k, mod):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return (rep_sqr(base, k / 2, mod) ** 2) % mod
    else:
        return (rep_sqr(base, k - 1, mod) * base) % mod

# a^(-1) == a^(m-2)
def flt(a, mod):
    return rep_sqr(a, mod-2, mod)