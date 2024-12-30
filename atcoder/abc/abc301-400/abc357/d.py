n = int(input())
MOD = 998244353

ans = 0
keta = len(str(n))
keta_mod = 0
keta_mod_memo = [1]

# 繰り返し二乗法
def rep_pow(base, k, mod=MOD):
    ans = 1
    while k > 0:
        if k & 1:
            ans = ans * base % mod
        base = base * base % mod
        k >>= 1
    return ans

# 等比数列の和
sn = ((rep_pow(10, n * keta, MOD) - 1) * rep_pow(((10**keta - 1) % MOD), MOD - 2, MOD)) % MOD
ans = (n % MOD) * sn % MOD

print(ans)