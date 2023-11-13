MOD = 998244353
a = list(map(int, input().split()))
a = [ai % MOD for ai in a]
abc_value = (a[0] * a[1] * a[2]) % MOD
def_value = (a[3] * a[4] * a[5]) % MOD
ans = (abc_value - def_value) % MOD

print(ans)