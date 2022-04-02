MOD = 10 ** 9 + 7
w, h = map(int, input().split())

# (h+w-2)!
v1 = 1
for i in range(2, h + w - 1):
    v1 *= i
    v1 %= MOD

# フェルマーの小定理
def rep_sqr(base, k, mod):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return (rep_sqr(base, k / 2, mod) ** 2) % mod
    else:
        return (rep_sqr(base, k - 1, mod) * base) % mod


v2 = 1
for i in range(2, h):
    v2 *= i
    v2 %= MOD
v3 = 1
for i in range(2, w):
    v3 *= i
    v3 %= MOD

v2 = rep_sqr(v2, MOD - 2, MOD)
v3 = rep_sqr(v3, MOD - 2, MOD)
ans = v1 * v2
ans %= MOD
ans = ans * v3
ans %= MOD
print(ans)
